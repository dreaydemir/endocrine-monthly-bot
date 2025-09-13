import yagmail

# Buraya kendi bilgilerini yaz
EMAIL_ADDRESS = "ensaraydemir@gmail.com"
EMAIL_APP_PASSWORD = "kviy swzi juva slmy"   # Google App Password (16 haneli)
EMAIL_TO = "ensaraydemir@gmail.com"

try:
    yag = yagmail.SMTP(user=EMAIL_ADDRESS, password=EMAIL_APP_PASSWORD)
    yag.send(to=EMAIL_TO, subject="Test Mail", contents="✅ Bu bir deneme mesajıdır. Eğer bunu aldıysan ayarlar doğru çalışıyor.")
    print("✅ Mail başarıyla gönderildi.")
except Exception as e:
    print("❌ Mail gönderilemedi:", e)
