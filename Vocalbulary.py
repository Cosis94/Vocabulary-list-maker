from ntpath import join
from Hiragana import Hiragana_low, Hiragana_up
from Katagana import Katagana
import csv

if __name__=="__main__":

    #for key, value in Hiragana_up.items():         #Test, ob auch kein Fehler in Dictionary ist
    #    print(key, ":",  value)

    #def get_key(val):                              #Funktion, um Key von Value zu bekommen bsp: get_key("ni") => に
    #    for key, value in Hiragana_low.items():
    #        if val == value:
    #            print(key)
    Liste = []
    class Vacabulary():
        def __init__(self, Input_G, Input_R):
            self.Input_G = Input_G
            self.Input_R = Input_R

        def Ausgabe(self):
            string = self.Input_R
            string = str(string)
            string = string.split(" ")
            List_length = len(string)
            length = 0
            Output_List = []

            while length < List_length:
                for key, value in Hiragana_low.items():
                        if value == string[length]:
                            Output_List.append(key)
                length = length+1
            
            new = [''.join(Output_List[:])]
            print(Output_List, new)
            Liste.append(new)
    

    class CSV_data():

        def __init__(self, filename):
            self.filename = filename
        
        def create_file(self):
            with open(self.filename, "w", newline='') as f:
                fieldnames = ["Deutsch", "Romanji", "Japanisch"]
                self.creator = csv.DictWriter(f, fieldnames=fieldnames)
                self.creator.writeheader()
                
        
        def Inputer(self):
            with open(self.filename, "a", newline='') as f:
                Eins = [str("Fatih"),",",str("Zekiye"),",",str("Fettah"),"\n"]
                Eins = "".join(Eins)
                f.write(Eins)



    fatih = Vacabulary("spät","o so i")
    fatih.Ausgabe()

    Csv_one = CSV_data("Eins.csv")
    #Csv_one.create_file()
    Csv_one.Inputer()
    

#Ziel Funktion für erstellen von Csv Datei
#Vokabeln in csv Datei einschreiben
#Csv Datei solange füllen bis beendet, dann neue Csv Datei erstellen können


