import random

def tarot():
    print("\nPřišli jste k opuštěnému tábořišti, nikdo kromě vás tady není.")
    print("Jde vidět sada Tarot karet na stolu, Co uděláš?")
    print("1 = Nechat je být")
    print("2 = Zkusit je")
    volba = str(input())
    if volba == "1":
        print("Rozhodli jste se karty nezkusit, ale na chvíli jste si odpočinuli předtím, než jste odešli. Získáváš 1 bod za odpočinek.")
        return 1
    elif volba == "2":
        print("Rozhodli jste si karty zamíchat a pak si jednu náhodně vzít.")
        tarotCards = {
            0: ["Blázen", "nové počátky."],
            1: ["Kouzelník", "dost síli pokračovat dále."],
            2: ["Nejvyšší kněžka", "klíč k podvědomí."],
            3: ["Císařovna", "péči a hojnost."],
            4: ["Císař", "autoritu."],
            5: ["Velekněz", "náboženství a konformitu."],
            6: ["Milenci", "lásku."],
            7: ["Válečný vůz", "sílu vůle a odhodlání."],
            8: ["Síla", "sílu a odvahu."],
            9: ["Poustevník", "být osamoťe, ale zvládat to."],
            10: ["Kolo štěstí", 'pořekadlo "co se stane, se stane".'],
            11: ["Spravedlnost", "spravedlnost a pravdu."],
            12: ["Oběšenec", "pauzu nebo vzdávání se."],
            13: ["Smrt", "konce."],
            14: ["Střídmost", "balanc a trpělivost."],
            15: ["Ďábel", "závislost a uvěznění."],
            16: ["Věž"],
            17: ["Hvězda", "naději."],
            18: ["Měsíc", 'iluzi.'],
            19: ["Slunce", "positivitu a spokojenost."],
            20: ["Poslední soud", "znovuzrození a vnitřní volání."],
            21: ["Svět", "dokončení."]
        }
        randomNum = random.randint(0, 21)
        if randomNum == 16:
            print('Vybrali jste si kartu číslo 16, neboli "Věž", což většinou symbolizuje nějakou katastrofu ve vašem životě.')
            print("Přitom co jste vracely karty zpátky tam kde byli, tak udeřil meteorit do země, který vás okamžitě zabil. Hra končí.")
            return -1
        else:
            if randomNum != 12:
                print(f"Vybrali jste si kartu číslo {randomNum}, neboli {tarotCards[randomNum][0]}, což většinou symbolizuje {tarotCards[randomNum][1]} Získáváš 2 body.")
                return 2
            else:
                print(f"Vybrali jste si kartu číslo {randomNum}, neboli {tarotCards[randomNum][0]}, což většinou symbolizuje {tarotCards[randomNum][1]} Získáváš 0 bodů.")
            return 0
    else:
        print("Neplatná volba, ale přišla vám zprává toho, že mám v oblasti tábořiště brzo spadnout meteorit, takže rychle odejdete. Získáváš 0 bodů.")
        return 0
    
def vez():
    print("\nDorazil jsi do tajemné věže. Na schodišti blikají svíčky.")
    volba = input("Vidíš starou knihu na stole. Co uděláš? (1 = Otevřít knihu, 2 = Ignorovat ji): ")
    if volba == "2":
        print("Ignoruješ knihu a pokračuješ dál. Získáváš 1 bod za klid.")
        return 1
    elif volba == "1":
        print("Kniha obsahuje magické kouzlo! Získáváš 3 body.")
        return 3
    else:
        print("Neplatná volba, díky kouzlu jsi vyvolal temnotu. Hra končí.")
        return -3
    
vez()
