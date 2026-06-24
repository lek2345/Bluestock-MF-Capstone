import requests
import pandas as pd

scheme_codes = [
    125497,  # HDFC Top 100 Direct
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)
        data = response.json()

        nav_data = pd.DataFrame(data["data"])

        nav_data.to_csv(
            f"../data/raw/nav_{code}.csv",
            index=False
        )

        print(f"Saved NAV data for {code}")

    except Exception as e:
        print(f"Error fetching {code}: {e}")