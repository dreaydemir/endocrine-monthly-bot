import re
import os

DEBUG = os.getenv("DEBUG_CATEGORIZE", "0") == "1"

CATEGORIES = {
    "tiroid": [
        "thyroid", "hyperthyroidism", "hypothyroidism", "graves", "hashimoto", "papillary carcinoma",
    ],
    "paratiroid": [
        "parathyroid", "hyperparathyroidism", "hypoparathyroidism", "pth",
    ],
    "kemik/osteoporoz": [
        "osteoporosis", "osteopenia", "bone mineral density", "bmd",
        "fragility fracture", "hip fracture", "vertebral fracture",
        "fracture risk", "denosumab", "bisphosphonate", "teriparatide"
    ],
    "yapay zeka": [
        "machine learning", "deep learning", "artificial intelligence", "ai model",
        "neural network", "transformer", "chatgpt"
    ],
    "diyabet/obezite": [
        "diabetes", "diabetic", "type 1 diabetes", "type 2 diabetes", "obesity", "obese",
        "insulin resistance", "hyperglycemia", "metformin", "glp-1", "liraglutide", "semaglutide"
    ],
    "adrenal": [
        "adrenal", "cushing", "pheochromocytoma", "aldosteronism", "incidentaloma", "hyperplasia",
    ],
    "reproduktif": [
        "polycystic ovary", "pco", "pcos", "infertility", "reproductive", "androgen", "estrogen",
    ],
    "hipofiz": [
        "pituitary", "acromegaly", "prolactinoma", "growth hormone", "gh deficiency",
    ],
    "case report": [
        "case report", "a case of", "case series"
    ]
}


def categorize(title: str) -> str:
    """
    Başlıkta anahtar kelime eşleşmesine göre kategori döndürür.
    Hiçbiri yoksa 'diğer' kategorisine atar.
    """
    if not title:
        return "diğer"

    t = title.lower()
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if re.search(r"\b" + re.escape(kw.lower()) + r"\b", t):
                if DEBUG:
                    print(f"[CAT] '{title[:60]}...' → {cat}")
                return cat

    if DEBUG:
        print(f"[CAT] '{title[:60]}...' → diğer")
    return "diğer"
