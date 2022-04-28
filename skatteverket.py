import os
from unicodedata import name
class County:
    def __init__(self, name, percentage) -> None:
        self.name = name
        self.percentage = percentage


class Citizen:
    def __init__(self, name) -> None:
        self.name = name
        self.county = ""
    def memori(self):
        with open("memorys.txt", "w", encoding="utf8") as mems:
        #r-read
        #x-create, får error om filen finns
        #w-write, radera det som fanns
        #a-append, skapa om inte existera.
            print("mata in alla elever i inf20,skriv # om du vill avsluta")
        while True:
            elev= input("elev: ")
            if "#" in elev:
                break
            else:
                mems.write(f"{elev}\n")

    with open("memorys.txt", "r", encoding="utf8") as mems:
        print("elever in inf20")
        for elev in mems.readlines():
            print(elev, end="")
            

    def municipality_procent(self, counties):
        self.memori()
        while True:
            county = input("in what municipality do you work at?")
            for c in counties:
                if c.name == county.lower():
                    self.county = c
                    self.procent_municipality()
                    break
                else:
                    print("you need to put in what municipality you work at (in stockholms county ).")

    def procent_municipality(self):
        salary = int(input("how much do you earn?"))
        överskatt = 504000/12
        åverskatt = 703000/12
        if salary <= överskatt:
            print(f"this is how much you need to pay:{salary*self.county.percentage}")
                    
        
        elif salary > överskatt <= åverskatt:
            överskatt1= salary - överskatt
            överskatt2=överskatt1*0.5
            print(f"this is how much you need to pay:{överskatt2*self.county.percentage + överskatt1}")
            
            #42000*0,3051= 12814,2
            #3000*0,5=1500
            #14314,2
        elif salary > åverskatt:
            åverskatt1 = salary - åverskatt
            åverskatt2 = åverskatt1*0.55
            print(f"this is how much you need to pay:{åverskatt2*self.county.percentage + åverskatt2}")
            
        #fortsätta med att skapa metod till att ta kommun och lön för att räkna ut.

def input_county():
    # Öppna fil med counties
    # Be användaren mata in en kommun som finns
    # Om den finns, returnera rätt kommun

    return input_county

def init_counties():
    counties = []
    with open("county.txt", "r", encoding="utf-8") as file:
        for line in file:
            atr = line.split(",")
            counties.append(County(atr[0],float(atr[1])))
    return counties

def main():
    name=input("hi what is your name: ")
    print(f"""Hi {name}, welcome to the tax authorities, how can we be at your service today? 
    We can help you with ether geting out your taxes baste on your county or 
    pay taxes 
    """)
    message = input("Here can you write what you would like to have help with: ")
    counties = init_counties()
    if "taxes" in message:
        print(f"okay {name} that we can help you with. If you want in the end you can fill out a form to help us to bee bettre. Tanks.")
        nille = Citizen("Nille")
        nille.municipality_procent(counties)

    # TODO:
    # - Fråga om kommun.
    # - Fråga om lön.
    # - Skapa Skatte-objekt med dessa två attribut


    

        



if __name__=="__main__":
    main()