import pandas as pd
from pathlib import Path
from main import df_to_pdf

# Test için sahte veriler
data = [
    {
        "category": "kemik/osteoporoz",
        "title": "Effects of denosumab treatment on bone mineral density in postmenopausal women",
        "journal": "Osteoporosis International",
        "quartile": "Q1",
        "url": "https://doi.org/10.1000/test1",
        "doi": "10.1000/test1",
        "is_open_access": True,
        "oa_status": "gold"
    },
    {
        "category": "diyabet/obezite",
        "title": "Metformin and GLP-1 analogues in the treatment of type 2 diabetes mellitus",
        "journal": "Diabetes Care",
        "quartile": "Q1",
        "url": "https://doi.org/10.1000/test2",
        "doi": "10.1000/test2",
        "is_open_access": False,
        "oa_status": "closed"
    },
    {
        "category": "adrenal",
        "title": "Cushing’s syndrome due to adrenal hyperplasia: a case report",
        "journal": "Endocrine Journal",
        "quartile": "Q2",
        "url": "https://doi.org/10.1000/test3",
        "doi": "10.1000/test3",
        "is_open_access": True,
        "oa_status": "bronze"
    }
]

# DataFrame oluştur
df = pd.DataFrame(data)

# Çıktı klasörü
outdir = Path("output")
outdir.mkdir(exist_ok=True)

# PDF oluştur
pdf_path = outdir / "test_output.pdf"
df_to_pdf(df, str(pdf_path))

print("✅ Test PDF oluşturuldu:", pdf_path)
