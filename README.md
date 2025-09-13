## 📘 README.md (önerilen içerik)

```markdown
# Endocrine Monthly Bot

🔬 **Endocrine Monthly Bot**, endokrinoloji dergilerinde yayımlanan en güncel makaleleri **Crossref API** üzerinden tarar, 
kategorize eder (tiroid, paratiroid, kemik/osteoporoz, diyabet/obezite, adrenal, hipofiz, reprodüktif, case report, yapay zeka, vb.) 
ve sonuçları **Excel (xlsx)** dosyası halinde aylık olarak e-posta ile gönderir.  

## 🚀 Özellikler
- Son 30 gün içerisindeki tüm makaleleri toplar
- Kategorilere ayırır
- Dergi quartile bilgisini ekler
- Open Access durumunu kontrol eder (Unpaywall API)
- Excel çıktısı oluşturur (`September_2025.xlsx` gibi)
- E-postaya otomatik ek yapar (bir veya birden fazla alıcıya)

## 📂 Proje Yapısı
```

endocrine-monthly-bot/
│── main.py              # Ana giriş dosyası
│── fetchers.py          # Crossref ve Unpaywall API çağrıları
│── categorize.py        # Makale kategorileme kuralları
│── emailer.py           # E-posta gönderim sistemi
│── requirements.txt     # Python bağımlılıkları
│── journals.csv         # Takip edilecek dergiler
│── .github/workflows/   # GitHub Actions ayarları

````

## 🔧 Kurulum (Lokal Kullanım)
1. Depoyu klonla:
   ```bash
   git clone https://github.com/dreaydemir/endocrine-monthly-bot.git
   cd endocrine-monthly-bot
````

2. Sanal ortam kur ve bağımlılıkları yükle:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows için: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. `.env` dosyası oluştur:

   ```env
   EMAIL_ADDRESS=your_gmail@gmail.com
   EMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
   EMAIL_TO=recipient1@gmail.com,recipient2@gmail.com
   UNPAYWALL_EMAIL=your_gmail@gmail.com
   LOOKBACK_DAYS=30
   MAX_RESULTS_PER_JOURNAL=250
   ```

4. Çalıştır:

   ```bash
   python main.py
   ```

## 🤖 GitHub Actions (Otomatik Çalıştırma)

1. Repo → **Settings → Secrets and variables → Actions**

2. Şu değerleri ekle:

   * `EMAIL_ADDRESS`
   * `EMAIL_APP_PASSWORD`
   * `EMAIL_TO`
   * `UNPAYWALL_EMAIL`

3. Workflow dosyası: `.github/workflows/monthly.yml`
   → Bot her ayın 1’inde otomatik çalışır ve raporu e-postayla gönderir.

## 📜 Lisans

Bu proje MIT lisansı ile sunulmaktadır. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

````

---

