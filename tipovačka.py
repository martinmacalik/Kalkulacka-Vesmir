import random

hodit_znova = "ano"

print("Vítej, vyzkoušíš jestli dokážeš uhodnou na jakou stranu dopadne  hrací kostka? ")

while hodit_znova == "ano" or hodit_znova == "a":

    vstup = input("Napiš číslo strany od 1 do 6: ")

    kostka = ["1", "2", "3", "4", "5", "6"]
    hod = random.choice(kostka)

    print(hod)

    if vstup == hod:
        print("Wow! Tvoje štěstí je fakt dobré.")
    else:
        print("Nevadí netrefil jsi se, zkus to znova.")

    hodit_znova = input("Hodit znova? (a/n) ")

if hodit_znova == "ne" or hodit_znova == "n":
    print("Děkuji že sis zahrál tipovačku!")
    ukoncit = input("Ukončíš stisknutím libovolné klávesy.")
