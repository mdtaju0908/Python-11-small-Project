"""
Email Transfer - A simple email sending simulation system
"""

import re
from datetime import datetime


class EmailTransfer:
    """Email Transfer system for sending and managing emails."""

    def __init__(self):
        """Initialize email system."""
        self.inbox = []
        self.sent = []
        self.drafts = []

    def validate_email(self, email):
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def compose_email(self, sender, recipient, subject, body):
        """Compose a new email."""
        if not self.validate_email(sender):
            return False, "Invalid sender email format."
        if not self.validate_email(recipient):
            return False, "Invalid recipient email format."
        if not subject.strip():
            return False, "Subject cannot be empty."
        if not body.strip():
            return False, "Body cannot be empty."

        email = {
            "sender": sender,
            "recipient": recipient,
            "subject": subject,
            "body": body,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "read": False
        }
        return True, email

    def send_email(self, email):
        """Send an email."""
        self.sent.append(email)
        # Simulate receiving the email in inbox
        received_email = email.copy()
        received_email["read"] = False
        self.inbox.append(received_email)
        return True, "Email sent successfully!"

    def save_draft(self, email):
        """Save email as draft."""
        self.drafts.append(email)
        return True, "Email saved to drafts."

    def view_inbox(self):
        """View all emails in inbox."""
        if not self.inbox:
            return "Inbox is empty."
        result = []
        for i, email in enumerate(self.inbox):
            status = "📧" if not email["read"] else "📭"
            result.append(f"{i + 1}. {status} From: {email['sender']} | "
                          f"Subject: {email['subject']} | {email['timestamp']}")
        return "\n".join(result)

    def view_sent(self):
        """View all sent emails."""
        if not self.sent:
            return "No sent emails."
        result = []
        for i, email in enumerate(self.sent):
            result.append(f"{i + 1}. To: {email['recipient']} | "
                          f"Subject: {email['subject']} | {email['timestamp']}")
        return "\n".join(result)

    def view_drafts(self):
        """View all draft emails."""
        if not self.drafts:
            return "No drafts."
        result = []
        for i, email in enumerate(self.drafts):
            result.append(f"{i + 1}. To: {email['recipient']} | "
                          f"Subject: {email['subject']}")
        return "\n".join(result)

    def read_email(self, index, folder="inbox"):
        """Read a specific email."""
        if folder == "inbox":
            emails = self.inbox
        elif folder == "sent":
            emails = self.sent
        else:
            emails = self.drafts

        if 0 <= index < len(emails):
            email = emails[index]
            if folder == "inbox":
                email["read"] = True
            return f"""
{'=' * 50}
From: {email['sender']}
To: {email['recipient']}
Subject: {email['subject']}
Date: {email['timestamp']}
{'=' * 50}

{email['body']}

{'=' * 50}
"""
        return "Email not found."

    def delete_email(self, index, folder="inbox"):
        """Delete an email from specified folder."""
        if folder == "inbox":
            emails = self.inbox
        elif folder == "sent":
            emails = self.sent
        else:
            emails = self.drafts

        if 0 <= index < len(emails):
            emails.pop(index)
            return True, "Email deleted successfully."
        return False, "Email not found."


def main():
    """Main function to run the email system."""
    email_system = EmailTransfer()

    print("=" * 50)
    print("       Welcome to Email Transfer System")
    print("=" * 50)

    user_email = input("Enter your email address: ")
    if not email_system.validate_email(user_email):
        print("Invalid email format. Using default: user@example.com")
        user_email = "user@example.com"

    while True:
        print("\n" + "-" * 50)
        print("1. Compose Email")
        print("2. View Inbox")
        print("3. View Sent")
        print("4. View Drafts")
        print("5. Read Email")
        print("6. Delete Email")
        print("7. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            recipient = input("Enter recipient email: ")
            subject = input("Enter subject: ")
            print("Enter email body (press Enter twice to finish):")
            body_lines = []
            while True:
                line = input()
                if line == "":
                    break
                body_lines.append(line)
            body = "\n".join(body_lines)

            success, result = email_system.compose_email(
                user_email, recipient, subject, body
            )
            if success:
                action = input("Send (s) or Save as draft (d)? ")
                if action.lower() == "s":
                    _, msg = email_system.send_email(result)
                    print(msg)
                elif action.lower() == "d":
                    _, msg = email_system.save_draft(result)
                    print(msg)
            else:
                print(result)

        elif choice == "2":
            print("\n📬 Inbox:")
            print(email_system.view_inbox())

        elif choice == "3":
            print("\n📤 Sent:")
            print(email_system.view_sent())

        elif choice == "4":
            print("\n📝 Drafts:")
            print(email_system.view_drafts())

        elif choice == "5":
            folder = input("Which folder? (inbox/sent/drafts): ").lower()
            try:
                index = int(input("Enter email number: ")) - 1
                print(email_system.read_email(index, folder))
            except ValueError:
                print("Invalid input.")

        elif choice == "6":
            folder = input("Which folder? (inbox/sent/drafts): ").lower()
            try:
                index = int(input("Enter email number to delete: ")) - 1
                success, msg = email_system.delete_email(index, folder)
                print(msg)
            except ValueError:
                print("Invalid input.")

        elif choice == "7":
            print("\nThank you for using Email Transfer System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
