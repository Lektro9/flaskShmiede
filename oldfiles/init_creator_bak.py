from Testcontent import Content, Karten_Content

THEMEN_DICT = Content()
KARTEN_DICT = Karten_Content()
##print(THEMEN_DICT)
##print(KARTEN_DICT)

vorlage = """
@app.route('/FACHLINKZURSEITE/')
def FUNKTIONSTITEL():
	try:
		return render_template("FACH/ORDNER/HTMLNAME", aktFach="FACH", aktThema="THEMA", kartenURL="/FACHKARTENLINK",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))
"""

vorlage_karten = """
@app.route('/FACHLINKZURSEITE/')
def FUNKTIONSTITEL():
	try:
		return render_template("FACH/ORDNER/HTMLNAME", aktFach="FACH", aktThema="THEMA", kartenURL="/FACHKARTENLINK",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["FACH"]["THEMA"])
	except Exception as e:
		print(str(e))
"""
##Achtung bei FACH und LINKZURSEITE

#print(THEMEN_DICT["ITS"][0][1])

for fach in THEMEN_DICT:
    #print(fach)
    for thema in THEMEN_DICT[fach]:
        FACH = fach
        LINKZURSEITE = thema[1]
        KARTENLINK = (thema[1]+"-karten")
        KARTENHTML = (thema[1]+"-karten.html")
        FUNKTIONSTITEL = thema[0].replace("-", "_").replace(".", "_").replace(" ", "_")
        KARTENFUNKTION = thema[0].replace("-", "_").replace(".", "_").replace(" ", "_")+"_karten"
        ORDNER = thema[0].replace("-", "_").replace(".", "_").replace(" ", "_") # important for html creation
        THEMA = thema[0]
        HTMLNAME = (thema[1]+".html").replace("/", "") # important for html creation
        HTMLNAME_KARTEN = (thema[1]+"-karten.html").replace("/", "")
        print(vorlage.replace("LINKZURSEITE", LINKZURSEITE).replace("FUNKTIONSTITEL", FUNKTIONSTITEL).replace("FACH", FACH).replace("THEMA", THEMA).replace("HTMLNAME", HTMLNAME).replace("KARTENLINK", KARTENLINK).replace("ORDNER", ORDNER))
        print(vorlage_karten.replace("LINKZURSEITE", KARTENLINK).replace("FUNKTIONSTITEL", KARTENFUNKTION).replace("FACH", FACH).replace("THEMA", THEMA).replace("HTMLNAME", HTMLNAME_KARTEN).replace("KARTENHTML", KARTENHTML).replace("ORDNER", ORDNER))
##for fach in KARTEN_DICT:
##    for thema in KARTEN_DICT[fach]:
##        print(thema)
