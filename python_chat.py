import time
import random

class CustomerSupportChatbot:
    def __init__(self):
        self.user_name = ""
        self.conversation_history = []
        self.services = {
            "1": "Check account status",
            "2": "Billing inquiries",
            "3": "Technical support",
            "4": "Product information",
            "5": "File a complaint",
            "6": "Speak to a human agent"
        }
        
        # Sub-options for each service
        self.service_options = {
            "1": {  # Account status options
                "1": "View account balance",
                "2": "Update account information",
                "3": "Check subscription status",
                "4": "Return to main menu"
            },
            "2": {  # Billing inquiries options
                "1": "View recent transactions",
                "2": "Dispute a charge",
                "3": "Update payment method",
                "4": "Payment plans",
                "5": "Return to main menu"
            },
            "3": {  # Technical support options
                "1": "Login issues",
                "2": "App/Website not working",
                "3": "Installation help",
                "4": "Error messages",
                "5": "Return to main menu"
            },
            "4": {  # Product information options
                "1": "Features overview",
                "2": "Pricing information",
                "3": "Compatibility questions",
                "4": "Return to main menu"
            },
            "5": {  # Complaint options
                "1": "Service quality issue",
                "2": "Product defect",
                "3": "Staff behavior",
                "4": "Return to main menu"
            }
        }
        
        # Knowledge base for common technical issues
        self.tech_solutions = {
            "login": "Try clearing your browser cookies and cache, then restart your browser. If the issue persists, try resetting your password through the 'Forgot Password' link.",
            "app": "Please try the following steps:\n1. Ensure your app is updated to the latest version\n2. Restart the app\n3. Restart your device\n4. Check your internet connection",
            "installation": "For installation issues, please make sure your system meets the minimum requirements. You can find these in the documentation at docs.example.com/requirements.",
            "error": "Please take a screenshot of the error message and send it to support@example.com along with details about what you were doing when the error occurred."
        }

    def start(self):
        """Start the chatbot conversation"""
        self.display_welcome_message()
        self.get_user_name()
        
        while True:
            user_choice = self.display_main_options()
            
            if user_choice == "7":
                self.end_conversation()
                break
            
            if user_choice in self.services:
                self.handle_service(user_choice)
            else:
                print("I'm sorry, that's not a valid option. Please try again.")

    def display_welcome_message(self):
        """Display the welcome message"""
        print("\n" + "=" * 50)
        print("Welcome to our Customer Support Chatbot!")
        print("I'm here to help you with any questions or issues you might have.")
        print("=" * 50)

    def get_user_name(self):
        """Get the user's name for personalized interaction"""
        print("Before we begin, may I know your name?")
        self.user_name = input("Your name: ")
        print(f"\nNice to meet you, {self.user_name}! How can I assist you today?")
    
    def display_main_options(self):
        """Display the main service options"""
        print("\nPlease select from the following options:")
        for key, service in self.services.items():
            print(f"{key}: {service}")
        print("7: End conversation")
        
        return input("\nEnter your choice (1-7): ")
    
    def handle_service(self, service_choice):
        """Handle the selected service"""
        selected_service = self.services[service_choice]
        self.conversation_history.append(f"User selected: {selected_service}")
        
        print(f"\nYou've selected: {selected_service}")
        
        # If user wants to speak to a human agent
        if service_choice == "6":
            self.transfer_to_agent()
            return
            
        # Display sub-options for the selected service
        while True:
            print("\nWhat specifically do you need help with?")
            
            # Display options for the selected service
            for key, option in self.service_options[service_choice].items():
                print(f"{key}: {option}")
                
            sub_choice = input("\nEnter your choice: ")
            
            # Return to main menu
            if sub_choice == "4" or sub_choice == "5":  # Some menus have 4, some have 5 options
                print("Returning to main menu...")
                break
                
            # Handle the specific sub-option
            if sub_choice in self.service_options[service_choice]:
                self.handle_specific_issue(service_choice, sub_choice)
            else:
                print("I'm sorry, that's not a valid option. Please try again.")
    
    def handle_specific_issue(self, service_choice, sub_choice):
        """Handle specific issues based on user's selection"""
        selected_option = self.service_options[service_choice][sub_choice]
        self.conversation_history.append(f"User selected: {selected_option}")
        
        print(f"\nYou've selected: {selected_option}")
        
        # Simulate processing time
        print("Processing your request...")
        self.simulate_typing()
        
        # Handle each service category differently
        if service_choice == "1":  # Account status
            self.handle_account_issue(sub_choice)
        elif service_choice == "2":  # Billing
            self.handle_billing_issue(sub_choice)
        elif service_choice == "3":  # Technical support
            self.handle_technical_issue(sub_choice)
        elif service_choice == "4":  # Product information
            self.handle_product_info(sub_choice)
        elif service_choice == "5":  # Complaints
            self.handle_complaint(sub_choice)
            
        # Ask if there's anything else the user needs help with
        print("\nIs there anything else you need help with regarding this issue?")
        print("1: Yes, I need more assistance")
        print("2: No, I'm good for now")
        
        follow_up = input("\nEnter your choice (1-2): ")
        
        if follow_up == "1":
            print("Let me help you further...")
        else:
            print("Great! Let's return to the previous menu.")
    
    def handle_account_issue(self, sub_choice):
        """Handle account-related issues"""
        if sub_choice == "1":  # View account balance
            balance = random.randint(100, 1000)
            print(f"\nYour current account balance is ${balance}.00")
            print("Would you like to make a payment?")
            print("1: Yes, make a payment")
            print("2: No, just checking")
            
            payment_choice = input("\nEnter your choice (1-2): ")
            
            if payment_choice == "1":
                print("Redirecting you to our secure payment portal...")
                self.simulate_typing()
                print("You would now be redirected to make a payment in our actual system.")
            else:
                print("No problem! Your account is in good standing.")
                
        elif sub_choice == "2":  # Update account information
            print("\nWhat information would you like to update?")
            print("1: Contact information")
            print("2: Mailing address")
            print("3: Email preferences")
            print("4: Security settings")
            
            update_choice = input("\nEnter your choice (1-4): ")
            
            print("In a real system, you would now be guided through updating your selected information.")
            self.simulate_typing()
            print("Information updated successfully!")
            
        elif sub_choice == "3":  # Check subscription status
            subscription_status = random.choice(["Active", "Expiring soon", "Renewal needed"])
            print(f"\nYour subscription status is: {subscription_status}")
            
            if subscription_status != "Active":
                print("Would you like to renew your subscription?")
                print("1: Yes, renew now")
                print("2: No, maybe later")
                
                renew_choice = input("\nEnter your choice (1-2): ")
                
                if renew_choice == "1":
                    print("Processing your renewal...")
                    self.simulate_typing()
                    print("Subscription renewed successfully!")
                else:
                    print("No problem! We'll remind you again before it expires.")
            else:
                print("Your subscription is active and will renew automatically.")
    
    def handle_billing_issue(self, sub_choice):
        """Handle billing-related issues"""
        if sub_choice == "1":  # View recent transactions
            print("\nHere are your most recent transactions:")
            transactions = [
                {"date": "2025-03-01", "amount": "$45.99", "description": "Monthly subscription"},
                {"date": "2025-02-15", "amount": "$10.00", "description": "Add-on service"},
                {"date": "2025-02-01", "amount": "$45.99", "description": "Monthly subscription"}
            ]
            
            for t in transactions:
                print(f"{t['date']} - {t['amount']} - {t['description']}")
                
        elif sub_choice == "2":  # Dispute a charge
            print("\nWhich charge would you like to dispute?")
            print("1: March 1, 2025 - $45.99 - Monthly subscription")
            print("2: February 15, 2025 - $10.00 - Add-on service")
            print("3: February 1, 2025 - $45.99 - Monthly subscription")
            
            dispute_choice = input("\nEnter your choice (1-3): ")
            
            print("\nPlease tell us why you're disputing this charge:")
            print("1: Unauthorized charge")
            print("2: Incorrect amount")
            print("3: Service not received")
            print("4: Other reason")
            
            reason_choice = input("\nEnter your choice (1-4): ")
            
            print("\nThank you for providing this information. Your dispute has been filed.")
            print("Dispute reference number: #" + str(random.randint(10000, 99999)))
            print("A billing specialist will review this and contact you within 48 hours.")
            
        elif sub_choice == "3":  # Update payment method
            print("\nSelect the payment method you'd like to use:")
            print("1: Add new credit/debit card")
            print("2: Use existing payment method")
            print("3: Set up automatic bank transfer")
            
            payment_choice = input("\nEnter your choice (1-3): ")
            
            print("In a real system, you would now be guided through updating your payment method.")
            self.simulate_typing()
            print("Payment method updated successfully!")
            
        elif sub_choice == "4":  # Payment plans
            print("\nWe offer the following payment plans:")
            print("1: Monthly ($45.99/month)")
            print("2: Quarterly ($129.99/quarter - Save 5%)")
            print("3: Annual ($499.99/year - Save 10%)")
            
            plan_choice = input("\nEnter your choice (1-3): ")
            
            print("Would you like to switch to this payment plan?")
            print("1: Yes, switch now")
            print("2: No, just checking")
            
            switch_choice = input("\nEnter your choice (1-2): ")
            
            if switch_choice == "1":
                print("Processing your request...")
                self.simulate_typing()
                print("Payment plan updated successfully!")
            else:
                print("No problem! Your current payment plan remains unchanged.")
    
    def handle_technical_issue(self, sub_choice):
        """Handle technical support issues"""
        if sub_choice == "1":  # Login issues
            print(self.tech_solutions["login"])
            print("\nDid this solution help resolve your issue?")
            print("1: Yes, it's resolved")
            print("2: No, I still need help")
            
            resolved = input("\nEnter your choice (1-2): ")
            
            if resolved == "2":
                print("\nLet me connect you with our technical team for more specialized assistance.")
                print("Please provide additional details about your login issue:")
                issue_details = input("\nYour issue details: ")
                print(f"\nThank you for providing these details. A support ticket (#{random.randint(100000, 999999)}) has been created.")
                print("Our technical team will contact you within 24 hours.")
                
        elif sub_choice == "2":  # App/Website not working
            print(self.tech_solutions["app"])
            print("\nIs there a specific feature or page that's not working?")
            feature = input("\nPlease specify (or type 'all' if everything is affected): ")
            
            print(f"\nThank you for letting us know about issues with {feature}.")
            print("Let me check if there are any known outages in our system...")
            self.simulate_typing()
            
            if random.choice([True, False]):
                print("We're currently experiencing some technical difficulties with this feature.")
                print("Our team is working on it and it should be resolved within the next few hours.")
            else:
                print("There are no known outages at this time. I recommend clearing your browser cache or reinstalling the app.")
                print("Would you like me to guide you through these steps?")
                print("1: Yes, guide me through the steps")
                print("2: No, I'll try on my own")
                
                guide_choice = input("\nEnter your choice (1-2): ")
                
                if guide_choice == "1":
                    print("\nHere's how to clear your cache and cookies:")
                    print("1. Open your browser settings")
                    print("2. Navigate to Privacy & Security")
                    print("3. Select 'Clear browsing data'")
                    print("4. Check 'Cookies' and 'Cached images and files'")
                    print("5. Click 'Clear data'")
                
        elif sub_choice == "3":  # Installation help
            print(self.tech_solutions["installation"])
            print("\nWhich platform are you trying to install on?")
            print("1: Windows")
            print("2: Mac")
            print("3: iOS")
            print("4: Android")
            
            platform_choice = input("\nEnter your choice (1-4): ")
            
            print("\nHere are the specific installation steps for your platform:")
            self.simulate_typing()
            
            if platform_choice == "1":
                print("1. Download the installer from our website")
                print("2. Right-click the installer and select 'Run as administrator'")
                print("3. Follow the on-screen instructions")
                print("4. Restart your computer after installation")
            elif platform_choice == "2":
                print("1. Download the DMG file from our website")
                print("2. Open the DMG file")
                print("3. Drag the application to your Applications folder")
                print("4. Right-click the app and select 'Open' for first-time use")
            else:
                print("1. Open the App Store/Google Play Store")
                print("2. Search for our application")
                print("3. Tap 'Install' and follow the prompts")
                
        elif sub_choice == "4":  # Error messages
            print(self.tech_solutions["error"])
            print("\nCan you provide the error code or message you're seeing?")
            error_message = input("\nError code/message: ")
            
            print(f"\nI've searched our database for error '{error_message}'")
            self.simulate_typing()
            
            print("This error typically occurs when there's a connection issue with our servers.")
            print("Would you like to try some troubleshooting steps or file a detailed report?")
            print("1: Try troubleshooting steps")
            print("2: File a detailed report")
            
            error_choice = input("\nEnter your choice (1-2): ")
            
            if error_choice == "1":
                print("\nPlease try the following:")
                print("1. Check your internet connection")
                print("2. Disable any VPN or proxy services")
                print("3. Clear your application cache")
                print("4. Restart the application")
            else:
                print("\nA support ticket has been created.")
                print(f"Ticket number: #{random.randint(100000, 999999)}")
                print("A technical specialist will contact you within 24 hours.")
    
    def handle_product_info(self, sub_choice):
        """Handle product information requests"""
        if sub_choice == "1":  # Features overview
            print("\nOur product includes the following key features:")
            print("1. Cloud synchronization across all your devices")
            print("2. Advanced security with two-factor authentication")
            print("3. Collaborative editing in real-time")
            print("4. Automated backup and version history")
            print("5. AI-powered suggestions and insights")
            
            print("\nWhich feature would you like to learn more about?")
            feature_choice = input("\nEnter your choice (1-5): ")
            
            feature_details = {
                "1": "Our cloud sync technology ensures your data is always up-to-date across all your devices, with changes reflected in real-time.",
                "2": "We use industry-standard encryption and offer multiple two-factor authentication options including SMS, authenticator apps, and hardware keys.",
                "3": "Multiple users can edit the same document simultaneously, with changes visible instantly and conflict resolution built-in.",
                "4": "We automatically create backups every 15 minutes and maintain a 30-day version history for all your files.",
                "5": "Our AI analyzes your usage patterns to provide helpful suggestions and insights, helping you work more efficiently."
            }
            
            if feature_choice in feature_details:
                print(f"\n{feature_details[feature_choice]}")
            
        elif sub_choice == "2":  # Pricing information
            print("\nWe offer the following pricing plans:")
            print("Basic Plan: $9.99/month - Includes core features for individual users")
            print("Premium Plan: $19.99/month - Includes advanced features and priority support")
            print("Business Plan: $49.99/month - Includes team collaboration and admin controls")
            print("Enterprise: Custom pricing - Includes custom integrations and dedicated support")
            
            print("\nWould you like to see a detailed feature comparison?")
            print("1: Yes, show comparison")
            print("2: No, thanks")
            
            compare_choice = input("\nEnter your choice (1-2): ")
            
            if compare_choice == "1":
                print("\nFeature Comparison:")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print("Feature          | Basic | Premium | Business | Enterprise")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print("Storage          | 10GB  | 100GB   | 1TB      | Unlimited")
                print("Users            | 1     | 1       | Up to 10  | Unlimited")
                print("Support          | Email | Priority| Priority  | Dedicated")
                print("API Access       | No    | Yes     | Yes       | Custom")
                print("Custom Branding  | No    | No      | Yes       | Yes")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
        elif sub_choice == "3":  # Compatibility questions
            print("\nWhat system or device are you checking compatibility for?")
            print("1: Windows")
            print("2: Mac")
            print("3: iOS")
            print("4: Android")
            print("5: Web browsers")
            print("6: Other")
            
            system_choice = input("\nEnter your choice (1-6): ")
            
            compatibility_info = {
                "1": "Windows: Compatible with Windows 10 and 11. Requires 4GB RAM and 500MB disk space.",
                "2": "Mac: Compatible with macOS 10.14 (Mojave) and newer. Requires 4GB RAM and 500MB disk space.",
                "3": "iOS: Compatible with iOS 13 and newer. Optimized for both iPhone and iPad.",
                "4": "Android: Compatible with Android 8.0 and newer. Tablet support available.",
                "5": "Web: Compatible with Chrome, Firefox, Safari, and Edge (latest versions).",
                "6": "For other systems, please specify and we'll check compatibility for you."
            }
            
            if system_choice in compatibility_info:
                print(f"\n{compatibility_info[system_choice]}")
                
            if system_choice == "6":
                other_system = input("\nPlease specify your system: ")
                print(f"\nI'll need to check compatibility for {other_system}. Let me create a ticket for our product team.")
                print(f"Ticket #{random.randint(10000, 99999)} has been created. We'll email you with compatibility information within 48 hours.")
    
    def handle_complaint(self, sub_choice):
        """Handle customer complaints"""
        if sub_choice == "1":  # Service quality issue
            print("\nI'm sorry to hear you're experiencing service quality issues.")
            print("Please rate the severity of the issue:")
            print("1: Minor inconvenience")
            print("2: Moderate issue")
            print("3: Major problem")
            print("4: Service completely unusable")
            
            severity = input("\nEnter your choice (1-4): ")
            
            print("\nPlease provide more details about the service quality issue:")
            details = input("Details: ")
            
            print("\nThank you for bringing this to our attention. Your feedback is important to us.")
            print(f"Complaint reference #: {random.randint(100000, 999999)}")
            
            if severity in ["3", "4"]:
                print("Due to the severity of this issue, a customer service manager will contact you within 24 hours.")
            else:
                print("We'll review your feedback and work on improving our service.")
                
        elif sub_choice == "2":  # Product defect
            print("\nI'm sorry to hear about the product defect.")
            print("Which product are you experiencing issues with?")
            product = input("Product name: ")
            
            print("\nHow long have you owned this product?")
            print("1: Less than 30 days")
            print("2: 1-6 months")
            print("3: 6-12 months")
            print("4: Over 1 year")
            
            ownership = input("\nEnter your choice (1-4): ")
            
            print("\nPlease describe the defect in detail:")
            defect_details = input("Defect details: ")
            
            print("\nWould you like to:")
            print("1: Request a repair")
            print("2: Request a replacement")
            print("3: Request a refund")
            
            request_type = input("\nEnter your choice (1-3): ")
            
            print(f"\nThank you. Your {['repair', 'replacement', 'refund'][int(request_type) - 1]} request has been submitted.")
            print(f"Reference #: {random.randint(100000, 999999)}")
            print("A product specialist will contact you within 48 hours to process your request.")
            
        elif sub_choice == "3":  # Staff behavior
            print("\nI'm sorry to hear you had a negative experience with our staff.")
            print("When did this incident occur?")
            date = input("Date (YYYY-MM-DD): ")
            
            print("\nIf you know, please provide the name of the staff member:")
            staff_name = input("Staff name (or leave blank if unknown): ")
            
            print("\nPlease describe what happened:")
            incident = input("Incident details: ")
            
            print("\nThank you for bringing this to our attention. We take these matters very seriously.")
            print(f"Complaint reference #: {random.randint(100000, 999999)}")
            print("Our customer relations manager will contact you within 24 hours to address this issue.")
    
    def transfer_to_agent(self):
        """Transfer the user to a human agent"""
        print("\nI understand you'd like to speak with a human agent.")
        print("Please select the department you need assistance with:")
        print("1: General customer service")
        print("2: Technical support")
        print("3: Billing department")
        print("4: Sales team")
        
        department = input("\nEnter your choice (1-4): ")
        
        print(f"\nThank you. I'll connect you with a {['customer service', 'technical support', 'billing', 'sales'][int(department) - 1]} representative.")
        print("Please provide a brief description of your issue:")
        issue = input("Issue description: ")
        
        print("\nThank you. Please hold while I connect you with the next available agent...")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        
        print("\nIn a real implementation, you would now be connected with a live agent.")
        print("Your reference number is: #" + str(random.randint(1000, 9999)))
        print("Estimated wait time: 5-10 minutes")
        
        # Return to main menu
        input("\nPress Enter to return to the main menu...")
    
    def simulate_typing(self):
        """Simulate typing/processing time"""
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print()
    
    def end_conversation(self):
        """End the conversation with the user"""
        print(f"\nThank you for chatting with us today, {self.user_name}!")
        print("Is there anything else you'd like assistance with before you go?")
        print("1: Yes, I have another question")
        print("2: No, I'm all set")
        
        final_choice = input("\nEnter your choice (1-2): ")
        
        if final_choice == "1":
            print("Great! Let's go back to the main menu.")
            self.start()
        else:
            print(f"\nThank you for using our customer support service, {self.user_name}.")
            print("Have a great day!")
            print("=" * 50)


def main():
    chatbot = CustomerSupportChatbot()
    chatbot.start()


if __name__ == "__main__":
    main()