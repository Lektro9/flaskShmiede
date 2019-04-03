from flask import Flask, render_template
import rly
import sys

app = Flask(__name__)

THEMEN_DICT = rly.Content()
KARTEN_DICT = rly.Karten_Content()


						# Themen-Dictionaries
ITS_THEMEN = []
for k in THEMEN_DICT["ITS"]:
	ITS_THEMEN.append(k)

AWE_THEMEN = []
for k in THEMEN_DICT["AWE"]:
	AWE_THEMEN.append(k)

ENG_THEMEN = []
for k in THEMEN_DICT["Englisch"]:
	ENG_THEMEN.append(k)
	
WGP_THEMEN = []
for k in THEMEN_DICT["WGP"]:
	WGP_THEMEN.append(k)

	
							# Homepages for Topics
@app.route('/')
def homepage():
	return render_template("home.html", aktFach="AWE", aktThema="Rechner", kartenURL="KARTENLINK")

@app.route('/its/')		
@app.route('/ITS/')
def ITS():
	try:
		return render_template("ITS/ITS.html", ITS_THEMEN=ITS_THEMEN, aktFach="ITS")
	except Exception as e:
		print(str(e))

@app.route('/awe/')		
@app.route('/AWE/')
def AWE():
	try:
		return render_template("AWE/AWE.html", ITS_THEMEN=ITS_THEMEN, aktFach="AWE", AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))

@app.route('/englisch/')		
@app.route('/Englisch/')
def englisch():
	try:
		return render_template("Englisch/Englisch.html", ENG_THEMEN=ENG_THEMEN, ITS_THEMEN=ITS_THEMEN, aktFach="Englisch", AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))
		
@app.route('/WGP/')		
@app.route('/wgp/')
def wgp():
	try:
		return render_template("WGP/WGP.html", WGP_THEMEN=WGP_THEMEN, ENG_THEMEN=ENG_THEMEN, ITS_THEMEN=ITS_THEMEN, aktFach="WGP", AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))
		
		
								# ITS

