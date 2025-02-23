import cv2
import numpy as np

def process_image(image):
    # Resize for consistency (optional)
    image = cv2.resize(image, (640, 480))
    
    # Brightness normalization (helps in varying light)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    image = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    
    # Improved color masking (BGR space for better yellow detection)
    white_mask = cv2.inRange(image, np.array([200, 200, 200]), np.array([255, 255, 255]))
    yellow_mask = cv2.inRange(image, np.array([0, 100, 100]), np.array([80, 255, 255]))
    combined_mask = cv2.bitwise_or(white_mask, yellow_mask)
    masked = cv2.bitwise_and(image, image, mask=combined_mask)
    
    # Edge detection with adaptive thresholds
    gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    
    # Auto Canny thresholds using median
    v = np.median(blur)
    lower = int(max(0, 0.7 * v))
    upper = int(min(255, 1.3 * v))
    edges = cv2.Canny(blur, lower, upper)
    
    # Dynamic ROI (works better for hills/curves)
    height, width = edges.shape
    roi_vertices = np.array([[
        (width * 0.1, height),
        (width * 0.4, height * 0.65),
        (width * 0.6, height * 0.65),
        (width * 0.9, height)
    ]], dtype=np.int32)
    
    # ROI masking
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, roi_vertices, 255)
    roi_edges = cv2.bitwise_and(edges, mask)
    
    # Probabilistic Hough with better parameters
    lines = cv2.HoughLinesP(roi_edges, 
                           rho=1, 
                           theta=np.pi/180, 
                           threshold=30,
                           minLineLength=50,
                           maxLineGap=30)
    
    # Line filtering and averaging
    left_fit = []
    right_fit = []
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            if x1 == x2:
                continue
            
            # Calculate polynomial fit (degree 1 for straight lines)
            fit = np.polyfit((x1, x2), (y1, y2), 1)
            slope, intercept = fit[0], fit[1]
            
            # Filter based on slope and position
            if abs(slope) < 0.4:
                continue
            
            # Classify left/right using x-position at bottom
            x_bottom = (height - intercept) / slope if slope !=0 else 0
            if slope < 0 and x_bottom < width/2:
                left_fit.append((slope, intercept))
            elif slope > 0 and x_bottom > width/2:
                right_fit.append((slope, intercept))
    
    # Create averaged lines
    line_image = np.zeros_like(image)
    
    if left_fit:
        left_avg = np.mean(left_fit, axis=0)
        left_points = make_coordinates(image, left_avg)
        cv2.line(line_image, left_points[0], left_points[1], (0,255,0), 8)
    
    if right_fit:
        right_avg = np.mean(right_fit, axis=0)
        right_points = make_coordinates(image, right_avg)
        cv2.line(line_image, right_points[0], right_points[1], (0,255,0), 8)
    
    # Blend with original
    return cv2.addWeighted(image, 0.8, line_image, 1, 1)

def make_coordinates(image, line_params):
    slope, intercept = line_params
    y1 = image.shape[0]  # Bottom of image
    y2 = int(y1 * 0.65)  # Match ROI height
    x1 = int((y1 - intercept) / slope) if slope != 0 else 0
    x2 = int((y2 - intercept) / slope) if slope != 0 else 0
    return ((x1, y1), (x2, y2))

# Debugging: Uncomment to see intermediate steps
def debug_steps(image):
    cv2.imshow("Original", image)
    cv2.imshow("CLAHE Enhanced", process_image(image))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image = cv2.imread("test_image.jpg")  # Replace with your image path
    if image is None:
        print("Error loading image!")
    else:
        result = process_image(image)
        cv2.imshow("Lane Detection", result)
        # debug_steps(image)  # Uncomment to debug
        cv2.waitKey(0)
        cv2.destroyAllWindows()