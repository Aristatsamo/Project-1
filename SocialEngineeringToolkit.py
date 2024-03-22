import random

class PhishingTool:
    def __init__(self, target_email):
        self.target_email = target_email

    def send_phishing_email(self):
        sender_name = "Your Friend"
        sender_email = "yourfriend@example.com"
        subject = "Important Message"

        # Craft phishing email
        phishing_email = f"""\
        Hi,

        I hope you're doing well. I came across something interesting and thought you might want to check it out.

        Please click on the link below:
        https://malicious.website/link?id={random.randint(1000, 9999)}

        Best regards,
        {sender_name}
        """

        # Send email (This is a simulated action)
        print(f"Sending phishing email to {self.target_email} from {sender_email} with subject '{subject}':")
        print(phishing_email)
        print("Email sent successfully!")

# Example usage
if __name__ == "__main__":
    target_email = "target@example.com"
    phishing_tool = PhishingTool(target_email)
    phishing_tool.send_phishing_email()
