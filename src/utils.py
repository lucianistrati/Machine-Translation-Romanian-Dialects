# https://ro.wikipedia.org/wiki/Graiul_cri%C8%99ean

crisanean_fonetical_rules = {"ine": "ne",
                             "e": "ă",
                             "ea": "a",
                             "i": "â",
                             "g": "j",
                             "âi": "ii",
                             "sl": "scl",
                             "nu": "anu",
                             "n": "r"}

crisanean_fonetical_examples = {
    "câine": "câne",
    "se rupe": "să rupe",
    "orășean": "orășan",
    "țin": "țân",
    "zic": "zâc",
    "ger": "jer",
    "întâi": "întii",
    "slab": "sclab",
    "numără": "anumără",
    "lună": "lură",
}

crisanean_gramatical_rules = {"ui": "i",
                              " sunt ": " îs ",
                              " este ": " îi ",
                              " e ": " îi ",
                              " a ": " o ",
                              " au ": " or ",
                              " să ": " și ",
                              " mă ": " m-am ",
                              " ar fi ": " o vu(t) ",
                              " al ": " a ",
                              " ai ": " a ",
                              " ale ": " a "
                              }

crisanean_gramatical_examples = {
    "omului": "omuli",
    "ale tale": "a tale",
    "ai tăi": "a tăi",
    "al tău": "a tău",
    "au făcut": "or făcut",
    "a făcut": "o făcut",
    "să merg": "și merg",
    "mă dusesem": "m-am fo dusă",
    "ar fi cântat": "o vu(t) hori",
    " Ai făcut foc? ": " 	Făcut-ai foc? ",  # auxiliarul după verbul cu sens lexical
    " Mă voi duce. ": " Duce-m-oi. "  # auxiliarul după verbul cu sens lexical
}

crisanean_lexical_examples = {" perdea ": " firhang ",  # din germana de la verhangen
                              " a gusta ": " a cuștuli ",  # maghiara
                              " a plânge ": "  	a cânta ",
                              " nas ": " nari ",
                              " mergi! ": " vă! ",
                              " du-te! ": " vă! "}

# https://ro.wikipedia.org/wiki/Graiul_ardelenesc

ardelean_fonetical_examples = {" dormi ": " durmi ",
                               " adormi ": " adurmi "}

ardelean_fonetical_rules = {"ea": "e",
                            "oa": "o",
                            "o": "u",
                            "ane": "ine"}

# https://ro.wikipedia.org/wiki/Graiul_b%C4%83n%C4%83%C8%9Bean

banatean_lexical_varieties_examples = {
    "avlie": "curte",
    "covăsât": "iaurt",
    "credenț": "dulap",
    "dereș": "canapea",
    "firang": "perdea",
    "hârț": "șoarece",
    "măsai": "față de masă",
    "peșchir": "prosop",
    "piglais": "fier de călcat",
    "spoiert": "sobă",
    "strimf": "ciorap",
    "tulipan": "lalea",
    "uiagă": "sticlă"}

# https://ro.wikipedia.org/wiki/Graiul_moldovenesc

moldovean_lexical_varieties_examples = {"pătlăgică": "roșie",
                                        "harbuz": "pepene",
                                        "zămos/dzămos": "pepene galben",
                                        "bostan": "dovleac",
                                        "chiperi": "ardei",
                                        "omăt": "zăpadă",
                                        "barabulă/cartof": "cartof"}

# https://ro.wikipedia.org/wiki/Graiul_maramure%C8%99ean  TODO -> should read this

# https://ro.wikipedia.org/wiki/Graiul_muntenesc

muntean_fonetical_examples = {"ușă": "ușe",
                              "lojă": "loje",
                              "deștept ": "dăștept",
                              " din ": " dân ",
                              "fetele": "fetili",
                              "caprele": "caprili"}

muntean_fonetical_rules = {"ă ": "e ",
                           "e": ["ă", "i"],
                           "i": "â"}

muntean_gramatical_examples = {" n-am decât două mere ": " am decât două mere ",
                               " nu mă mai duc ": " nu mai mă duc ",
                               " mănâncă pâine": " mănâncă la pâine ",
                               " omul care vine ": " omul de vine ",
                               " floarea de pe masă": " floarea după/dupe masă ",
                               " grinda este așezată aici": " grinda vine așezată aici ",
                               " începe să crească": " 	vine și/de crește ",
                               " era să cad": " am vrut să cad ",
                               " ei/ele au venit ": " ei/ele a venitără ",
                               " ei/ele vor bea ": " ei/ele va bea ",
                               " ei/ele beau ": " ei/ele bea "}

muntean_gramatical_rules = {"au": "a", "de pe": ["după", "dupe"], " care ": " de "}

