"""
Descarga TODAS las reseñas (cualquier fecha, incluidas 'review bombs')
de Nekopara Vol.0 (AppID 333600) en inglés y las guarda en un .txt
Requiere: pip install requests tqdm
"""

import requests, time, urllib.parse, json
from tqdm import tqdm

APP_ID   = 333600
LANG     = "english"           
OUT_FILE = "nekopara_all_reviews.txt"
DELAY    = 0.6                 # espera entre peticiones (seguridad)

params_fixed = {
    "json":                 1,
    "filter":               "updated",   # recorre todo el histórico
    "language":             LANG,
    "review_type":          "all",
    "purchase_type":        "all",
    "num_per_page":         100,         # máximo permitido
    "filter_offtopic_activity": 0        # incluye off-topic
}

cursor   = "*"
total_dl = 0
pbar     = tqdm(desc="Descargando", unit=" reviews")

with open(OUT_FILE, "w", encoding="utf-8") as fout:
    while True:
        # querystring con cursor codificado
        params = params_fixed | {"cursor": cursor}
        url    = f"https://store.steampowered.com/appreviews/{APP_ID}"
        r      = requests.get(url, params=params, timeout=15)
        data   = r.json()
        reviews = data.get("reviews", [])

        if not reviews:               # <-- sin más reseñas: fin
            break

        for rev in reviews:
            txt = rev.get("review", "").replace("\n", " ").strip()
            if txt:
                fout.write(txt + "\n")
                total_dl += 1
                pbar.update(1)

        # preparación para la siguiente página
        cursor = data.get("cursor")
        time.sleep(DELAY)

pbar.close()
print(f"\nTotal de reseñas guardadas: {total_dl}")
print(f"Archivo generado: {OUT_FILE}")