@app.route('/ITS/PC-Struktur/')
def PC_Struktur():
	try:
		return render_template("ITS/PC_Struktur/PC-Struktur.html", aktFach="ITS", aktThema="PC-Struktur", kartenURL="/ITS/PC-Struktur-karten",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/ITS/PC-Struktur-karten/')
def PC_Struktur_karten():
	try:
		return render_template("ITS/PC_Struktur/PC-Struktur-karten.html", aktFach="ITS", aktThema="PC-Struktur", zurueckURL="/ITS/PC-Struktur",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["ITS"]["PC-Struktur"])
	except Exception as e:
		print(str(e))


@app.route('/ITS/RAM-ROM-CACHE/')
def RAM_ROM_CACHE():
	try:
		return render_template("ITS/RAM_ROM_CACHE/RAM-ROM-CACHE.html", aktFach="ITS", aktThema="RAM ROM CACHE", kartenURL="/ITS/RAM-ROM-CACHE-karten",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/ITS/RAM-ROM-CACHE-karten/')
def RAM_ROM_CACHE_karten():
	try:
		return render_template("ITS/RAM_ROM_CACHE/RAM-ROM-CACHE-karten.html", aktFach="ITS", aktThema="RAM ROM CACHE", zurueckURL="/ITS/RAM-ROM-CACHE",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["ITS"]["RAM ROM CACHE"])
	except Exception as e:
		print(str(e))


@app.route('/ITS/IPv4/')
def IPv4():
	try:
		return render_template("ITS/IPv4/IPv4.html", aktFach="ITS", aktThema="IPv4", kartenURL="/ITS/IPv4-karten",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/ITS/IPv4-karten/')
def IPv4_karten():
	try:
		return render_template("ITS/IPv4/IPv4-karten.html", aktFach="ITS", aktThema="IPv4", zurueckURL="/ITS/IPv4",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["ITS"]["IPv4"])
	except Exception as e:
		print(str(e))


@app.route('/ITS/Zahlensysteme/')
def Zahlensysteme():
	try:
		return render_template("ITS/Zahlensysteme/Zahlensysteme.html", aktFach="ITS", aktThema="Zahlensysteme", kartenURL="/ITS/Zahlensysteme-karten",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/ITS/Zahlensysteme-karten/')
def Zahlensysteme_karten():
	try:
		return render_template("ITS/Zahlensysteme/Zahlensysteme-karten.html", aktFach="ITS", aktThema="Zahlensysteme", zurueckURL="/ITS/Zahlensysteme",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["ITS"]["Zahlensysteme"])
	except Exception as e:
		print(str(e))


@app.route('/ITS/Subnetting/')
def Subnetting():
	try:
		return render_template("ITS/Subnetting/Subnetting.html", aktFach="ITS", aktThema="Subnetting", kartenURL="/ITS/Subnetting-karten",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))
		
@app.route('/ITS/snloesung/')
def snloesung():
	try:
		return render_template("ITS/Subnetting/snloesung.html")
	except Exception as e:
		print(str(e))


@app.route('/ITS/Subnetting-karten/')
def Subnetting_karten():
	try:
		return render_template("ITS/Subnetting/Subnetting-karten.html", aktFach="ITS", aktThema="Subnetting", zurueckURL="/ITS/Subnetting",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["ITS"]["Subnetting"])
	except Exception as e:
		print(str(e))


@app.route('/ITS/PCIe/')
def PCIe():
	try:
		return render_template("ITS/PCIe/PCIe.html", aktFach="ITS", aktThema="PCIe", kartenURL="/ITS/PCIe-karten",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/ITS/PCIe-karten/')
def PCIe_karten():
	try:
		return render_template("ITS/PCIe/PCIe-karten.html", aktFach="ITS", aktThema="PCIe", zurueckURL="/ITS/PCIe",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["ITS"]["PCIe"])
	except Exception as e:
		print(str(e))


@app.route('/ITS/HDD-SSD/')
def HDD_SSD():
	try:
		return render_template("ITS/HDD_SSD/HDD-SSD.html", aktFach="ITS", aktThema="HDD SSD", kartenURL="/ITS/HDD-SSD-karten",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/ITS/HDD-SSD-karten/')
def HDD_SSD_karten():
	try:
		return render_template("ITS/HDD_SSD/HDD-SSD-karten.html", aktFach="ITS", aktThema="HDD SSD", zurueckURL="/ITS/HDD-SSD",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["ITS"]["HDD SSD"])
	except Exception as e:
		print(str(e))

		
							# AWE

@app.route('/AWE/Einstieg/')
def Einstieg():
	try:
		return render_template("AWE/Einstieg/Einstieg.html", aktFach="AWE", aktThema="Einstieg", kartenURL="/AWE/Einstieg-karten",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/AWE/Einstieg-karten/')
def Einstieg_karten():
	try:
		return render_template("AWE/Einstieg/Einstieg-karten.html", aktFach="AWE", aktThema="Einstieg", zurueckURL="/AWE/Einstieg",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["AWE"]["Einstieg"])
	except Exception as e:
		print(str(e))


@app.route('/AWE/Rechner/')
def Rechner():
	try:
		return render_template("AWE/Rechner/Rechner.html", aktFach="AWE", aktThema="Rechner", kartenURL="/AWE/Rechner-karten",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/AWE/Rechner-karten/')
def Rechner_karten():
	try:
		return render_template("AWE/Rechner/Rechner-karten.html", aktFach="AWE", aktThema="Rechner", zurueckURL="/AWE/Rechner",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["AWE"]["Rechner"])
	except Exception as e:
		print(str(e))


@app.route('/AWE/Bubblesort/')
def Bubblesort():
	try:
		return render_template("AWE/Bubblesort/Bubblesort.html", aktFach="AWE", aktThema="Bubblesort", kartenURL="/AWE/Bubblesort-karten",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/AWE/Bubblesort-karten/')
def Bubblesort_karten():
	try:
		return render_template("AWE/Bubblesort/Bubblesort-karten.html", aktFach="AWE", aktThema="Bubblesort", zurueckURL="/AWE/Bubblesort",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["AWE"]["Bubblesort"])
	except Exception as e:
		print(str(e))

											# ENGLISCH
		
@app.route('/Englisch/Vokabeln/')
def Vokabeln():
	try:
		return render_template("Englisch/Vokabeln/Vokabeln.html", aktFach="Englisch", aktThema="Vokabeln", kartenURL="/Englisch/Vokabeln-karten", ENG_THEMEN=ENG_THEMEN, ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/Englisch/Vokabeln-karten/')
def Vokabeln_karten():
	try:
		return render_template("Englisch/Vokabeln/Vokabeln-karten.html", aktFach="Englisch", aktThema="Vokabeln", zurueckURL="/Englisch/Vokabeln",  ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, ENG_THEMEN=ENG_THEMEN, Kartei=KARTEN_DICT["Englisch"]["Vokabeln"])
	except Exception as e:
		print(str(e))

@app.route('/Englisch/Vokabeln2/')
def Vokabeln2():
	try:
		return render_template("Englisch/Vokabeln2/Vokabeln2.html", aktFach="Englisch", aktThema="Vokabeln2", kartenURL="/Englisch/Vokabeln2-karten", ENG_THEMEN=ENG_THEMEN, WGP_THEMEN=WGP_THEMEN, ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/Englisch/Vokabeln2-karten/')
def Vokabeln2_karten():
	try:
		return render_template("Englisch/Vokabeln2/Vokabeln2-karten.html", aktFach="Englisch", aktThema="Vokabeln2", zurueckURL="/Englisch/Vokabeln2", WGP_THEMEN=WGP_THEMEN, ENG_THEMEN=ENG_THEMEN, ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["Englisch"]["Vokabeln2"])
	except Exception as e:
		print(str(e))
		
										# WGP
										
@app.route('/WGP/Arbeitsrecht/')
def Arbeitsrecht():
	try:
		return render_template("WGP/Arbeitsrecht/Arbeitsrecht.html", aktFach="WGP", aktThema="Arbeitsrecht", kartenURL="/WGP/Arbeitsrecht-karten", WGP_THEMEN=WGP_THEMEN, ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/WGP/Arbeitsrecht-karten/')
def Arbeitsrecht_karten():
	try:
		return render_template("WGP/Arbeitsrecht/Arbeitsrecht-karten.html", aktFach="WGP", aktThema="Arbeitsrecht", zurueckURL="/WGP/Arbeitsrecht", WGP_THEMEN=WGP_THEMEN, ENG_THEMEN=ENG_THEMEN, ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["WGP"]["Arbeitsrecht"])
	except Exception as e:
		print(str(e))


@app.route('/WGP/Berufsbildungsgesetz/')
def Berufsbildungsgesetz():
	try:
		return render_template("WGP/Berufsbildungsgesetz/Berufsbildungsgesetz.html", aktFach="WGP", aktThema="Berufsbildungsgesetz", kartenURL="/WGP/Berufsbildungsgesetz-karten", WGP_THEMEN=WGP_THEMEN, ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN)
	except Exception as e:
		print(str(e))


@app.route('/WGP/Berufsbildungsgesetz-karten/')
def Berufsbildungsgesetz_karten():
	try:
		return render_template("WGP/Berufsbildungsgesetz/Berufsbildungsgesetz-karten.html", aktFach="WGP", aktThema="Berufsbildungsgesetz", zurueckURL="/WGP/Berufsbildungsgesetz", WGP_THEMEN=WGP_THEMEN, ENG_THEMEN=ENG_THEMEN, ITS_THEMEN=ITS_THEMEN, AWE_THEMEN=AWE_THEMEN, Kartei=KARTEN_DICT["WGP"]["Berufsbildungsgesetz"])
	except Exception as e:
		print(str(e))
		
		
if __name__ == "__main__":
    app.run(host='0.0.0.0')

