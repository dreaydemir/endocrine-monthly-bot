import requests
from datetime import datetime, timedelta

# Crossref API: Belirli bir dergi için son X günün makalelerini getir
def crossref_recent_by_journal(journal_title: str, days: int = 30, max_results: int = 100):
    url = "https://api.crossref.org/works"
    from_date = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%d")

    params = {
        "filter": f"from-pub-date:{from_date},container-title:{journal_title}",
        "sort": "published",
        "order": "desc",
        "rows": max_results
    }

    try:
        r = requests.get(url, params=params, timeout=20)
        r.raise_for_status()
        data = r.json()
        return data.get("message", {}).get("items", [])
    except Exception as e:
        print(f"⚠️ Crossref API hatası ({journal_title}):", e)
        return []

# Unpaywall API: DOI üzerinden OA durumunu kontrol et
def unpaywall_lookup(doi: str, email: str):
    if not doi:
        return False, "unknown"
    try:
        url = f"https://api.unpaywall.org/v2/{doi}?email={email}"
        r = requests.get(url, timeout=15)
        if r.status_code != 200:
            return False, "unknown"
        data = r.json()
        is_open = data.get("is_oa", False)
        oa_status = data.get("oa_status", "unknown")
        return is_open, oa_status
    except Exception as e:
        print(f"⚠️ Unpaywall hatası ({doi}):", e)
        return False, "error"