muntean_lexical_examples = {"mire": "ginere",
                            "ardei iute": "ciușcă",
                            "prosop": "peșchir",
                            "adăpost pentru vite": "perdea",
                            "ciur": "dârmon"}

# https://ro.wikipedia.org/wiki/Graiul_oltenesc

oltenesc_fonetical_examples = {"strachină": "straichină",
                               "răchită": "răichită",
                               "ureche": "ureiche",
                               "ochi": "oichi",
                               "păduche": "păduiche",
                               "hrean": "hirean",
                               "școală": "ișcoală",
                               "zice": "zâce",
                               "țelină": "țălină",
                               "măsea": "măsa"}

oltenesc_fonetical_rules = {"a": "ai",
                            "ă": "ăi",
                            "e": ["ei", "ă"],
                            " o": " oi",
                            "hr": "hir",
                            " ș": " iș",
                            "i": "â",
                            "ea": "a"}

oltenesc_gramatical_examples = {"am cântat": "cântai",
                                "aici": ["ici", "aici", "aci", "acia"],
                                "nu cântați!": "nu cântareți!"}

oltenesc_lexical_examples = {" șold ": " ar m",
                             " a strănuta ": " a străfiga ",
                             " 	picior de pasăre": " cotoi "}

# wikipedia above
# colegiu.info below

moldavean_rules = {"pi": "chi", "fe": "fi", "ci": "și"}
banatean_rules = {"de": "ge", "te": "ce"}
ardelean_rules = {"de": "ghe", "te": "che"}
muntean_rules = {"pe": "pă"}

# 'maramuresean': {'fonetical_rules': maramuresean_,
#      "fonetical_examples": ,
#      "gramatical_rules":
#     },


dialectical_rules = {'crisanean': {'fonetical_rules': crisanean_fonetical_rules,
                                   "fonetical_examples": crisanean_fonetical_examples,
                                   "gramatical_rules": crisanean_gramatical_rules
                                   },
                     'banatean': {"fonetical_rules": banatean_rules,
                                  "fonetical_examples": banatean_lexical_varieties_examples,
                                  "gramatical_rules": banatean_rules
                                  },
                     'ardelean': {'fonetical_rules': ardelean_fonetical_rules,
                                  "fonetical_examples": ardelean_fonetical_examples,
                                  "gramatical_rules": ardelean_rules
                                  },
                     'oltean': {'fonetical_rules': oltenesc_fonetical_rules,
                                "fonetical_examples": oltenesc_fonetical_examples,
                                "gramatical_rules": oltenesc_gramatical_examples,
                                "lexical_examples": oltenesc_lexical_examples
                                },
                     'moldovean': {'fonetical_rules': moldavean_rules,
                                   "fonetical_examples": moldovean_lexical_varieties_examples,
                                   "gramatical_rules": moldavean_rules
                                   },
                     'muntean': {'fonetical_rules': muntean_fonetical_rules,
                                 "fonetical_examples": muntean_fonetical_examples,
                                 "gramatical_rules": muntean_gramatical_rules,
                                 "rules": muntean_rules,
                                 "lexical_examples": muntean_lexical_examples,
                                 "gramatical_examples": muntean_gramatical_examples
                                 },
                     'maramuresean': {'fonetical_rules': None,
                                      "fonetical_examples": None,
                                      "gramatical_rules": None
                                      },
                     "timocean": {'fonetical_rules': None,
                                  "fonetical_examples": None,
                                  "gramatical_rules": None
                                  },
                     }

def invert_dict(d):
    inv = dict()
    for (k, v) in d.items():
        if isinstance(v, str):
            inv[v] = k
        elif isinstance(v, list):
            v = list(set(v))
            for elem in v:
                inv[elem] = k
    return inv


for (k, v) in dialectical_rules.items():
    dialect_dict = v
    for (k_, v_) in dialect_dict.items():
        a = v_
        if isinstance(a, dict):
            a = invert_dict(a)
        dialectical_rules[k][k_] = a

classes = ["crisanean", "maramuresean", "banatean", "ardelean", "oltean", "moldovean", "muntean", "timocean"]

class_to_book = {'crisanean': [''],
                 'maramuresean': ["dstef_antologie-de-folclor-din-maramures.pdf"],
                 'banatean': ['Poezi-in-grai-banatean-vol1.pdf'],
                 'ardelean': ['Ion_Pop_Reteganul_Poveti_ardeleneti_Ba.pdf'],
                 'oltean': ['Dilibau. Povesti oltenesti - Cristiana Belodan.pdf'],
                 'moldovean': ['Moldovan_in_Ukraine_01.pdf'],
                 'muntean': [''],
                 "timocean": [""]}

