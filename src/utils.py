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

muntean_fonetical_examples = {" ușă ": " ușe ",
                              " lojă ": " loje ",
                              " deștept ": " dăștept ",
                              " din ": " dân ",
                              " fetele ": " fetili ",
                              " caprele ": " caprili "}

muntean_fonetical_rules = {"ă ": "e ",
                           "e": ["ă", "i"],
                           "i": "â"}

muntean_gramatical_examples = {"n-am decât două mere": "am decât două mere",
                               "nu mă mai duc": "nu mai mă duc",
                               "mănâncă pâine": " 	mănâncă la pâine",
                               " 	omul care vine": "omul de vine",
                               "floarea de pe masă": "floarea după/dupe masă",
                               "grinda este așezată aici": "grinda vine așezată aici",
                               "începe să crească": " 	vine și/de crește",
                               "era să cad": " 	am vrut să cad",
                               " 	ei/ele au venit": "ei/ele a venitără",
                               "ei/ele vor bea": "ei/ele va bea",
                               "ei/ele beau": "ei/ele bea"}

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

oltenesc_lexical_examples = {"șold": "arm",
                             "a strănuta": "a străfiga",
                             " 	picior de pasăre": "cotoi"}

# wikipedia above
# colegiu.info below

moldavean_rules = {"pi": "chi", "fe": "fi"}
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
