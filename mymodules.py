"""
    Funktionen zum Auslesen der CPU- und RAM-
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
"""------------------------------------------------------------Funktionen------------------------------------------------------------------------------------"""
def Daten_abspeichern():
        #Verbindung prüfen
        while 1:
                try:
                        conn = mysql.connector.connect(user="root",host= "localhost", database="abgabe")
                        print("Verbindung hergestellt")
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                return("Etwas ist falsch mit dem user name oder password")
                                break
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                return("Datenbank existiert nicht! Bitte Befehl 4 ausführen!")
                                break
                        else:
                                return(err)
                                break
                else:
                        cursor = conn.cursor()
                        print( "(1) erstes Gerät")                                                          # Menü und Benutzerauswahl
                        print( "(2) zweites Gerät")
                        print( "(0) Zurück zum Hauptmenü")
                        abfrage = int(input( "Auswahl: "))
                    
                        if( abfrage < 0 or abfrage > 2):                                                    # Testen, ob ein bekannter Befehl eingegeben wurde
                                print( "Unbekannter Befehl: " + str(abfrage))
                                print( "")
                                continue

                        if abfrage == 0:
                                return ("... Sie befinden sich jetzt im Hauptmenü")
                                break

                        if abfrage == 1:
                                with open("datenspeicher.csv", 'w', newline='') as csvfile:

                                        # CSV-Writer anlegen, Kopfzeile schreiben
                                        csvwriter = csv.writer(csvfile, delimiter=',')
                                        csvwriter.writerow(['TIMESTAMP', 'CPU', 'RAM', 'GERÄT'])

                                        #Kopfzeile der Bildschirmausgabe
                                        print("ZEITSTEMPEL \t\t CPU [%]\t RAM [%]\t GERÄT")

                                        try:
                                                while True:
                                                        # Zeit und Auslastung ermitteln
                                                        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                                        cpu = psutil.cpu_percent(1)
                                                        ram = psutil.virtual_memory().percent
                                                        gerät = 1
                                    
                                                        # Daten in CSV schreiben 
                                                        csvwriter.writerow(["\'"+time+"\'",cpu,ram,gerät])
                                                        # Daten in MYSQL schreiben
                                                        mydb = mysql.connector.connect(user="root",host= "localhost",database="abgabe")
                                                        mycursor = mydb.cursor()
                                                        mycursor.execute("""INSERT INTO ergebnisse VALUES ("%s","%s","%s","%s")""",(time, cpu, ram, gerät))
                                                        mycursor.close()
                                                        mydb.commit()
                                                    
                                                        # Bildschirmausgabe
                                                        print(time,"\t",cpu,"\t\t",ram,"\t\t",gerät)
                                            
                                        except KeyboardInterrupt:
                                                print("... Abbruch!")

                                mydb.close()
                                return ("Daten gesichert")
                                break
                        if abfrage == 2:
                                with open("datenspeicher.csv", 'w', newline='') as csvfile:
                                        # CSV-Writer anlegen, Kopfzeile schreiben
                                        csvwriter = csv.writer(csvfile, delimiter=',')
                                        csvwriter.writerow(['TIMESTAMP', 'CPU', 'RAM', 'GERÄT'])

                                        #Kopfzeile der Bildschirmausgabe
                                        print("ZEITSTEMPEL \t\t CPU [%]\t RAM [%]\t GERÄT")

                                        try:
                                                while True:
                                                        
                                                        # Zeit und Auslastung ermitteln
                                                        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                                        cpu = psutil.cpu_percent(1)
                                                        ram = psutil.virtual_memory().percent
                                                        gerät = 2
                                                    
                                                        # Daten in CSV schreiben 
                                                        csvwriter.writerow(["\'"+time+"\'",cpu,ram,gerät])
                                                        # Daten in MYSQL schreiben
                                                        mydb = mysql.connector.connect(user="root",host= "localhost",database="abgabe")
                                                        mycursor = mydb.cursor()
                                                        mycursor.execute("""INSERT INTO ergebnisse VALUES ("%s","%s","%s","%s")""",(time, cpu, ram, gerät))
                                                        mycursor.close()
                                                        mydb.commit()
                                                    
                                                        # Bildschirmausgabe
                                                        print(time,"\t",cpu,"\t\t",ram,"\t\t",gerät)
                                                    
                                        except KeyboardInterrupt:
                                                print("... Abbruch!")

                                mydb.close()
                                return ("Daten gesichert")
                                break
                        
def Daten_RAM():
        #Verbindung prüfen
        while 1:
                try:
                        conn = mysql.connector.connect(user="root",host= "localhost", database="abgabe")
                        print("Verbindung hergestellt")
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                return("Etwas ist falsch mit dem user name oder password")
                                break
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                return("Datenbank existiert nicht! Bitte Befehl 4 ausführen!")
                                break
                        else:
                                return(err)
                                break
                else:
                        cursor = conn.cursor()
                        #Auf Gerät 1 zugreifen
                        mydb = mysql.connector.connect(user="root",host= "localhost",database="abgabe")
                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT MIN(ram),MAX(ram),AVG(ram)FROM ergebnisse WHERE gerät = '1'")
                        myresult = mycursor.fetchall()
                        print("MIN  MAX  Durschnitt  von Gerät 1")
                        for i in myresult:
                                print(i[0],i[1],i[2])
                        mycursor.close()
                        mydb.close()
                            #Auf Gerät 2 zugreifen
                        mydb = mysql.connector.connect(user="root",host= "localhost",database="abgabe")
                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT MIN(ram),MAX(ram),AVG(ram)FROM ergebnisse WHERE gerät = '2'")
                        myresult = mycursor.fetchall()
                        print("MIN  MAX  Durschnitt  von Gerät 2")
                        for i in myresult:
                                print(i[0],i[1],i[2])
                        mycursor.close()
                        mydb.close()
                            #Auf alle Geräte zugreifen
                        mydb = mysql.connector.connect(user="root",host= "localhost",database="abgabe")
                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT MIN(ram),MAX(ram),AVG(ram)FROM ergebnisse")
                        myresult = mycursor.fetchall()
                        print("MIN  MAX  Durschnitt  von allen Geräten")
                        for i in myresult:
                                print(i[0],i[1],i[2])
                        mycursor.close()
                        mydb.close()
                        return("Daten ausgelesen")
def Daten_CPU():
        #Verbindung prüfen
        while 1:
                try:
                        conn = mysql.connector.connect(user="root",host= "localhost", database="abgabe")
                        print("Verbindung hergestellt")
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                return("Etwas ist falsch mit dem user name oder password")
                                break
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                return("Datenbank existiert nicht! Bitte Befehl 4 ausführen!")
                                break
                        else:
                                return(err)
                                break
                else:
                        cursor = conn.cursor()
                        #Auf Gerät 1 zugreifen
                        mydb = mysql.connector.connect(user="root",host= "localhost",database="abgabe")
                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT MIN(cpu),MAX(cpu),AVG(cpu)FROM ergebnisse WHERE gerät = '1'")
                        myresult = mycursor.fetchall()
                        print("MIN MAX Durschnitt  von Gerät 1")
                        for i in myresult:
                                print(i[0],i[1],i[2])    
                        mycursor.close()
                        mydb.close()
                        #Auf Gerät 2 zugreifen
                        mydb = mysql.connector.connect(user="root",host= "localhost",database="abgabe")
                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT MIN(cpu),MAX(cpu),AVG(cpu)FROM ergebnisse WHERE gerät = '2'")
                        myresult = mycursor.fetchall()
                        print("MIN MAX Durschnitt  von Gerät 2")
                        for i in myresult:
                                print(i[0],i[1],i[2])    
                        mycursor.close()
                        mydb.close()
                        #Auf alle Geräte zugreifen
                        mydb = mysql.connector.connect(user="root",host= "localhost",database="abgabe")
                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT MIN(cpu),MAX(cpu),AVG(cpu)FROM ergebnisse")
                        myresult = mycursor.fetchall()
                        print("MIN MAX Durschnitt  von allen Geräten")
                        for i in myresult:
                                print(i[0],i[1],i[2])    
                        mycursor.close()
                        mydb.close()
                        return("Daten ausgelesen")
def Datenbank_erstellen():
        while 1:
                try:
                        conn = mysql.connector.connect(user="root",host= "localhost")
                        print("Verbindung hergestellt")
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                return("Etwas ist falsch mit dem user name oder password")
                                break
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                return("Datenbank existiert nicht! Bitte Befehl 4 ausführen!")
                                break
                        else:
                                return(err)
                                break
                else:
                        cursor = conn.cursor()
                        #Datenbank löschen wenn sie bereits existiert
                        mydb = mysql.connector.connect(user="root",host= "localhost")
                        mycursor = mydb.cursor()
                        mycursor.execute("drop DATABASE if exists abgabe")
                        mycursor.close()
                        mydb.close()
                        print ("Datenbank gelöscht")
                        #Datenbank anlegen
                        mydb = mysql.connector.connect(user="root",host= "localhost")
                        mycursor = mydb.cursor()
                        mycursor.execute("CREATE DATABASE if not exists abgabe")
                        mycursor.close()
                        mydb.close()
                        print ("Datenbank angelegt")
                        #Tabelle anlegen
                        mydb = mysql.connector.connect(user="root",host= "localhost", database="abgabe")
                        mycursor = mydb.cursor()
                        mycursor.execute("CREATE TABLE ergebnisse (TIMESTAMP text, CPU float, RAM float, GERÄT int )")
                        mycursor.close()
                        mydb.close()
                        print ("Tabelle angelegt")
                        return ("Sie können jetzt Ihre Daten mit Befehl 1 absichern")
def Datenbank_löschen():
        while 1:
                try:
                        conn = mysql.connector.connect(user="root",host= "localhost", database="abgabe")
                        print("Verbindung hergestellt")
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                return("Etwas ist falsch mit dem user name oder password")
                                break
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                return("Datenbank existiert nicht! Bitte Befehl 4 ausführen!")
                                break
                        else:
                                return(err)
                                break
                else:
                        cursor = conn.cursor()
                        #Datenbank löschen
                        mydb = mysql.connector.connect(user="root",host= "localhost")
                        mycursor = mydb.cursor()
                        mycursor.execute("drop DATABASE if exists abgabe")
                        mycursor.close()
                        mydb.close()
                        return ("Datenbank gelöscht")
"""def Datenbank_verbindung():
        while 1:
                try:
                        conn = mysql.connector.connect(user="root",host= "localhost", database="abgabe")
                        print("Verbindung hergestellt")
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                return("Etwas ist falsch mit dem user name oder password")
                                break
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                return("Datenbank existiert nicht! Bitte Befehl 4 ausführen!")
                                break
                        else:
                                return(err)
                                break
                else:
                        cursor = conn.cursor()
                        return (" ")>>>"""

    
    

