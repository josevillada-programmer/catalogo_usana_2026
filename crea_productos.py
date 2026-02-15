import json

datos_usana = {
    "101": {"desc": "CellSentials (CorMin y Vita-AO)", "pc": 32, "pref": 1150.0, "pub": 1380.0},
    "122": {"desc": "BiOmega", "pc": 12, "pref": 530.0, "pub": 636.0},
    "131": {"desc": "Procosa", "pc": 20, "pref": 860.0, "pub": 1032.0},
    "163": {"desc": "Paquete Vida Sana", "pc": 57, "pref": 2232.0, "pub": 2678.0},
    "110": {"desc": "Proflavanol C100", "pc": 22, "pref": 920.0, "pub": 1104.0},
    "123": {"desc": "MagneCal D", "pc": 9, "pref": 415.0, "pub": 498.0},
    "100": {"desc": "TotalPak (56 sobres)", "pc": 50, "pref": 2020.0, "pub": 2424.0},
    "108": {"desc": "USANA HPS", "pc": 16, "pref": 750.0, "pub": 900.0},
    "120": {"desc": "USANA Probiotic (14 sobres)", "pc": 13, "pref": 545.0, "pub": 654.0},
    "135": {"desc": "CoQuinone 30", "pc": 18, "pref": 850.0, "pub": 1020.0},
    "210": {"desc": "Dutch Chocolate (Bolsa 9 raciones)", "pc": 12, "pref": 585.0, "pub": 702.0}
}

with open('productos.json', 'w', encoding='utf-8') as f:
    json.dump(datos_usana, f, indent=4, ensure_ascii=False)

print("✅ Archivo productos.json creado con éxito.")