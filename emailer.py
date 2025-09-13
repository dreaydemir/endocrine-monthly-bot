import os
import yagmail

def send_email(subject: str, body: str, attachments=None):
    user = os.getenv("EMAIL_ADDRESS")
    app_pw = os.getenv("EMAIL_APP_PASSWORD")
    to_raw = os.getenv("EMAIL_TO", "")

    if not user or not app_pw:
        raise RuntimeError("EMAIL_ADDRESS ve EMAIL_APP_PASSWORD .env içinde tanımlı olmalı!")

    # Virgül ile ayrılmış adresleri listeye çevir
    recipients = [addr.strip() for addr in to_raw.split(",") if addr.strip()]

    yag = yagmail.SMTP(user=user, password=app_pw)
    yag.send(
        to=recipients,
        subject=subject,
        contents=body,
        attachments=attachments or []
    )
    print(f"✅ Mail gönderildi → {', '.join(recipients)}")
