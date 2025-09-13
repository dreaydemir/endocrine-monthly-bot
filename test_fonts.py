import os

# Kontrol edilecek font dosyaları
candidates = {
    "Segoe UI": "C:\\Windows\\Fonts\\segoeui.ttf",
    "Calibri": "C:\\Windows\\Fonts\\calibri.ttf",
    "Times New Roman": "C:\\Windows\\Fonts\\times.ttf",
    "Verdana": "C:\\Windows\\Fonts\\verdana.ttf",
    "Arial Unicode MS": "C:\\Windows\\Fonts\\ARIALUNI.TTF",
}

print("📌 Windows Font Kontrolü:\n")
for name, path in candidates.items():
    if os.path.exists(path):
        print(f"✅ {name} bulundu → {path}")
    else:
        print(f"❌ {name} bulunamadı ({path})")

print("\nBitti ✅")
