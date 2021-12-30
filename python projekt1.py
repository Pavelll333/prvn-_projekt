


TEXTS = ['''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive topographic 
feature that rises sharply some 1000 feet above 
Twin Creek Valley to an elevation of more than 7500 
feet above sea level. The butte is located just north 
of US 30N and the Union Pacific Railroad, which traverse the valley.''',
'''At the base of Fossil Butte are the bright red, 
purple, yellow and gray beds of the Wasatch Formation. 
Eroded portions of these horizontal beds slope 
gradually upward from the valley floor and steepen 
abruptly. Overlying them and extending to the top 
of the butte are the much steeper buff-to-white beds 
of the Green River Formation, which are about 300 feet thick.''',
'''The monument contains 8198 acres and 
protects a portion of the largest deposit 
of freshwater fish fossils in the world. 
The richest fossil fish deposits are found 
in multiple limestone layers, which lie 
some 100 feet below the top of the butte. 
The fossils represent several varieties 
of perch, as well as other freshwater 
genera and herring similar to those 
in modern oceans. Other fish such as 
paddlefish, garpike and stingray 
are also present.''']


uzivatel = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
cara = "-" *60

jmeno = input("Zadej jméno: ")
heslo = input("Zadej heslo: ")
print(cara)

if uzivatel.get(jmeno) == heslo:
    print("Vítel v aplikaci analyzování textu,", jmeno.title())
else:
    print("Neregistrovaný uživatel, program se ukončí!")
    exit()

cislo_textu = print("Mám tady pro teba 3 texty k analyzování.")
print(cara)
cislo_textu = (input("Zadej číslo 1 - 3: "))
print(cara)

if cislo_textu.isdigit() and cislo_textu >= "1"  and cislo_textu <= "3":
    text = (TEXTS[int(cislo_textu) -1])
else:
    print("Zadaná hodnota není číslo nebo je mimo rozsah, ukončuji program!")
    exit()


list_text = text.split(" ")
#print(list_text)
print("V textu je celkem:", (len(list_text)),"slov")

prvniVelke = 0
vseVelke = 0
vseMale = 0
jeCislo = 0
soucetCisel = 0

for slovo in list_text:
    if slovo.istitle():
        prvniVelke = (prvniVelke + 1)
    elif slovo.isupper():
        vseVelke = (vseVelke + 1)
    elif slovo.islower():
        vseMale = (vseMale +1)
    else:
        slovo.isnumeric()
        jeCislo = (jeCislo + 1)
        soucetCisel = ((soucetCisel) + int(slovo))


print("V textu je:",(prvniVelke),"slov, která začínají velkým písmenem")
print("V textu je:",(vseVelke), "slov, která jsou celá velká")
print("V textu je:",(vseMale),"slov, která jsou napsána malými písmeny")
print("V textu je:",(jeCislo),"slov, která jsou čísla")
print("Součet všech čísel v textu je:",(soucetCisel))

print(cara)

delkaSlov = list()

for slovo in list_text:
    delkaSlov.append(len(slovo))

nejdelsi = max(delkaSlov)
print("DELKA |       PŘÍPARDY     |POČET")
print(cara)
for i in (range(1,nejdelsi +1)):
    a = ("*" * ((delkaSlov).count(i)))
    b = ((delkaSlov).count(i))
    print(f"{i:>5} | {a:<18} | {b}")
    i = (i +1)















