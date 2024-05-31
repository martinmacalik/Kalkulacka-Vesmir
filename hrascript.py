print("Vítej v mojem kvízu, jestli projdeš všemi otázkam, tak jsi rozený chytrák.")
spravne = 0
otazky = 6

dohral = 1

ans = input("Jsi připravenej hrát? ")
if ans.lower() == "ano":

    ans = input("Kolik má žirafa krčních obratlů?")
    if ans.lower() == "7" or ans.lower() == "stejně jako lidé":
        spravne += 1
        print("Správně")
    else:
        print("Špatně")

    ans = input("Kdo řekl že e=mc2 ?")
    if ans.lower() == "einstein":
        spravne += 1
        print("Správně")
    else:
        print("Špatně")

    ans = input("Jak se jmenuje nejvyšší vrchol Orlických hor?")
    if ans.lower() == "velká deštná":
        spravne += 1
        print("Správně")
    else:
        print("Špatně")

    ans = input("Nejvetší město státu Louisiana se rozkládá do Mexického zálivu. O které město se jedná?")
    if ans.lower() == "new orleans":
        spravne += 1
        print("Správně")
    else:
        print("Špatně")

    ans = input("Kdo hrál v hlavní roli ve filmu The Gray Man?")
    if ans.lower() == "ryan gosling":
        spravne += 1
        print("Správně")
    else:
        print("Špatně")

    ans = input("Kolik let dlouhé, je funkční období soudce Ústavního soudu?")
    if ans.lower() == "10" or ans.lower() == "deset":
        spravne += 1
        print("Správně")
    else:
        print("Špatně")
elif ans.lower() == "ne":
    print("Tak já počkám no, až budeš připraven, tak zapni program znova.")
    dohral = 2

else:
    print("špatně zadaný vstup, zkus zadat ano nebo ne")
    dohral = 2

if dohral == 1:
    print("Děkuji za hraní mojeho kvízu, uhodl jsi", spravne, "otázky/ek správně!")
    skore = (spravne / otazky) * 100

    print("Tvoje skóre je", skore, "bodů.")
    print("Ahooooooooj!!!")

konec = input("Ukončíš libovolnou klávesou.")