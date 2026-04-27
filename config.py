from os import getenv

sender_email: str | None = getenv("sender_email")
to: str | None = getenv("to")
password: str | None = getenv("app_password")
hover_unfriendly_password: str | None = password
