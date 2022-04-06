

class Skatteverket:
    def __init__(self, kommun, lön ) -> None:
        self.kommun = kommun
        self.lön = lön

    def county_procent(self):
        while True:
            county = input("what county do you work at?")
            with open("county.txt", "r", "UTF-8") as f:
                lines = f.readlines()
                if county in lines:
                    print("so you live there.")
                    self.procent_county()
                    break
                else:
                    print("you need to put in what county you work at.")

    def procent_county(self):
        procent = input("how much do you earn?")
        print("this is how much you need to pay")
        with open("county.txt", "r", "UTF-8") as g:
            line = g.readlines()
            


            
                

        #fortsätta med att skapa metod till att ta kommun och lön för att räkna ut.

def input_county():
    # Öppna fil med counties
    # Be användaren mata in en kommun som finns
    # Om den finns, returnera rätt kommun

    return county
    

def main():
    print("Hi and welcome to Skattevärket!! How can i help you?")
    meny=input("""
    get out your taxes baste on your county (the first one)
    pay taxes (the secound one)
    """)
    if "the first one" in meny:
        Skatteverket.county_procent()

    # TODO:
    # - Fråga om kommun.
    # - Fråga om lön.
    # - Skapa Skatte-objekt med dessa två attribut

    county = input_county()
    salary = int(input("What is your salary? "))

    user = Skatteverket(county, salary)
    user.calculate_treasure()
    

        



__name__=="__main__"
main()