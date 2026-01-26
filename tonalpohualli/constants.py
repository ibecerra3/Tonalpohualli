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
# Veintena ruling gods (Xiuhpohualli)
# ---------------------------
VEINTENA_RULING_GODS = {
    "Atlcahualo": ["Tlaloc", "Chalchiuhtlicue"],
    "Tlacaxipehualiztli": ["Xipe Totec"],
    "Tozoztontli": ["Coatlicue", "Tlaloc"],
    "Huey Tozoztli": ["Cinteotl", "Chicomecoatl"],
    "Toxcatl": ["Tezcatlipoca", "Huitzilopochtli"],
    "Etzalcualiztli": ["Tlaloc"],
    "Tecuilhuitontli": ["Huixtocihuatl"],
    "Huey Tecuilhuitl": ["Xilonen"],
    "Tlaxochimaco (Miccailhuitontli)": ["Huitzilopochtli"],
    "Xocotlhuetzi": ["Xiuhtecuhtli"],
    "Ochpaniztli": ["Toci"],
    "Teotleco": ["Todos los dioses"],
    "Tepeilhuitl": ["Tlaloc", "Dioses de los cerros"],
    "Quecholli": ["Mixcoatl"],
    "Panquetzaliztli": ["Huitzilopochtli"],
    "Atemoztli": ["Tlaloc"],
    "Tititl": ["Cihuacoatl"],
    "Izcalli": ["Xiuhtecuhtli"],
}

# ---------------------------
# Year Bearers (Portadores del Año) + Annual Regent Gods
# ---------------------------
# 1 Tochtli, 2 Acatl, 3 Tecpatl, 4 Calli, 5 Tochtli, etc.
YEAR_BEARER_SIGNS = ["Tochtli", "Acatl", "Tecpatl", "Calli"]

# Anchor year-bearer for the ANCHOR_DATE's xiuhpohualli year (year index 0).
ANCHOR_YEAR_BEARER_NUMBER = 1
ANCHOR_YEAR_BEARER_SIGN = "Tochtli"

# Annual regent gods (7-god rotation).
# If your list/order differs, edit THIS list only.
YEAR_REGENT_GODS = [
    "Xiuhtecuhtli",
    "Tezcatlipoca",
    "Chalchiuhtlicue",
    "Centeotl",
    "Mictecacihuatl y Mictlantecuhtli",
    "Tlazolteotl",
    "Tlaloc",
]

# Anchor
ANCHOR_DATE = date(1506, 3, 13)
ANCHOR_NUMBER = 1
ANCHOR_SIGN_INDEX = DAY_SIGNS.index("Cipactli")
ANCHOR_LORD_INDEX = LORDS_OF_NIGHT.index("Xiuhtecuhtli")
