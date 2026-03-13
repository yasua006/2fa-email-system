import sys
import smtplib

from pyotp import TOTP
from pyotp import random_base32
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

from config import *


def main() -> None:
    totp: TOTP = TOTP(random_base32())

    msg: MIMEText = MIMEText(totp.now())

    if sender_email == to:
        print("Receiver can't be sender!")
        sys.exit(0)

    msg['Subject'] = "Kode test - 2FA"
    msg['From'] = sender_email
    msg['To'] = to

    s: SMTP_SSL = smtplib.SMTP_SSL("smtp.gmail.com")
    s.login(sender_email, hover_unfriendly_password)
    s.sendmail(
        from_addr=sender_email,
        to_addrs=to,
        msg=msg.as_string())
    s.quit()

if __name__ == '__main__':
    main()