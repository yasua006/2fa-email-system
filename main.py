import sys
import smtplib

from pyotp import TOTP
from pyotp import random_base32
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

from config import *


def ask(current_totp: str) -> None:
    result = input(
        f"Please enter the authentication code.\nThe authentication code has been sent to email: {to}\n")

    if result == current_totp:
        print("Success!")
        sys.exit(0)
    else:
        print("Invalid authentication code!")
        sys.exit(0)

def main() -> None:
    totp: TOTP = TOTP(random_base32())
    emailed_code: str = totp.now()

    msg: MIMEText = MIMEText("Your code is: " + totp.now())
    # print(msg)

    if sender_email == to:
        print("Receiver can't be sender!")
        sys.exit(0)

    msg['Subject'] = "2FA Verification"
    msg['From'] = sender_email
    msg['To'] = to

    s: SMTP_SSL = smtplib.SMTP_SSL("smtp.gmail.com")
    s.login(sender_email, hover_unfriendly_password)
    s.sendmail(
        from_addr=sender_email,
        to_addrs=to,
        msg=msg.as_string())
    s.quit()

    ask(emailed_code)

if __name__ == '__main__':
    main()