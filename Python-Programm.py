"""
    Programm zum Auslesen der CPU- und RAM-
    Auslastung und Export in das CSV-Datenformat.

    Autor:  T.Kreuzkamp
    Datum:  01.03.2021
"""

import mymodules
import mysql.connector
from mysql.connector import errorcode
import csv
import psutil
import sys
from datetime import datetime

while 1:
    print ("")
    print( "Programm zum Auslesen der CPU- und RAM-Auslastung")
    print( "-------------------------------------------")
    print( "")
    print( "(1) Daten abspeichern")                                                 #Menü und Benutzerauswahl
    print( "(2) RAM-Daten auslesen")
    print( "(3) CPU-Daten auslesen")
    print( "(4) Datenbank erstellen")
    print( "(5) Datenbank löschen")
    print( "(0) Ende")
    befehl = int(input( "Auswahl: "))

    if( befehl < 0 or befehl > 5):                                                  #Testen, ob ein bekannter Befehl eingegeben wurde
        print( "Unbekannter Befehl: " + str(befehl))
        print( "")
        continue
    if befehl == 0:                                                                 #Programm beenden
        print( "Programm beendet")
        break
    if befehl == 1: 
        print (mymodules.Daten_abspeichern())                                       #Auf Modul zugreifen
        continue
    if befehl == 2:
        print (mymodules.Daten_RAM())                                               #Auf Modul zugreifen
        continue
    if befehl == 3:
        print (mymodules.Daten_CPU())                                               #Auf Modul zugreifen
        continue
    if befehl == 4:
        print (mymodules.Datenbank_erstellen())                                     #Auf Modul zugreifen
        continue
    if befehl == 5:
        print (mymodules.Datenbank_löschen())                                       #Auf Modul zugreifen
        continue
sys.exit(0)
