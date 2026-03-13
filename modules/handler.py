import sys

from config import sender_email, to


def handle_user_result(result, current_totp) -> None:
    if result == current_totp:
        print("Success!")
        sys.exit(0)
    else:
        print("Invalid authentication code!")
        sys.exit(0)

def handle_equal_emails_config():
    if sender_email == to:
        print("Receiver can't be sender!")
        sys.exit(0)