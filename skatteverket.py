
class County:
    def __init__(self, name, percentage) -> None:
        self.name = name
        self.percentage = percentage


class Citizen:
    def __init__(self, name) -> None:
        self.name = name

    def municipality_procent(self, counties):
        county = input("what municipality do you work at?")
        for c in counties:
            if c.name == county.capitalize():
                break
            self.procent_municipality(c)
                
                
        else:
            print("you need to put in what municipality you work at (in stockholms county ).")

    def procent_municipality(self, county):
        
        salary = int(input("how much do you earn?"))
        print(f"this is how much you need to pay:{salary*county.percentage}")

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
            counties.append(County(atr[0],atr[1]))
    return counties

def main():
    print("Hi and welcome to Skattevärket!! How can i help you?")
    counties = init_counties()
    meny=input("""
    get out your taxes baste on your county (the first one)
    pay taxes (the secound one)
    """)
    if "the first one" in meny:
        nille = Citizen("Nille")
        nille.municipality_procent(counties)

    # TODO:
    # - Fråga om kommun.
    # - Fråga om lön.
    # - Skapa Skatte-objekt med dessa två attribut


    

        



if __name__=="__main__":
    main()