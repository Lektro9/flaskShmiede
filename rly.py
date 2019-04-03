THEMEN_DICT = {}
KARTEN_DICT = {}

def Content():
    THEMEN_DICT = {"ITS": [["PC-Struktur", "/PC-Struktur",],
                                 ["RAM ROM CACHE", "/RAM-ROM-CACHE"],
								 ["IPv4", "/IPv4"],
								 ["Zahlensysteme", "/Zahlensysteme"],
								 ["Subnetting", "/Subnetting"],
								 ["PCIe", "/PCIe"],
								 ["HDD SSD", "/HDD-SSD"]
								 
								 ],
                   "AWE": 		[["Einstieg", "/Einstieg"], ["Rechner", "/Rechner"],["Bubblesort", "/Bubblesort"]],
				   "Englisch":  [["Vokabeln", "/Vokabeln"], ["Vokabeln2", "/Vokabeln2"]],
				   "WGP": 		[["Arbeitsrecht", "/Arbeitsrecht"], ["Berufsbildungsgesetz", "/Berufsbildungsgesetz"]]
                   }
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
								 ["Testaufgabe: Netzadresse von 10.15.0.1/16", "10.15.0.0, kann aber nicht vergeben werden!"],
								 ["Was ist mit einer Broadcast-Adresse möglich?", "letzte Adresse im Netzwerk, kann alle in diesem Netzwerk erreichen"],
								 ["Testaufgabe: Broadcast-Adresse von 192.168.0.1/24", "192.168.0.255, kann aber nicht vergeben werden!"]
								 
								 ],
								 
				 "Zahlensysteme": [["Nenne die drei wichtigsten Zahlensysteme in der Informatik", "Binär, Dezimal, Hexadezimal"],
								  ["Rechne von binär zu dezimal: 11000000", "192"],
								  ["Rechne von dezimal zu binär: 252", "11111100"],
								  ["Rechne von hexadezimal zu binär: 6A", "0110 1010"],
								  ["Rechne von hexadezimal zu dezimal: AFE", "1010 1111 1110 -> 2048+512+128+64+32+16+8+4+2= 2814"],
								  ["Macadressen werden in der Regel __ geschrieben.", "hexadezimal"],
								  ["Übersetze den ASCII Binärcode: 01100111<br>01101010 ", "'gj' mit <a href='http://roubaixinteractive.com/PlayGround/Binary_Conversion/The_Characters.asp' target='_blank'>Tabelle</a>"]
								 
								 ],
					"Subnetting": [["Wie prüft eine Subnetzmaske, ob eine IP-Adresse zum Netzwerk gehört?", "Sie vergleicht die '1-en' mit dem Zielnetzwerk"],
								  ["Was zeigt die 'dotted decimal notation'?", "Subnetzmaske in dezimal-Zahlen"],
								  ["Wie bestimmt man die <a href='https://de.wikipedia.org/wiki/Classless_Inter-Domain_Routing' target='_blank'>'CIDR'</a>-Schreibweise (zb /20)", "alle '1-en' in der Subnetzmaske zählen"],
								  ["In wieviele Netze muss ich tatsächlich teilen, wenn ich 40 Netze brauche?", "64"],
								  ["Um wieviel würde sich /24 dann erweitern?", "um 6 weitere Bits also /30"],
								  ["Bestimme die Broadcast-Adresse von 192.168.1.0/30", "Netzabstand=4 (256/64), also Broadcast-Adresse: 192.168.1.3"],
								  ["Testaufgabe: 10.0.0.0/8 ges.: 450 Netze gebe alle Infos an wie in der letzten Tabelle im Artikel", "<a href='http://shmiede.de/ITS/snloesung/' target='_blank'>Lösung</a>"],
							
								 ],
				 "RAM ROM CACHE": [["Wofür steht 'RAM'?", "'Random-Access Memory'"],
								  ["Warum nutzen wir RAM anstatt z.B. Festplatten?", "RAM ist um ein vielfaches schneller und kann auf Speicheradressen direkt zugreifen"],
								  ["Wofür steht SRAM und DRAM", "statisches und dynamisches RAM"],
								  ["Ist ein Cache ein DRAM?", "Nein es ist ein SRAM, da dieser schneller ist und nicht 'refreshed' werden muss."],
								  ["Warum wird bei heutigen Arbeitsspeicher das DRAM, statt des SRAMs genutzt?", "DRAM hat weniger Bauelemente und kann mehr Speicher auf weniger Platz nutzen."],
								  ["Wofür steht die Zahlenangabe '1600' (zb in DDR1 PC 1600)?", "Dies ist die Taktrate in Mhz, also 1600 Mhz"],
								  ["Wie rechnet man die Taktrate (1866Mhz) in MByte/s um?", "Busbreite(64Bit) * Taktrate(1866Mhz) / 8 = 14928 MByte/s"],
								  ["Wofür steht 'ROM'?", "Read Only Memory"],
								  ["Wozu wurden ROMs meistens genutzt?", "BIOS, CD-ROM"],
								  ["Ist ein ROM ein flüchtiger oder nicht flüchtiger Speicher?", "Ein nicht flüchtiger Speicher (BIOS-Einstellungen bleiben erhalten)"],
								  ["Wofür steht die Bezeichnung 'EEPROM'?", "Electrically Erasable Programmable Read Only Memory, ein neu beschreibbarer ROM"],
								  ["Was macht die 'read-ahead'-Funktion eines Cache?", "Wichtige Daten werden vermutet und Zwischengespeichert"],
								  ["Welches Cache hat den größeren Speicher: L1, L2 oder L3?", "L3, da er weiter vom Kern entfernt ist und mehr Platz hat"],
								  ["Welches Cache ist am schnellsten: L1, L2 oder L3?", "L1, da dieser sich direkt neben dem Kern befindet"],
								  ["Was sind die Hauptaufgaben eines Cache?", "Wichtige Daten/Befehle schneller abrufbar zu machen und Kerne gleichmäßig auszulasten"],
							
								 ],
						"PCIe":   [["Welche Schnittstellen hat PCIe abgelöst?", "PCI, PCI-X und AGP"],
								  ["Was macht ein PCIe-Controller?", "Er ist mit den Erweiterungskarten verbunden und steuert diese."],
								  ["Wo sind die beiden PCIe-Controller zu finden?", "In der CPU (steuert Grafikkarten-Slots) und in dem Chipset (steuert alle anderen Slots)"],
								  ["Aus wievielen Leitungen besteht eine 'Lane'?", "Aus zwei Leitungspaaren (Datenversand und Datenempfang)"],
								  ["Mit wievielen Lanes kommuniziert ein PCIe-Controller?", "16 Lanes"],
								  ["Wieviele Lanes braucht eine übliche Grafikkarte?", "16 Lanes"],
								  ["Mit welchen Verfahren kann man mehrere Grafikkarten gleichzeitig nutzen?", "<a href='http://www.pcgameshardware.de/Mainboard-Hardware-154107/Specials/PCI-Express-erklaert-1168801/' target='_blank'>PCI-Sharing oder PCI-Switch</a>"],
								  
								 ],
						"HDD SSD":[["Wofür steht 'HDD'?", "Hard Disk Drive"],
								  ["Wofür steht 'SSD'?", "Solid State Drive"],
								  ["Nenne Anschlussmöglichkeiten für Festplatten", "SATA, SAS, Parallel SCSI, PCIe, Fibre-Channel-Interface"],
								  ["Ist es sicher eine Festplatte einfach zu formatieren?", "Nein, da alte Datenreste ausgelesen werden können."],
								  ["Warum ist eine HDD so laut im Vergleich mit einer SSD?", "HDDs arbeiten mechanisch und ein Schreibarm macht Geräusche beim Lesen/Schreiben"],
								  ["Wenn ich möglichst viel Speicher für wenig Geld haben möchte kaufe ich eine __.", "HDD, da diese günstiger im Speicher pro Euro Verhältnis sind."],
								  ["Ich installiere mein Betriebssystem lieber auf einer __ um schneller zu booten", "SSD, da diese schnellere Zugriffszeiten bietet."],
								  ["Warum ist eine HDD-Festplatte langsamer als eine SSD-Festplatte?", "Eine HDD muss eine Scheibe drehen, wohingegen die SSD einfach einen Flashspeicher abrufen muss."],
								  
								 ],
						   },
                   "AWE": {"Einstieg": [["Was macht ein Algorithmus?", "gibt einen eindeutigen Lösungsweg in Einzelschritten"], 
										["Was kann eine Variable?", "Informationen mit Datentyp speichern, veränderbar"],
										["Wie funktioniert ein Datentyp?", "Wie eine Einheit (Bsp.: Int, float, char, str)"],
										["Wofür steht 'PAP'", "Programmablaufplan"],
										
										
										
										
										]},
					"Englisch": {"Vokabeln": [["Our company was founded in 1997", "Unsere Firma wurde 1997 gegründet."],
												["In 2005 we were taken over by", "2005 wurden wir von ... übernommen"],
												["We are a leading manufacturer of", "Wir sind ein führender Hersteller von"],
												["We are a small-sized/medium-sized/large-sized company", "Wir sind ein kleines/mittelständisches/großes Unternehmen"],
												["We are a chain of electronic suppliers.", "Wir sind eine Kette von Elektronik-Anbietern."],
												["We offer sustainable solutions.", "Wir bieten nachhaltige Lösungen an."],
												["Our products are both reliable and long-lasting.", "Unsere Produkte sind zuverlässig und haben eine lange Lebensdauer."],
												["Our software is adapted to suit your requirements.", "Unsere Software wird Ihren Bedürfnissen angepasst."],
												["X employees work for our company.", "Für unsere Firma arbeiten X Angestellte."],
												["(to) have a sales volume of X Euro per annum", "einen jährlichen Umsatz von X Euro haben"],
												["(to) sell products within a range of ... kilometres", "Produkte im Umkreis von ... Kilometer verkaufen"],
												["(to) be one of the leading companies in the local market/Bonn area/ world market", "einer der lokalen Marktführer/Marktführer im Bonner Umkreis/weltweiten Marktführer sein"],
												["(to) have branchen/subsidiaries in", "Filialen/Tochtergesellschaften in ... haben"],
												["(to) be situated in", "liegen/sich befinden"],
												["(to) be based in ...", "ansässig sein"],
												["The head office is located in..", "Der Hauptsitz liegt in..."],
												["(to) be specialised in databases/networks/software development/providing Internet access/web design", "auf etwas spezialisiert sein (Datenbanken/Netzwerke/ Anwendungsentwicklung/ Internetprovider/ Webdesign)"],
												["(to) provide cost-effective solutions", "kostengünstige Lösungen anbieten"],
												["(to) satisfy/meet/suit the needs of a customer", "die Bedürfnisse eines Kunden erfüllen"],
												["(to) have a high reputation for...", "einen guten Ruf für etwas haben"],
												["(to) be responsible for /(to) be in charge of", "für etwas verantwortlich sein"],
												["(to) have a flat hierarchy", "eine flache Hierarchie haben"],
												["(to) analyse business processes", "Geschäftsprozesse analysieren"],
												["(to) organise tasks in projects", "Projektaufgaben organisieren"],
												["personnel department", "Personalabteilung"],
												["sales and marketing department", "Vertriebsabteilung"],
												["finance department", "Finanzabteilung"],
										
										
										
										
										],
								"Vokabeln2": [["purchasing department", "Einkaufsabteilung"],
											["administration", "Verwaltung"],
											["research and development", "Forschung und Entwicklung"],
											["Im training to become a ...", "Ich mache eine Lehre/Ausbildung zur/zum ..."],
											["I am responsible for programming the machines.", "Ich bin for die Programmierung der Maschinen zuständig."],
											["I work shifts.", "Ich mache Schichtarbeit."],
											["I often have to do overtime.", "Ich muss oft Überstunden machen"],
											["I repair electrical devices.", "Ich repariere elektrische Geräte."],
											["My superior is ...", "Mein Vorgesetzter ist ..."],
											["I want to become a(n)... IT security officer/IT specialist, specialised in applications development/IT specialist, specialised in system integration / IT system support specialist/IT system electronics technician", "Ich möchte gerne ein ... werden IT-Sicherheitsbeauftragter/IT-Fachmann im Bereich Anwendungsentwicklung / IT-Fachmann im Bereich Systemintegration / IT-Systembetreuer / IT-Systemelektroniker"],
											["Our regular office hours are from ... to ...", "Unnare regulieren Bürozeiten sind von ... bis ..."],
											["I get ... days of leave per year.", "Ich habe im Jahr ... Urlaubstage"],
											["We have flexible working hours.", "Wir haben flexible Arbeitszeiten."],
											["First thing I do every morning is ...", "Jeden morgen mache ich als erstes ..."],
											["I usually run the backup jobs in our computer centre.", "In der Regel übernehme ich die Backup-Jobs in unserem Computerzentrum"],
											["I would like to start telling you about my company.", "Zunächst möchte ich Ihnen etwas über meine Firma erzählen"],
											["I would like to welcome any questions at the end of my presentation.", "Ich bin gern bereit, etwaige Fragen am Ende meiner Präsentation zu beantworten."],
											["Now my second point is ...", "Ich komme nun zu Punkt 2 ..."],
											["Thirdly, let me give you some basic statistics", "Drittens darf ich Ihnen ein paar grundlegende Statistiken zeigen."],
											["I would now like to move on to the next topic.", "Ich möchte nun gern zur nächsten Thema übergehen."],
											["An excellent example of this is ...", "Ein hervorragendes Beispiel dafür ist.."],
											["I would like to give you an example to illustrate this point.", "Ich möchte diesen Punkt mit einem Beispiel erläutern."],
											["To sum up we can say that ...", "Zusammenfassend kann man sagen, dass ..."],
											["Before I finish my presentation, I'd just like to mention ...", "Bevor ich meinen Vortrag beende, möchte ich ... kurz erwähnen."],
											["Well, that's the end of my presentation.", "Damit bin ich am Ende meiner Präsentation angelangt."],
											["Thank you for your attention.", "Vielen Dank für Ihre Aufmerksamkeit."],
										
										
										]}
				   
				   
				   }
    return KARTEN_DICT
##    for thema, inhalt in KARTEN_DICT.items():
##        print(thema)
####        print("/"+thema+"/")
##        for unterthema in inhalt:
##            print(unterthema)
##            for karte in inhalt[unterthema]:
##                print(karte[0])
##                print(karte[1])
##            um alles zu erreichen



## WHAT DO I NEED Example:
## {Fach: [Thema, URL]}
## {Karten_Fach: {Thema: [[Frage, Antwort], [Frage, Antwort]]}}
