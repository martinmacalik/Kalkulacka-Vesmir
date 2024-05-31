import random

znova = "ano" or "a"

while znova == "ano" or znova == "a":

    veta = input("Zadej tvoji větu a já ti vyvěštím odpověď: ")

    vestba = ["A", "B", "C", "D", "F", "G", "H", "I", "J"]
    odpoved = random.choice(vestba)

    if odpoved == "A":
        print("Určitě ano.")
    elif odpoved == "B":
        print("Určitě ne.")
    elif odpoved == "C":
        print("Ano, ale nikomu to neříkej.")
    elif odpoved == "D":
        print("Zatím ne.")
    elif odpoved == "E":
        print("Dříve ne.")
    elif odpoved == "F":
        print("Ne, když jsi přítomna/en.")
    elif odpoved == "G":
        print("Pokud chceš.")
    elif odpoved == "H":
        print("Ano i ty.")
    elif odpoved == "I":
        print("Trochu.")
    else:
        print("Moc.")

    znova = input("Chceš věštit dále?Je nebezpečné věštit moc často. (a/n) ")

if znova == "ne" or znova == "n":
    print("Děkuji za použití.")

konec = input("Ukončíš stisknutím libovolné klávesy.")