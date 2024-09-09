import sys
import time
import matplotlib.pyplot as plt


vypujcene_knihy = ["1984", "Nesnesitelná lehkost bytí", "Na cestě", "Malý princ", "Anna Karenina", "Sto roků samoty"]
uzivatele = ["Kuba", "Petr", "Lucie", "Jana", "Marie", "Tom"]
vypujcene_knihy_dict = {
    "vypujcka_1": {
        "Jméno": "Kuba",
        "Kniha": ["1984"],
        "Datum": "04.09.2024"
    },

    "vypujcka_2": {
        "Jméno": "Petr",
        "Kniha": ["Nesnesitelná lehkost bytí"],
        "Datum": "13.08.2024"
    },

    "vypujcka_3": { 
        "Jméno": "Lucie",
        "Kniha": ["Na cestě"],
        "Datum": "31.08.2024"
    },

    "vypujcka_4": {
        "Jméno": "Jana",
        "Kniha": ["Malý princ"],
        "Datum": "22.07.2024"
    },

    "vypujcka_5": {
        "Jméno": "Marie",
        "Kniha": ["Anna Karenina"],
        "Datum": "08.08.2024"
    },

    "vypujcka_6": {
        "Jméno": "Tom",
        "Kniha": ["Sto roků samoty"],
        "Datum": "06.09.2024"
    }
}


uzivatele_knihy = {
    "Kuba": {
        "Jméno": "Kuba",
        "Identifikační číslo": "1",
        "Vypujcene_knihy": ["1984"]
    },

    "Petr": {
        "Jméno": "Petr",
        "Identifikační číslo": "2",
        "Vypujcene_knihy": ["Nesnesitelná lehkost bytí"]
    },

    "Lucie": {
        "Jméno": "Lucie",
        "Identifikační číslo": "3",
        "Vypujcene_knihy": ["Na cestě"]
    },

    "Jana": {
        "Jméno": "Jana",
        "Identifikační číslo": "4",
        "Vypujcene_knihy": ["Malý princ"]
    },

    "Marie": {
        "Jméno": "Marie",
        "Identifikační číslo": "5",
        "Vypujcene_knihy": ["Anna Karenina"]
    },

    "Tom": {
        "Jméno": "Tom",
        "Identifikační číslo": "6",
        "Vypujcene_knihy": ["Sto roků samoty"]
    }
}

books_list = [
    "Válka s mloky", 
    "Krysař", 
    "Nesnesitelná lehkost bytí", 
    "Zločin a trest",
    "1984", 
    "Srdce temnoty", 
    "Cesta", 
    "Na cestě", 
    "Velký Gatsby", 
    "Malý princ", 
    "Hobit", 
    "Sto roků samoty", 
    "Jméno růže", 
    "Anna Karenina",
    "Mechanický pomeranč"
]

books_dict = {
    "Válka s mloky":{
        "Název": "Válka s mloky",
        "Autor": "Karel Čapek",
        "ISBN": "978-80-87950-41-8",
        "Dostupnost": True      
    },

    "Krysař":{
        "Název": "Krysař",
        "Autor": "Viktor Dyk",
        "ISBN": "978-80-7287-267-1",
        "Dostupnost": True   
    },

    "Nesnesitelná lehkost bytí":{
        "Název": "Nesnesitelná lehkost bytí",
        "Autor": "Milan Kundera",
        "ISBN": "978-80-7108-351-1",
        "Dostupnost": False   
    },

    "Zločin a trest":{
        "Název": "Zločin a trest",
        "Autor": "Fjodor Michajlovič Dostojevskij",
        "ISBN": "978-80-207-2164-8",
        "Dostupnost": True   
    },

    "1984": {
        "Název": "1984",
        "Autor": "George Orwell",
        "ISBN": "978-80-7335-647-7",
        "Dostupnost": False
    },

    "Srdce temnoty": {
        "Název": "Srdce temnoty",
        "Autor": "Joseph Conrad",
        "ISBN": "978-80-7363-307-3",
        "Dostupnost": True
    },

    "Cesta": {
        "Název": "Cesta",
        "Autor": "Cormac McCarthy",
        "ISBN": "978-80-257-2867-3",
        "Dostupnost": True
    },

    "Na cestě": {
        "Název": "Na cestě",
        "Autor": "Jack Kerouac",
        "ISBN": "978-80-257-2997-7",
        "Dostupnost": False
    },

    "Velký Gatsby": {
        "Název": "Velký Gatsby",
        "Autor": "Francis Scott Fitzgerald",
        "ISBN": "978-80-7335-889-1",
        "Dostupnost": True
    },

    "Malý princ": {
        "Název": "Malý princ",
        "Autor": "Antoine de Saint-Exupéry",
        "ISBN": "978-80-00-07302-6",
        "Dostupnost": False
    },

    "Hobit": {
        "Název": "Hobit",
        "Autor": "J.R.R. Tolkien",
        "ISBN": "978-80-257-1949-7",
        "Dostupnost": True
    },

    "Sto roků samoty": {
        "Název": "Sto roků samoty",
        "Autor": "Gabriel García Márquez",
        "ISBN": "978-80-207-2045-0",
        "Dostupnost": False
    },

    "Jméno růže": {
        "Název": "Jméno růže",
        "Autor": "Umberto Eco",
        "ISBN": "978-80-257-2435-4",
        "Dostupnost": True
    },

    "Anna Karenina": {
        "Název": "Anna Karenina",
        "Autor": "Lev Nikolajevič Tolstoj",
        "ISBN": "978-80-7547-617-3",
        "Dostupnost": False
    },

    "Mechanický pomeranč": {
        "Název": "Mechanický pomeranč",
        "Autor": "Anthony Burgess",
        "ISBN": "978-80-207-2082-5",
        "Dostupnost": True
    }
}




