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
# NEW: Regente del Numeral (1–13)
# ---------------------------
REGENTES_DEL_NUMERAL = [
    "Xiuhtecuhtli",                         # 1  Ce
    "Tlaltecuhtli",                         # 2  Ome
    "Chalchihuitlicue",                     # 3  Yei
    "Tonatiuh",                             # 4  Nahui
    "Tlazolteotl",                          # 5  Mahcuilli
    "Mictecacihuatl y Mictlantecuhtli",     # 6  Chicuacen
    "Centeotl",                             # 7  Chicome
    "Tlaloc",                               # 8  Chicuei
    "Quetzalcoatl",                         # 9  Chicunahui
    "Tezcatlipoca",                         # 10 Mahtlactli
    "Chalmecatecuhtli",                     # 11 Mahtlactli-once
    "Tlahuizcalpantecuhtli",                # 12 Mahtlactli-omome
    "Citlalicue",                           # 13 Mahtlactli-omei
]

# ---------------------------
# NEW: Volátil (1–13)
# ---------------------------
VOLATIL = [
    "Huiztilin (humming-bird)",                  # 1
    "Quetzalhuiztilin (green humming-bird)",     # 2
    "Huactli (hawk)",                            # 3
    "Zolin (quail)",                             # 4
    "Cuauhtli (eagle)",                          # 5
    "Chicuatli (screech owl)",                   # 6
    "Papalotl (butterfly)",                      # 7
    "Tlotli (hawk eagle)",                       # 8
    "Huexolotl (turkey)",                        # 9
    "Tecolotl (owl)",                            # 10
    "Alotl (macaw)",                             # 11
    "Quetzal (quetzal)",                         # 12
    "Toznene (parrot)",                          # 13
]

# Anchor
ANCHOR_DATE = date(1506, 3, 13)
ANCHOR_NUMBER = 1
ANCHOR_SIGN_INDEX = DAY_SIGNS.index("Cipactli")
ANCHOR_LORD_INDEX = LORDS_OF_NIGHT.index("Xiuhtecuhtli")
