

THEMEN_DICT = {}
KARTEN_DICT = {}

def Content():
    THEMEN_DICT = {"ITS": [["PC-Struktur", "/PC-Struktur",],
                                 ["RAM ROM CACHE", "/RAM-ROM-CACHE"],
								 ["IPv4", "/IPv4"]],
                   "AWE": [["Einstieg", "/Einstieg"], ["Rechner", "/Rechner"],["Bubblesort", "/Bubblesort"]]
                   }
##    ITS_THEMEN = []
##    for k in THEMEN_DICT["ITS"]:
##        ITS_THEMEN.append(k)
##    print(ITS_THEMEN)
    return THEMEN_DICT

def Karten_Content():
    KARTEN_DICT = {"ITS": {"PC-Struktur":[["Was ist das EVA-Prinzip?", "Eingabe Verarbeitung Ausgabe"],
                                 ["Wofür ist das Bussystem verantwortlich?", "fehlerfreie Datenübtragung zwischen Komponenten ('Leitungen')"],
								 ["Welche Bussysteme gibt es?", "Datenbus Adressbus Steuerbus"],
								 ["Was macht der Datenbus?", "transportiert die Hauptdaten"],
								 ["Was macht der Adressbus?", "gibt Komponenten unterschiedliche 'Adressen'"],
								 ["Was macht der Steuerbus?", "kontrolliert wer wann welche 'Busleitung' benutzen darf"],
								 ["Wie überträgt die serielle Datenübertragung?", "Bit für Bit, nacheinander (bps (bits))"],
								 ["Wie überträgt die parallele Datenübertragung?", "Byte für Byte (8 bits gleichzeitig) (Bps (Bytes))"],
								 ["Was heißt Simplex", "nur Senden zb Radio, TV"],
								 ["Halbduplex", "Senden ODER Empfangen zb Walkie-Talkie"],
								 ["Vollduplex", "Senden UND Empfangen zb 1000BASE-T(doppelter Netzwerkanschluss)"],
								 ["Chipset(traditionell)", "Northbridge(MCH) Southbridge(ICH)"],
								 ["Was heißt MCH", "Memory Controller Hub Für RAM, CPU, GPU"],
								 ["ICH", "I/O Controller Hub Für PCI, Flash ROM, I/O Panel, SATA, CMOS Memory"],
								 ["Chipset(modern)", "Northbridge in CPU Southbridge ist nun PCH('Platform')"]],
								 
						 "IPv4": [["Woraus besteht eine IPv4?", "32Bit, 4Byte, geschrieben in 4 Oktetten"],
								 ["Was ist eine Netzklassen?", "Unterteilung des IPv4-Adressbereiches(A, B, C, D, evtl.E)"],
								 ["Nenne den Bereich von Klasse A", "10.0.0.0 - 127.255.255.255"],
								 ["Nenne den Bereich von Klasse B", "128.0.0.0 - 191.255.255.255"],
								 ["Nenne den Bereich von Klasse C", "192... - 223..."],
								 ["Nenne den Bereich von Klasse D(Multicast)", "224... - 239..."],
								 ["Nenne den Bereich von Klasse E(zukünftige Zwecke)", "240.0.0.0 - 255.255.255.255"],
								 ["Was sind private Adressbereiche?", "nicht öffentlich verfügbar, nur für privaten Gebrauch"],
								 ["Nenne die privaten Adressbereiche", "10.0.0.0-10.255.255.255(CIDR: 10/8) 172.16/12 192.168/16"],
								 ["Was macht ein Subnetz?", "Unterteilung in mehrere Kleinnetzwerke"],
								 ["Wie unterteilt ein Subnetz?", "mithilfe von binären Grenzen unter gemeinsamen Vorderteil"],
								 ["Was ist die CIDR Schreibweise?", "Kurzform von 255.255.255.0 = /24"],
								 ["Testaufgabe: 255.255.240.0 in CIDR", "alle 1en aufschreiben und zählen = /20"],
								 ["Was ist der Sinn einer Netzadresse?", "Sie beschreibt das Netz und kann nicht vergeben werden"],
								 ["Was ist eine Hostadresse?", "Hostadressen können beliebig vergeben werden"],
								 ["Testaufgabe: Netzadresse von 10.15.0.1/16", "10.15.0.0 kann nicht vergeben werden!"],
								 ["Was ist mit einer Broadcast-Adresse möglich?", "letzte Adresse im Netzwerk, kann alle in diesem Netzwerk erreichen"],
								 ["Testaufgabe: Broadcast-Adresse von 192.168.0.1/24", "192.168.0.255 kann nicht vergeben werden!"],
						   
						   
						   
						   ]},
                   "AWE": {"Einstieg": [["Was macht ein Algorithmus?", "gibt einen eindeutigen Lösungsweg in Einzelschritten"], 
										["Was kann eine Variable?", "Informationen mit Datentyp speichern, veränderbar"],
										["Wie funktioniert ein Datentyp?", "Wie eine Einheit (Bsp.: Int, float, char, str)"],
										["Wofür steht 'PAP'", "Programmablaufplan"],
										
										
										
										
										]}
				   
				   
				   }
    
##    for thema, inhalt in KARTEN_DICT.items():
##        #print(thema)
####        print("/"+thema+"/")
##        for unterthema in inhalt:
##            #print(unterthema)
##            for karte in inhalt[unterthema]:
##                print(karte)
##                #print(karte[1])
####            um alles zu erreichen

##    testliste = KARTEN_DICT["ITS"]["PC-Struktur"]
##    for a in testliste:
##        print(a[1])
    return KARTEN_DICT



##Karten_Content()


## WHAT DO I NEED Example:
## {Fach: [Thema, URL]}
## {Karten_Fach: {Thema: [[Frage, Antwort], [Frage, Antwort]]}}


