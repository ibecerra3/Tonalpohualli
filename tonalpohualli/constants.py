# tonalpohualli/constants.py

from datetime import date

ROMAN_NUMERALS = [
    "I", "II", "III", "IV", "V",
    "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII"
]

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
    "Coatl": "Chalchiuhtlicue",
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
# Regentes del Numeral (1–13)
# ---------------------------
REGENTE_DEL_NUMERAL = {
    1: "Xiuhtecuhtli",
    2: "Tlaltecuhtli",
    3: "Chalchihuitlicue",
    4: "Tonatiuh",
    5: "Tlazolteotl",
    6: "Mictecacihuatl y Mictlantecuhtli",
    7: "Centeotl",
    8: "Tlaloc",
    9: "Quetzalcoatl",
    10: "Tezcatlipoca",
    11: "Chalmecatecuhtli",
    12: "Tlahuizcalpantecuhtli",
    13: "Citlalicue",
}

# ---------------------------
# Year Bearers + Annual Regent Gods + 52-year cycle
# ---------------------------
YEAR_BEARER_SIGNS = ["Tochtli", "Acatl", "Tecpatl", "Calli"]

ANCHOR_YEAR_BEARER_NUMBER = 1
ANCHOR_YEAR_BEARER_SIGN = "Tochtli"

YEAR_REGENT_GODS = [
    "Xiuhtecuhtli",
    "Tezcatlipoca",
    "Chalchiuhtlicue",
    "Centeotl",
    "Mictecacihuatl y Mictlantecuhtli",
    "Tlazolteotl",
    "Tlaloc",
]

# ---------------------------
# Anchor
# ---------------------------
ANCHOR_DATE = date(1506, 3, 13)
