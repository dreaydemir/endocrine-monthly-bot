import pandas as pd

# Noktalı virgül ile ayrılmış CSV
df = pd.read_csv("scimago.csv", sep=";")

# Gerekli kolonlardan yeni tablo oluştur
out = pd.DataFrame({
    "journal_title": df["Title"],
    "quartile": df["SJR Quartile"],
    "open_access": df["Open Access"].str.strip().str.lower().replace({"yes": "yes", "no": "no"}),
    "open_access_diamond": df["Open Access Diamond"].str.strip().str.lower().replace({"yes": "yes", "no": "no"}),
    "base_url": ""  # elle dolduracaksın
})

# Kaydet
out.to_csv("journals.csv", index=False, encoding="utf-8")
print("✅ journals.csv oluşturuldu. Lütfen 'base_url' kolonunu doldurun.")