while True:
    otazka = int(input("Vítej v mém programu, kde si můžeš spravovat svoji knihovnu, Co chceš zvolit? (Napiš číslo)\n1. Přidat knihu\n2. Odstranit knihu\n3. Registrovat nového uživatele\n4. Vyhledat knihu\n5. Vypůjčit knihu\n"))

    #1 Přidání knihy
    if otazka == 1:
        nazev_knihy = str(input("\nNapiš název knihy: "))
        if nazev_knihy in books_list:
            print("Taková kniha už je v naší databázi.\n")
            time.sleep(2)
            continue
        else:
            books_list.append(nazev_knihy)
            nove_knihy_detaily = {}
            nove_knihy_detaily["Název"] = nazev_knihy
            nove_knihy_detaily["Autor"] = str(input("Napiš jméno autora: "))
            nove_knihy_detaily["ISBN"] = str(input("Napiš ISBN: "))
            nove_knihy_detaily["Dostupnost"] = True
            books_dict[nazev_knihy] = nove_knihy_detaily
            print("Kniha byla úspěšně přidána.\n")
            time.sleep(2)
            continue


    #2 Odstranit knihu
    if otazka == 2:
        print("Toto jsou knihy, které máme v databázi:")
        print(', '.join(map(str, books_list)))
        odstranit_knihu = str(input("Jakou knihu si přeješ odstranit? "))
        if odstranit_knihu in books_list:
            books_list.remove(odstranit_knihu)
            del books_dict[odstranit_knihu]
            print("Kniha byla úspěšně odstraněna.\n")
            time.sleep(2)
            continue
        if odstranit_knihu not in books_list:
            print("Takovou knihu u nás nemáme.\n")
            time.sleep(2)
            continue


    #3 Registrovat nového uživatele
    if otazka == 3:
        jmeno = str(input("Napiš jméno nového uživatele: "))
        uzivatele.append(jmeno)
        nove_uzivatele_detaily = {}
        nove_uzivatele_detaily["Jméno"] = jmeno
        nove_uzivatele_detaily["Identifikační číslo"] = str(input("Napiš identifikační číslo: "))
        nove_uzivatele_detaily["Vypujcene_knihy"] = []
        if any(nove_uzivatele_detaily["Identifikační číslo"] == details["Identifikační číslo"] for details in uzivatele_knihy.values()):
            print("Takové identifikační číslo už je v naší databázi.\n")
            time.sleep(2)
        else:
            nove_uzivatele_detaily["Vypujcene_knihy"] = []
            uzivatele_knihy[jmeno] = nove_uzivatele_detaily
            print("Uživatel byl úspěšně přidán.\n")
            time.sleep(2)
            continue
            #     break

            # elif nove_uzivatele_detaily["Identifikační číslo"] not in uzivatele_knihy:
            #     nove_uzivatele_detaily["Vypujcene_knihy"] = []
            #     uzivatele_knihy[jmeno] = nove_uzivatele_detaily
            #     print("Uživatel byl úspěšně přidán.\n")
            #     time.sleep(2)
            #     continue
        
        # if nove_uzivatele_detaily["Identifikační číslo"] in uzivatele_knihy:
        #     print("Takové identifikační číslo už je v naší databázi.\n")
        #     time.sleep(2)
        #     continue



    #4 Vyhledat knihu
    if otazka == 4:
        vyhledavana_kniha = str(input("Jakou knihu hledáš? Chceš hledat podle názvu knihy nebo autora? (kniha/autor) "))
        if vyhledavana_kniha == "kniha":
            vyhledavana_kniha_podle_nazvu = str(input("Napiš název knihy: "))
            if vyhledavana_kniha_podle_nazvu in books_list:
                print("Tuto knihu máme v databázi.\n")
                time.sleep(1)
                if vyhledavana_kniha_podle_nazvu in vypujcene_knihy:
                    print("Je však vypůjčená.\n")
                    time.sleep(2)
                    continue
                if vyhledavana_kniha_podle_nazvu not in vypujcene_knihy:
                    print("Je k dispozici k zapůjčení.\n")
                    time.sleep(2)
                    continue
            if vyhledavana_kniha_podle_nazvu not in books_list:
                time.sleep(2)
                print("Takovou knihu u nás nevedeme.")
                continue

        if vyhledavana_kniha == "autor":
            vyhledavana_kniha_podle_autora = str(input("Napiš jméno autora: "))
            for key, value in books_dict.items():
                if vyhledavana_kniha_podle_autora in value.values():
                    print("Tuto knihu máme v databázi.\n")
                    time.sleep(1)
                    if key in vypujcene_knihy:
                        print("Je však vypůjčená.\n")
                        time.sleep(2)
                        continue
                    if key not in vypujcene_knihy:
                        print("Je k dispozici k zapůjčení.\n")
                        time.sleep(2)
                        continue
                if vyhledavana_kniha_podle_autora not in value.values():
                    time.sleep(2)
                    print("Nemáme u nás žádnou knihu od tohoto autora.")
                    break

    #5 Vypůjčit knihu
    if otazka == 5:
        knihy_k_dispozici = []
        for key, value in books_dict.items():
            if value.get("Dostupnost") == True:
                knihy_k_dispozici.append(key)

            if value.get("Dostupnost") == False:
                continue
        
        print("Zde jsou naše aktuální knihy k dispozici:")
        print(', '.join(knihy_k_dispozici))

        #Sloupcový graf

        autori_dostupne_knihy = {}

        for key, value in books_dict.items():
            if value.get("Dostupnost") == True:
                autor = value.get("Autor")
                if autor in autori_dostupne_knihy:
                    autori_dostupne_knihy[autor] += 1
                else:
                    autori_dostupne_knihy[autor] = 1

            # if value.get("Dostupnost") == False:
            #     autor = value.get("Autor")
            #     if autor in autori_dostupne_knihy:
            #         autori_dostupne_knihy[autor] = 0
            #     else:
            #         autori_dostupne_knihy[autor] = 0

        # Rozdělení dat do os X a Y
        x = list(autori_dostupne_knihy.keys())
        y = list(autori_dostupne_knihy.values())

        # Vytvoření sloupcového grafu
        plt.bar(x, y, color='blue', label='Počet dostupných knih')

        plt.xlabel('Autoři')
        plt.ylabel('Počet dostupných knih')
        plt.title('Počet dostupných knih podle autorů')
        plt.legend()
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Zobrazení grafu
        plt.show()






        x2 = list(uzivatele_knihy.keys())
        y2 = list(map(lambda x: len(x["Vypujcene_knihy"]), uzivatele_knihy.values()))

        # Vytvoření sloupcového grafu
        plt.bar(x2, y2, color='blue', label='Počet dostupných knih')

        plt.xlabel('Uživatelé')
        plt.ylabel('Počet vypůjčených knih')
        plt.title('Počet vypůjčených knih podle uživatelů')
        plt.legend()
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Zobrazení grafu
        plt.show()



        
        kniha = str(input("Jakou knihu chceš půjčit? "))
        if kniha in knihy_k_dispozici:
            jmeno = str(input("Jak se jmenuješ? "))
            if jmeno in uzivatele:
                vypujcene_knihy.append(kniha)
                for key, value in uzivatele_knihy.items():
                    if jmeno in value.values():
                        value["Vypujcene_knihy"].append(kniha)
                        books_dict[kniha]["Dostupnost"] = False
                        knihy_k_dispozici.remove(kniha)
                        print("Kniha byla úspěšně vypůjčena.\n")
                        time.sleep(2)
                        continue
                        

            if jmeno not in uzivatele:
                print("Takový uživatel u nás není zaregistrovaný.\n")
                time.sleep(2)
                continue

        elif kniha not in knihy_k_dispozici:
            print("Takovou knihu u nás nemáme k dispozici.\n")
            time.sleep(2)
            continue


    
                    
            


            