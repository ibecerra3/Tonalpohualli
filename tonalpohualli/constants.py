# tonalpohualli/constants.py

from datetime import date

DAY_SIGNS = [
    "Cipactli", "Ehecatl", "Calli", "Cuetzpalin", "Coatl",
    "Miquiztli", "Mazatl", "Tochtli", "Atl", "Itzcuintli",
    "Ozomahtli", "Malinalli", "Acatl", "Ocelotl", "Cuauhtli",
    "Cozcacuauhtli", "Ollin", "Tecpatl", "Quiahuitl", "Xochitl"
]

LORDS_OF_NIGHT = [
    "Xiuhtecuhtli",
    "Itztli",
    "Piltzintecuhtli",
    "Centeotl",
    "Mictecacihuatl y Mictlantecuhtli",
    "Chalchiuhtlicue",
    "Tlazolteotl",
    "Tepeyollotl",
    "Tlaloc"
]

DAY_GODS = {
    "Cipactli": "Tonacacihuatl y Tonacatecuhtli",
    "Ehecatl": "Quetzalcoatl",
    "Calli": "Tepeyollotl",
    "Cuetzpalin": "Huehuecoyotl",
    "Coatl": "Chalchiuhtli",
    "Miquiztli": "Tecciztecatl",
    "Mazatl": "Tlaloc",
    "Tochtli": "Mayahuel",
    "Atl": "Xiuhtecuhtli",
    "Itzcuintli": "Mictecacihuatl y Mictlantecuhtli",
    "Ozomahtli": "Xochipili",
    "Malinalli": "Patecatl",
    "Acatl": "Tezcatlipoca",
    "Ocelotl": "Tlazolteotl",
    "Cuauhtli": "Xipe Totec",
    "Cozcacuauhtli": "Itzpapalotl",
    "Ollin": "Xolotl",
    "Tecpatl": "Chalchihuihtotolin",
    "Quiahuitl": "Tonatiuh",
    "Xochitl": "Xochiquetzal"
}

ROMAN_NUMERALS = ["I", "II", "III", "IV", "V", "VI"]

TRECENA_RULING_GODS = {
    "Cipactli": ["Tonacatecuhtli y Tonacacihuatl"],
    "Ocelotl": ["Quetzalcoatl"],
    "Mazatl": ["Tepeyollotl", "Quetzalcoatl", "Tlazolteotl"],
    "Xochitl": ["Huehuecoyotl", "Ixnextli"],
    "Acatl": ["Chalchihuitlicue", "Tlazolteotl"],
    "Miquiztli": ["Tonatiuh", "Tecciztecatl"],
    "Quiahuitl": ["Tlaloc", "Chicomecoatl"],
    "Malinalli": ["Mayahuel", "Xochipilli", "Cinteotl"],
    "Coatl": ["Xiuhtecuhtli", "Tlahuizcalpantecuhtli"],
    "Tecpatl": ["Mictecacihuatl y Mictlantecuhtli", "Tonatiuh"],
    "Ozomahtli": ["Patecatl"],
    "Cuetzpalin": ["Itzlacoliuhqui"],
    "Ollin": ["Tlazolteotl"],
    "Itzcuintli": ["Xipe Totec"],
    "Calli": ["Itzpapalotl"],
    "Cozcacuauhtli": ["Xolotl", "Tlalchitonatiuh"],
    "Atl": ["Chalchihuihtotolin"],
    "Ehecatl": ["Chantico"],
    "Cuauhtli": ["Xochiquetzal"],
    "Tochtli": ["Xiuhtecuhtli", "Itztapaltotec"]
}

# ---------------------------
# Veintena ruling gods (Xiuhpohualli) — placeholder table
# Fill this later with your official list
# ---------------------------
VEINTENA_RULING_GODS = {
    # "NombreDeVeintena": ["Dios Principal"],
    # "OtraVeintena": ["Dios Principal", "Dios Secundario", "Otro Secundario"],
}

# Anchor
ANCHOR_DATE = date(1506, 3, 13)
ANCHOR_NUMBER = 1
ANCHOR_SIGN_INDEX = DAY_SIGNS.index("Cipactli")
ANCHOR_LORD_INDEX = LORDS_OF_NIGHT.index("Xiuhtecuhtli")