book_to_class = {'dstef_antologie-de-folclor-din-maramures.pdf': 'maramuresean',
                 'Poezi-in-grai-banatean-vol1.pdf': 'banatean',
                 'Ion_Pop_Reteganul_Poveti_ardeleneti_Ba.pdf': 'ardelean',
                 'Dilibau. Povesti oltenesti - Cristiana Belodan.pdf': 'oltean',
                 'Moldovan_in_Ukraine_01.pdf': 'moldovean'}

class_to_video = {'crisanean': [''],
                  'maramuresean': [''],
                  'banatean': [''],
                  'ardelean': ['Curs de dialect ardelenesc!.mp4',
                               'Curs de dialect ardelenesc!suduieli si blesteme!.mp4'],
                  'oltean': [''],
                  'moldovean': ["Stirile in limba moldoveneasca.mp4",
                                'Igor Dodon explică strategia prin care doreşte să mute graniţa dintre România şi Republica Moldova.mp4',
                                "Vox pop Unirea cu România şi preţul ei.mp4",
                                "Vox populi Tinerii despre România şi Unire.mp4"],
                  'muntean': [''],
                  'timocean': ['About our village and our language – Timok Romanian (Vlach) Collection.mp4']}

video_to_class = {'Curs de dialect ardelenesc!.mp4': 'ardelean',
                  'Curs de dialect ardelenesc!suduieli si blesteme!.mp4': 'ardelean',
                  'Stirile in limba moldoveneasca.mp4': 'moldovean',
                  'Igor Dodon explică strategia prin care doreşte să mute graniţa dintre România şi Republica Moldova.mp4': 'moldovean',
                  'Vox pop Unirea cu România şi preţul ei.mp4': 'moldovean',
                  'Vox populi Tinerii despre România şi Unire.mp4': 'moldovean',
                  'About our village and our language – Timok Romanian (Vlach) Collection.mp4': 'timocean'}

video_to_alias = {'Curs de dialect ardelenesc!.mp4': 'ardelenesc.txt',
                  'Curs de dialect ardelenesc!suduieli si blesteme!.mp4': 'ardelenesc_suduieli.txt',
                  'Stirile in limba moldoveneasca.mp4': 'stiri_moldoveneasca.txt',
                  'Igor Dodon explică strategia prin care doreşte să mute graniţa dintre România şi Republica Moldova.mp4': 'dodon.txt',
                  'Vox pop Unirea cu România şi preţul ei.mp4': 'vox_pop_pretul_unirii.txt',
                  'Vox populi Tinerii despre România şi Unire.mp4': 'vox_pop_romania_unire.txt',
                  'About our village and our language – Timok Romanian (Vlach) Collection.mp4': 'timok.txt'}

import pandas as pd

df = pd.read_csv("data/RoAcReL.csv")

print(df.columns)
print(set(df["County/Region"]))

words = df['Word'].to_list()
meanings = df["Meaning"].to_list()
origins = df["County/Region"].to_list()

classes_ = ['oltean', 'moldovean', 'muntean', 'ardelean', 'maramuresean', 'banatean']

dialect_to_formal_dict = {'oltean': {},
                          'moldovean': {},
                          'muntean': {},
                          'ardelean': {},
                          'maramuresean': {},
                          'banatean': {}}

specifical_change_stuff_rules_dict = {'oltean': {},
                                      'moldovean': {},
                                      'muntean': {},
                                      'ardelean': {},
                                      'maramuresean': {},
                                      'banatean': {}}

exceptions_to_rules_dict = {'oltean': {},
                            'moldovean': {},
                            'muntean': {},
                            'ardelean': {},
                            'maramuresean': {},
                            'banatean': {}}

county_region_to_dialect = {'Moldova, Transilvania': ["moldovean", "ardelean"],
                            'Maramureș': ["maramuresean"],
                            'Dobrogea': ["muntean"],
                            'Comuna Șerbănești, Județul Olt': ["oltean"],
                            'Bucovina': ["moldovean"],
                            'Bucovina / Republica Moldova': [],
                            'Oltenia': ["oltean"],
                            'Sudul Moldovei': ["moldovean"],
                            'Comuna Suharău, Județul Botoșani': [],
                            'Muntenia': ["muntean"],
                            'Banat': ["banatean"],
                            'Moldova': ["moldovean"],
                            'Transilvania': ["ardelean"],
                            'Ardeal': ["ardelean"]}

cnt = 0
print(len(df))
for (dialect_word, formal_word, origin) in zip(words, meanings, origins):
    if origin != origin:
        continue
    cnt += 1
    origins_ = county_region_to_dialect[origin]
    for origin in origins_:
        dialect_to_formal_dict[origin][dialect_word] = formal_word

print(cnt)
print(f"For {len(df) - cnt} words out of the {len(df)} in RoAcReL there is no origin!")

"""
ierarchie/cascada de aplicata reguli

intai pe cuvinte

apoi pe grupuri de litere sortate descrescator, de la grupuri de 3 litere, la 2 litere, la 1 litera
"""
