import os
from tkinter import N



def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def init_counties():
    counties = []
    with open("county.txt", "r", encoding="utf-8") as file:
        for line in file:
            atr = line.split(",")
            counties.append(County(atr[0],float(atr[1])))
    return counties


def meny():
    yes=input(f"Do you need help with any thing els?")
    if "y" in yes:
        clearconsole()
        print("""
    [1]geting out your taxes baste on your county 
    [2]pay taxes
    [3]if you dont need anything, write '#' """)
    else:
        print(f"Very well, see you next time {name}")
        quit()
    message = input("Here can you write what you would like to have help with: ")
    counties = init_counties()
    if "1" in message:
        print(f"okay that we can help you with. If you want in the end you can fill out a form to help us to bee bettre. Tanks.")
        nille = Citizen("Nille")
        nille.municipality_procent(counties)
    elif "2" in message:
        pass
    elif "#" in message:
        form = input("do you want to fill out a form to custemer survice? (y/n)")
        if "y" in form:
            forms()
            quit()
        else:
            print(f"Very well, see you next time {name}")
            quit()

def forms():
    with open("service.txt", "a", encoding="utf-8") as s:
        print("press ENTER to move on")
        s.write(input("How was your experiens? "))
        s.write(input("Did you have any problems? "))
        s.write(input("What was your problem? "))
        s.write(input("How can we do bettre?"))
        print("Thank you for your suport we will take it to consideration.")
        

class County:
    def __init__(self, name, percentage) -> None:
        self.name = name
        self.percentage = percentage


class Citizen:
    def __init__(self, name) -> None:
        self.name = name
        self.county = ""

    #def memori(self):
        #with open("memorys.txt", "w", encoding="utf-8") as mems:
        #r-read
        #x-create, får error om filen finns
        #w-write, radera det som fanns
        #a-append, skapa om inte existera.
            #print("mata in alla elever i inf20,skriv # om du vill avsluta")
        #while True:
        #    elev= input("elev: ")
         #   if "#" in elev:
          #      break
           # else:
            #    mems.write(f"{elev}\n")
   # with open("memorys.txt", "r", encoding="utf8") as mems:
    #    print("elever in inf20")
     #   for elev in mems.readlines():
      #      print(elev, end="")
            

    def municipality_procent(self, counties):
        with open("persanol_information.txt", "a", encoding="utf-8") as p:
            while True:
                county = input("in what municipality do you work at?")
                for c in counties:
                    if c.name == county.lower():
                        self.county = c
                        p.write(county)
                        p.close()
                        self.procent_municipality()
                        
                        break
                    else:
                        print("you need to put in what municipality you work at (in stockholms county ).")
                

    def procent_municipality(self):
        with open("persanol_information.txt", "a", encoding="utf-8") as p:
            salary = int(input("how much do you earn?"))
            överskatt = 504000/12 #42 000kr
            åverskatt = 703000/12 #58 583kr
            if salary <= överskatt:
                p.write(print(f"this is how much you need to pay:{salary*self.county.percentage}"))
                meny()
                p.write(salary)
                p.close()
            
            elif salary > överskatt and salary <= åverskatt:
                överskatt1= salary - överskatt
                överskatt2=överskatt1*0.5
                p.write.str((print(f"this is how much you need to pay:{överskatt*self.county.percentage + överskatt2}")))
                meny()
                #42000*0,3051= 12814,2
                #3000*0,5=1500
                #14314,2
            elif salary > åverskatt:
                åverskatt1 = salary - åverskatt
                åverskatt2 = åverskatt1*0.55
                p.write(print(f"this is how much you need to pay:{åverskatt*self.county.percentage + åverskatt2}"))
                meny()
            #fortsätta med att skapa metod till att ta kommun och lön för att räkna ut.

def main():
    global name
    with open("persanol_information.txt", "a", encoding="utf-8") as p:
        name=input("Hi what is your name: ")
        print(f"Hi {name}, welcome to the tax authorities, how can we be at your service today?") 
        print(f"""
        [1]geting out your taxes baste on were you work
        [2]pay taxes""")
        message = input("Here can you write what you would like to have help with: ")
        counties = init_counties()
        if "1" in message:
            print(f"okay that we can help you with. If you want in the end you can fill out a form to help us to bee bettre. Tanks.")
            nille = Citizen("Nille")
            nille.municipality_procent(counties)
        elif "2" in message:
            pass
    p.write(name, message)


if __name__=="__main__":
    main()