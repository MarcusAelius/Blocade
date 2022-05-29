import sys
import os
from termcolor import colored
import queue

red = 0
kolona = 0
pocenti_broj_zidova = 0
broj_zidova = []

igrac1 = []
igrac2 = []

odrediste1 = []
odrediste2 = []

horizontalni_zidovi = []
vertikalni_zidovi = []

pocinje_igru_igrac = None


def unos_dimenzija_table():
    print("Red: (6-26, paran broj) Kolona: (5-21, neparan broj)\n")
    global red, kolona, pocenti_broj_zidova, broj_zidova
    while True:
        red_unos = input("Unesite dimenziju table (broj redova): ")
        if not red_unos.isdigit():
            ocisti_zadnju_liniju_terminala()
            continue
        else:
            red_unos = int(red_unos)
        if red_unos < 4 or red_unos > 26 or red_unos % 2 == 1:
            ocisti_zadnju_liniju_terminala()
            continue
        else:
            ocisti_zadnju_liniju_terminala()
            break

    while True:
        kolona_unos = input("Unesite dimenziju table (broj kolona): ")
        if not kolona_unos.isdigit():
            ocisti_zadnju_liniju_terminala()
            continue
        else:
            kolona_unos = int(kolona_unos)
        if kolona_unos < 3 or kolona_unos > 21 or kolona_unos % 2 == 0:
            ocisti_zadnju_liniju_terminala()
            continue
        else:
            ocisti_zadnju_liniju_terminala()
            break

    pocenti_broj_zidova = ((red_unos + kolona_unos)//2 - 1)
    red = red_unos
    kolona = kolona_unos
    broj_zidova.append(pocenti_broj_zidova)
    broj_zidova.append(pocenti_broj_zidova)
    ocisti_terminal()
    stampaj_tablu()
#dobra
def unos_kordinata_figura():

    print("Protivnicke figure se postavljaju simetricno u odnosu na kordinate figura koje unosite!\n")
    broj_igraca = 2

    while True:
        if red < 10:
            x_unos = input(f"Unesite indeks reda u kome zelite da postavite figure (1-9): ")
        else:
            x_unos = input(f"Unesite indeks reda u kome zelite da postavite figure (1-9, a-{chr(red+87)}): ")

        if not ((x_unos.isalpha() and len(x_unos) == 1) or ((x_unos.isdigit() and len(x_unos) == 1))):
            ocisti_zadnju_liniju_terminala()
            continue
        else:

            if x_unos.islower():
                x_unos = ord(x_unos) - 87
            elif x_unos.isupper():
                x_unos = ord(x_unos) - 55
            elif x_unos.isdigit():
                x_unos = ord(x_unos) - 48

            if x_unos < 1 or x_unos > red:
                ocisti_zadnju_liniju_terminala()
                continue
            else:
                ocisti_zadnju_liniju_terminala()
                break

    while broj_igraca != 0:
        while True:
            if kolona < 10:
                y_unos = input(f"Unesite indeks kolone u kojoj zelite postaviti figuru (1-9): ")
            else:
                y_unos = input(f"Unesite indeks kolone u kojoj zelite postaviti figuru (1-9, a-{chr(kolona+87)}): ")

            if not ((y_unos.isalpha() and len(y_unos) == 1) or ((y_unos.isdigit() and len(y_unos) == 1))):
                ocisti_zadnju_liniju_terminala()
                continue
            else:
                if y_unos.islower():
                    y_unos = ord(y_unos) - 87
                elif y_unos.isupper():
                    y_unos = ord(y_unos) - 55
                elif y_unos.isdigit():
                    y_unos = ord(y_unos) - 48
                    
                if y_unos < 1 or y_unos > kolona:
                    ocisti_zadnju_liniju_terminala()
                    continue
                else:
                    ocisti_zadnju_liniju_terminala()
                    break

        kordinate = (x_unos, y_unos)
        kordinate_protivnika = (red + 1 - x_unos, y_unos)

        if not (kordinate in igrac1 or kordinate in igrac2):
            igrac1.append(kordinate)
            igrac2.append(kordinate_protivnika)
            odrediste1.append(kordinate_protivnika)
            odrediste2.append(kordinate)
            ocisti_terminal()
            stampaj_tablu()
            print("Protivnicke figure se postavljaju simetricno u odnosu na kordinate figura koje unosite!\n")
            broj_igraca -= 1
        else:
            continue

    igrac1.sort()
    igrac2.sort()

    ocisti_terminal()
    stampaj_tablu()
#dobra
def stampaj_info():
    info = ""
    info += f"X: {igrac1}   "
    info += f"Odredista: {odrediste1}   "
    info += f"Preostalo zidova: {broj_zidova[0]} / {pocenti_broj_zidova}"
    info += "\n"
    info += f"O: {igrac2}   "
    info += f"Odredista: {odrediste2}   "
    info += f"Preostalo zidova: {broj_zidova[1]} / {pocenti_broj_zidova}"
    info += "\n"
    info += f"Horizontalni zidovi: {horizontalni_zidovi}"
    info += "\n"
    info += f"Vertikalni zidovi: {vertikalni_zidovi}"
    info += "\n"
    return print(info)
#dobra
def stampaj_prostiji_info():
    info = ""
    info += " Igrac X:   "
    #info += f" Igrac X: {igrac1}   "
    info += f"Preostalo zidova: {broj_zidova[0]} / {pocenti_broj_zidova}"
    info += "\n"
    info += " Igrac O:   "
    #info += f" Igrac O: {igrac2}   "
    info += f"Preostalo zidova: {broj_zidova[1]} / {pocenti_broj_zidova}"
    info += "\n"
    return print(info)
#dobra
def stampaj_tablu(igrac = igrac1):
    tabla_string = ""

    #---------------------------------------brojevi red gore uvuceno
    tabla_string += "    "
    for i in range(1,kolona+1):
        if i < 10:
            tabla_string += f"{i}  "
        else:
            tabla_string += f"{chr(i+55)}  "
    tabla_string += "\n"

    tabla_string += "    "
    for i in range(1,kolona+1):
        tabla_string += "══ "
    tabla_string += "\n"
    #---------------------------------------
    for i in range(1,red+1):
        # redovi
        if i < 10:
            tabla_string += f"{i} ║ "
        else:
            tabla_string += f"{chr(i+55)} ║ "
        for j in range(1,kolona+1):
            (x, y) = (i, j)

            if igrac == igrac1:
                if (x, y) in igrac1:
                    tabla_string += colored ("⊗ ", 'yellow')
                elif (x, y) in igrac2:
                    tabla_string += colored ("⊚ ", 'red')
                elif (x, y) in odrediste2 and (x, y) not in igrac1:
                    tabla_string += colored ("✕ ", 'yellow')
                elif (x, y) in odrediste1 and (x, y) not in igrac2:
                    tabla_string += colored ("✕ ", 'red')
                else:
                    tabla_string += "--"
            elif igrac == igrac2:
                if (x, y) in igrac2:
                    tabla_string += colored ("⊚ ", 'red')
                elif (x, y) in igrac1:
                    tabla_string += colored ("⊗ ", 'yellow')
                elif (x, y) in odrediste2 and (x, y) not in igrac1:
                    tabla_string += colored ("✕ ", 'yellow')
                elif (x, y) in odrediste1 and (x, y) not in igrac2:
                    tabla_string += colored ("✕ ", 'red')
                else:
                    tabla_string += "--"
            else:
                tabla_string += "--"   

            if (i, j) in vertikalni_zidovi:
                tabla_string += colored ("║", "green")
            else:
                tabla_string += " "
        #---------------------------------------numeracija na kraju
        if i < 10:
            tabla_string += f"║ {i}"  
        else:
            tabla_string += f"║ {chr(i+55)}"    
        tabla_string += "\n"
        #---------------------------------------izmedju redova
        tabla_string += "    "
        for j in range(1, kolona+1): 
            if (i, j) in horizontalni_zidovi:
                tabla_string += colored("══ ", 'blue')
            elif i == red:
                tabla_string += "══ "
            else:
                tabla_string += "   "
        tabla_string += "\n"
    #---------------------------------------brojevi red dole uvuceno
    tabla_string += "    "  
    for i in range(1,kolona+1):
        if i < 10:
            tabla_string += f"{i}  "
        else:
            tabla_string += f"{chr(i+55)}  "
    tabla_string += "\n"
    return print(tabla_string)
#dobra
def da_li_je_dobro_postavljen_zid(pozicija, horizontalni):

    (x, y) = pozicija
    if x >= red or x < 1 or y >= kolona or y < 1:
        return False
        
    if horizontalni == True:
        if not (x, y) in horizontalni_zidovi \
            and not ((x, y) in vertikalni_zidovi and (x + 1, y) in vertikalni_zidovi):
            if (x, y + 1) in horizontalni_zidovi:
                return False
            return True

    elif horizontalni == False:
        if not (x, y) in vertikalni_zidovi \
            and not ((x, y) in horizontalni_zidovi and (x, y + 1) in horizontalni_zidovi):
            if (x + 1, y) in vertikalni_zidovi:
                return False
            return True
#dobra
def postavi_zid(pozicija, horizontalni, igrac):

    if broj_zidova[igrac] <= 0:
        return
    if horizontalni:
        horizontalni_zidovi.append(pozicija)
        horizontalni_zidovi.append((pozicija[0], pozicija[1]+1))
    else:
        vertikalni_zidovi.append(pozicija)
        vertikalni_zidovi.append((pozicija[0]+1, pozicija[1]))
    broj_zidova[igrac] -= 1
    ocisti_terminal()
#dobra
def da_li_je_valjan_pomeraj_figure(trenutna_pozicija, nova_pozicija):

    (trenutni_red, trenutna_kolona) = trenutna_pozicija
    (novi_red, nova_kolona) = nova_pozicija

    (x, y) = trenutna_pozicija
    moguce_pozicije = [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), 
                        (x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2), 
                        (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    #filtriranje nevalidnih pozicija 
    moguce_pozicije = [pozicija for pozicija in moguce_pozicije if (pozicija[0] > 0 and pozicija[0] <= red) and (pozicija[1] > 0 and pozicija[1] <= kolona)]
    
    # da ispitamo da li je potez isti i da li premasuje granice table
    if ((trenutni_red == novi_red and trenutna_kolona == nova_kolona)
        or novi_red > red
        or novi_red < 1
        or nova_kolona > kolona
        or nova_kolona < 1):
        return False
            
    #------------------------------------------------------------------------------------

    # ne sme desno 2
    if novi_red == trenutni_red and nova_kolona - 2 == trenutna_kolona:

        if (trenutni_red, trenutna_kolona) in vertikalni_zidovi \
            or (trenutni_red, trenutna_kolona + 1) in vertikalni_zidovi \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2):
            moguce_pozicije.remove((x, y + 2))

    # ne sme levo 2
    if novi_red == trenutni_red and nova_kolona + 2 == trenutna_kolona:

        if (trenutni_red, trenutna_kolona - 1) in vertikalni_zidovi \
            or (trenutni_red, trenutna_kolona - 2) in vertikalni_zidovi \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2):
            moguce_pozicije.remove((x, y - 2))

    # ne sme dole 2
    if novi_red - 2 == trenutni_red and nova_kolona == trenutna_kolona:

        if (trenutni_red, trenutna_kolona) in horizontalni_zidovi \
            or (trenutni_red + 1, trenutna_kolona) in horizontalni_zidovi \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2):
            moguce_pozicije.remove((x + 2, y))

    # ne sme gore 2
    if novi_red + 2 == trenutni_red and nova_kolona == trenutna_kolona:

        if (trenutni_red - 1, trenutna_kolona) in horizontalni_zidovi \
            or (trenutni_red - 2, trenutna_kolona) in horizontalni_zidovi \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2):
            moguce_pozicije.remove((x - 2, y))

    #------------------------------------------------------------------------------------

    # sme desno ako nema figura 1 i ima zid i figura 2
    if novi_red == trenutni_red and nova_kolona - 1 == trenutna_kolona:

        if (trenutni_red, trenutna_kolona) in vertikalni_zidovi \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2) \
            or ((trenutni_red, trenutna_kolona) not in vertikalni_zidovi \
                and (trenutni_red, trenutna_kolona + 1) not in vertikalni_zidovi \
                and ((trenutna_pozicija in igrac1 and (trenutni_red, trenutna_kolona + 2) in odrediste1) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red, trenutna_kolona + 2) in odrediste2))) \
            or (trenutni_red,trenutna_kolona) not in vertikalni_zidovi \
                and (trenutni_red, trenutna_kolona + 1) not in vertikalni_zidovi \
                and (trenutni_red, trenutna_kolona + 1) != (trenutni_red, kolona) \
                and ((trenutna_pozicija in igrac1 and (trenutni_red, trenutna_kolona + 1) not in odrediste1) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red, trenutna_kolona + 1) not in odrediste2)) \
                and ((trenutna_pozicija in igrac1 and (trenutni_red, trenutna_kolona + 2) not in igrac1 + igrac2) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red, trenutna_kolona + 2) not in igrac2 + igrac1)):
            moguce_pozicije.remove((x, y + 1))

    # sme levo ako nema figura 1 i ima zid i figura 2
    if novi_red == trenutni_red and nova_kolona + 1 == trenutna_kolona:
        
        if (trenutni_red, trenutna_kolona - 1) in vertikalni_zidovi \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2) \
            or ((trenutni_red, trenutna_kolona - 1) not in vertikalni_zidovi \
                and (trenutni_red, trenutna_kolona - 2) not in vertikalni_zidovi \
                and ((trenutna_pozicija in igrac1 and (trenutni_red, trenutna_kolona - 2) in odrediste1) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red, trenutna_kolona - 2) in odrediste2))) \
            or (trenutni_red,trenutna_kolona - 1) not in vertikalni_zidovi \
                and (trenutni_red, trenutna_kolona - 2) not in vertikalni_zidovi \
                and (trenutni_red, trenutna_kolona - 1) != (trenutni_red, 1) \
                and ((trenutna_pozicija in igrac1 and (trenutni_red, trenutna_kolona - 1) not in odrediste1) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red, trenutna_kolona - 1) not in odrediste2)) \
                and ((trenutna_pozicija in igrac1 and (trenutni_red, trenutna_kolona - 2) not in igrac1 + igrac2) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red, trenutna_kolona - 2) not in igrac2 + igrac1)):
            moguce_pozicije.remove((x, y - 1))

    # sme dole ako nema figura 1 i ima zid i figura 2
    if novi_red - 1 == trenutni_red and nova_kolona == trenutna_kolona:
        
        if (trenutni_red, trenutna_kolona) in horizontalni_zidovi \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2) \
            or ((trenutni_red, trenutna_kolona) not in horizontalni_zidovi \
                and (trenutni_red + 1, trenutna_kolona) not in horizontalni_zidovi \
                and ((trenutna_pozicija in igrac1 and (trenutni_red + 2, trenutna_kolona) in odrediste1) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red + 2, trenutna_kolona) in odrediste2))) \
            or (trenutni_red,trenutna_kolona) not in horizontalni_zidovi \
                and (trenutni_red + 1, trenutna_kolona) not in horizontalni_zidovi \
                and (trenutni_red + 1, trenutna_kolona) != (red, trenutna_kolona) \
                and ((trenutna_pozicija in igrac1 and (trenutni_red + 1, trenutna_kolona) not in odrediste1) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red + 1, trenutna_kolona) not in odrediste2)) \
                and ((trenutna_pozicija in igrac1 and (trenutni_red + 2, trenutna_kolona) not in igrac1 + igrac2 ) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red + 2, trenutna_kolona) not in igrac2 + igrac1)):
            moguce_pozicije.remove((x + 1, y))

    # sme gore ako nema figura 1 i ima zid i figura 2
    if novi_red + 1 == trenutni_red and nova_kolona == trenutna_kolona:
        
        if (trenutni_red - 1, trenutna_kolona) in horizontalni_zidovi \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2) \
            or ((trenutni_red - 1, trenutna_kolona) not in horizontalni_zidovi \
                and (trenutni_red - 2, trenutna_kolona) not in horizontalni_zidovi \
                and ((trenutna_pozicija in igrac1 and (trenutni_red - 2, trenutna_kolona) in odrediste1) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red - 2, trenutna_kolona) in odrediste2))) \
            or (trenutni_red - 1,trenutna_kolona) not in horizontalni_zidovi \
                and (trenutni_red - 2, trenutna_kolona) not in horizontalni_zidovi \
                and (trenutni_red - 1, trenutna_kolona) != (1, trenutna_kolona) \
                and ((trenutna_pozicija in igrac1 and (trenutni_red - 1, trenutna_kolona) not in odrediste1) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red - 1, trenutna_kolona) not in odrediste2)) \
                and ((trenutna_pozicija in igrac1 and (trenutni_red - 2, trenutna_kolona) not in igrac1 + igrac2) \
                    or (trenutna_pozicija in igrac2 and (trenutni_red - 2, trenutna_kolona) not in igrac2 + igrac1)):
            moguce_pozicije.remove((x - 1, y))

    #-------------------------------------------------------------------------------------

    # ne sme dijagonalno gore desno
    if novi_red + 1 == trenutni_red and nova_kolona - 1 == trenutna_kolona:

        if ((trenutni_red - 1, trenutna_kolona + 1) in horizontalni_zidovi \
                and (trenutni_red - 1, trenutna_kolona) in vertikalni_zidovi) \
            or ((trenutni_red - 1, trenutna_kolona) in horizontalni_zidovi \
                and (trenutni_red, trenutna_kolona) in vertikalni_zidovi) \
            or ((trenutni_red - 1, trenutna_kolona + 1) in horizontalni_zidovi \
                and (trenutni_red - 1, trenutna_kolona ) in horizontalni_zidovi) \
            or ((trenutni_red - 1, trenutna_kolona) in vertikalni_zidovi \
                and (trenutni_red, trenutna_kolona ) in vertikalni_zidovi) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2):
            moguce_pozicije.remove((x - 1, y + 1))

    # ne sme dijagonalno gore levo
    if novi_red + 1 == trenutni_red and nova_kolona + 1 == trenutna_kolona:

        if ((trenutni_red - 1, trenutna_kolona - 1) in horizontalni_zidovi \
                and (trenutni_red - 1, trenutna_kolona - 1) in vertikalni_zidovi) \
            or ((trenutni_red - 1, trenutna_kolona) in horizontalni_zidovi \
                and (trenutni_red, trenutna_kolona - 1) in vertikalni_zidovi) \
            or ((trenutni_red - 1, trenutna_kolona - 1) in horizontalni_zidovi \
                and (trenutni_red - 1, trenutna_kolona) in horizontalni_zidovi) \
            or ((trenutni_red - 1, trenutna_kolona - 1) in vertikalni_zidovi \
                and (trenutni_red, trenutna_kolona - 1) in vertikalni_zidovi) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2):
            moguce_pozicije.remove((x - 1, y - 1))

    # ne sme dijagonalno dole desno
    if novi_red - 1 == trenutni_red and nova_kolona - 1 == trenutna_kolona:

        if ((trenutni_red, trenutna_kolona + 1) in horizontalni_zidovi \
                and (trenutni_red + 1, trenutna_kolona) in vertikalni_zidovi) \
            or ((trenutni_red, trenutna_kolona) in horizontalni_zidovi \
                and (trenutni_red, trenutna_kolona) in vertikalni_zidovi) \
            or ((trenutni_red, trenutna_kolona) in horizontalni_zidovi \
                and (trenutni_red, trenutna_kolona + 1) in horizontalni_zidovi) \
            or ((trenutni_red, trenutna_kolona) in vertikalni_zidovi \
                and (trenutni_red + 1, trenutna_kolona) in vertikalni_zidovi) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2):
            moguce_pozicije.remove((x + 1, y + 1))

    # ne sme dijagonalno dole levo
    if novi_red - 1 == trenutni_red and nova_kolona + 1 == trenutna_kolona:

        if ((trenutni_red, trenutna_kolona - 1) in horizontalni_zidovi \
                and (trenutni_red + 1, trenutna_kolona - 1) in vertikalni_zidovi) \
            or ((trenutni_red, trenutna_kolona) in horizontalni_zidovi \
                and (trenutni_red, trenutna_kolona - 1) in vertikalni_zidovi) \
            or ((trenutni_red, trenutna_kolona) in horizontalni_zidovi \
                and (trenutni_red, trenutna_kolona - 1) in horizontalni_zidovi) \
            or ((trenutni_red, trenutna_kolona - 1) in vertikalni_zidovi \
                and (trenutni_red + 1, trenutna_kolona - 1) in vertikalni_zidovi) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac1) \
            or (trenutna_pozicija in igrac1 and nova_pozicija in igrac2 and nova_pozicija not in odrediste1) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac2) \
            or (trenutna_pozicija in igrac2 and nova_pozicija in igrac1 and nova_pozicija not in odrediste2):
            moguce_pozicije.remove((x + 1, y - 1))
    
    #------------------------------------------------------------------------------------

    if(nova_pozicija not in moguce_pozicije):
        return False    
    return True 
#dobra
def pomeri_figuru(trenutna_pozicija, nova_pozicija, figura):
    
    if trenutna_pozicija in igrac1:
        igrac1[figura] = nova_pozicija

    if trenutna_pozicija in igrac2:
        igrac2[figura] = nova_pozicija

    ocisti_terminal()
#dobra
def jeste_pobeda():
    if (igrac1[0] in odrediste1 or igrac1[1] in odrediste1) \
        or (igrac2[0] in odrediste2 or igrac2[1] in odrediste2):
        return True
    else:
        return False
#dobra
def ocisti_terminal():                              # https://www.delftstack.com/howto/python/python-clear-console/
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def ocisti_zadnju_liniju_terminala():               # https://linustechtips.com/topic/1257798-delete-last-line-in-console-python-3/
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def ko_pocinje_igru():
    global pocinje_igru_igrac

    while True:
        ko_igra_prvi = input("Unesite x ili o da selektujete ko igra prvi: ")
        if (ko_igra_prvi not in ['x','X','o','O']):
            ocisti_zadnju_liniju_terminala()
            continue
        else:
            ocisti_zadnju_liniju_terminala()
            if ko_igra_prvi in ['x', 'X']:
                pocinje_igru_igrac = 0
            else:
                pocinje_igru_igrac = 1
            break
#dobra
def akcija_postavi_zid(igrac):
    while True:
        while True:
            tip_zida = input("Unesite tip zida (v, h): ")
            if tip_zida not in ['V','v','H','h']:
                ocisti_zadnju_liniju_terminala()
                continue
            else:
                ocisti_zadnju_liniju_terminala()
                if tip_zida in ['V','v']:
                    horizontalni_unos = False
                if tip_zida in ['H','h']:
                    horizontalni_unos = True
                break
        while True:
            if red < 10:
                x_unos = input(f"Unesite kordinate zida (red) (1-9): ")
            else:
                x_unos = input(f"Unesite kordinate zida (red) (1-9, a-{chr(red+87)}): ")

            if not ((x_unos.isalpha() and len(x_unos) == 1) or ((x_unos.isdigit() and len(x_unos) == 1))):
                ocisti_zadnju_liniju_terminala()
                continue
            else:
                if x_unos.islower():
                    x_unos = ord(x_unos) - 87
                elif x_unos.isupper():
                    x_unos = ord(x_unos) - 55
                elif x_unos.isdigit():
                    x_unos = ord(x_unos) - 48

                if x_unos < 1 or x_unos > red - 1:
                    ocisti_zadnju_liniju_terminala()
                    continue
                else:
                    ocisti_zadnju_liniju_terminala()
                    break
        while True:
            if kolona < 10:
                y_unos = input(f"Unesite kordinate zida (kolona) (1-9): ")
            else:
                y_unos = input(f"Unesite kordinate zida (kolona) (1-9, a-{chr(kolona+87)}): ")
            if not ((y_unos.isalpha() and len(y_unos) == 1) or ((y_unos.isdigit() and len(y_unos) == 1))):
                ocisti_zadnju_liniju_terminala()
                continue
            else:
                if y_unos.islower():
                    y_unos = ord(y_unos) - 87
                elif y_unos.isupper():
                    y_unos = ord(y_unos) - 55
                elif y_unos.isdigit():
                    y_unos = ord(y_unos) - 48

                if y_unos < 1 or y_unos > kolona - 1:
                    ocisti_zadnju_liniju_terminala()
                    continue
                else:
                    ocisti_zadnju_liniju_terminala()
                    break

        if not da_li_je_dobro_postavljen_zid((x_unos, y_unos),horizontalni_unos):
            continue
        else:
            postavi_zid((x_unos, y_unos),horizontalni_unos,igrac)

            postoji_put = BFS(igrac1[0], odrediste1[0]) \
                    and BFS(igrac1[0], odrediste1[1]) \
                    and BFS(igrac1[1], odrediste1[0]) \
                    and BFS(igrac1[1], odrediste1[1]) \
                    and BFS(igrac2[0], odrediste2[0]) \
                    and BFS(igrac2[0], odrediste2[1]) \
                    and BFS(igrac2[1], odrediste2[0]) \
                    and BFS(igrac2[1], odrediste2[1])

            if postoji_put == True:
                break
            else:
                if horizontalni_unos == False:
                    vertikalni_zidovi.remove((x_unos, y_unos))
                    vertikalni_zidovi.remove((x_unos + 1, y_unos))
                    broj_zidova[igrac] += 1
                    ocisti_terminal()
                    stampaj_tablu()
                    print("Nepravilan potez! Postavljanjem ovog zida bi zagradili put do cilja igracima.\n") 
                else:
                    horizontalni_zidovi.remove((x_unos, y_unos))
                    horizontalni_zidovi.remove((x_unos, y_unos + 1))
                    broj_zidova[igrac] += 1
                    ocisti_terminal()
                    stampaj_tablu()
                    print("Nepravilan potez! Postavljanjem ovog zida bi zagradili put do cilja igracima.\n")
#dobra
def akcija_pomeri_figuru(igrac): # 0 za levu 1 za desnu jer su sortirane kordinate
    while True:
        while True:
            figura = input("Koju figuru zelite da pomerite (l, d): ")
            if figura not in ['l','L','d','D']:
                ocisti_zadnju_liniju_terminala()
                continue
            else:
                ocisti_zadnju_liniju_terminala()
                break
        if figura in ['l','L']:
            leva_desna = 0
        if figura in ['d','D']:
            leva_desna = 1
        while True:
            if red < 10:
                x_unos = input(f"Unesite kordinate skoka (red) (1-9): ")
            else:
                x_unos = input(f"Unesite kordinate skoka (red) (1-9, a-{chr(red+87)}): ")

            if not ((x_unos.isalpha() and len(x_unos) == 1) or ((x_unos.isdigit() and len(x_unos) == 1))):
                ocisti_zadnju_liniju_terminala()
                continue
            else:
                if x_unos.islower():
                    x_unos = ord(x_unos) - 87
                elif x_unos.isupper():
                    x_unos = ord(x_unos) - 55
                elif x_unos.isdigit():
                    x_unos = ord(x_unos) - 48

                if x_unos < 1 or x_unos > red:
                    ocisti_zadnju_liniju_terminala()
                    continue
                else:
                    ocisti_zadnju_liniju_terminala()
                    break
        while True:
            if kolona < 10:
                y_unos = input(f"Unesite kordinate skoka (kolona) (1-9): ")
            else:
                y_unos = input(f"Unesite kordinate skoka (kolona) (1-9, a-{chr(kolona+87)}): ")

            if not ((y_unos.isalpha() and len(y_unos) == 1) or ((y_unos.isdigit() and len(y_unos) == 1))):
                ocisti_zadnju_liniju_terminala()
                continue
            else:
                if y_unos.islower():
                    y_unos = ord(y_unos) - 87
                elif y_unos.isupper():
                    y_unos = ord(y_unos) - 55
                elif y_unos.isdigit():
                    y_unos = ord(y_unos) - 48

                if y_unos < 1 or y_unos > kolona:
                    ocisti_zadnju_liniju_terminala()
                    continue
                else:
                    ocisti_zadnju_liniju_terminala()
                    break
        if not da_li_je_valjan_pomeraj_figure(igrac[leva_desna], (x_unos, y_unos)):
            continue
        else:
            pomeri_figuru(igrac[leva_desna],(x_unos, y_unos),leva_desna)
            break
#dobra


def vrati_poteze(pozicija):
    (x, y) = pozicija
    # svi potezi jer figura moze da ide jedno polje u odredjenim situacijama
    pozicije = [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), 
    (x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    pozicije = [pozicija for pozicija in pozicije if (pozicija[0] > 0 and pozicija[0] <= red) and (pozicija[1] > 0 and pozicija[1] <= kolona)]
    potezi = []

    for nova_pozicija in pozicije:
        if da_li_je_valjan_pomeraj_figure(pozicija, nova_pozicija):
            potezi.append(nova_pozicija)
    return potezi
#dobra
def BFS(pocetna_pozicija, odredisna_pozicija):

    queue_pozicija = queue.Queue(kolona*red)
    poseceni = set()
    prethodni_cvor = dict()
    prethodni_cvor[pocetna_pozicija] = None
    poseceni.add(pocetna_pozicija)
    queue_pozicija.put(pocetna_pozicija)
    odrediste = False

    while (not odrediste) and (not queue_pozicija.empty()):
        trenutna_pozicija = queue_pozicija.get()
        for nova_pozicija in vrati_poteze(trenutna_pozicija):
            if nova_pozicija not in poseceni:
                prethodni_cvor[nova_pozicija] = trenutna_pozicija
                if nova_pozicija == odredisna_pozicija:
                    odrediste = True
                    break
                poseceni.add(nova_pozicija)
                queue_pozicija.put(nova_pozicija)

    return True if odrediste == True else False
#dobra


def BFSPut(pocetna_pozicija, odredisna_pozicija):

    queue_pozicija = queue.Queue(kolona*red)
    poseceni = set()
    prethodni_cvor = dict()
    prethodni_cvor[pocetna_pozicija] = None
    poseceni.add(pocetna_pozicija)
    queue_pozicija.put(pocetna_pozicija)
    odrediste = False

    while (not odrediste) and (not queue_pozicija.empty()):
        trenutna_pozicija = queue_pozicija.get()
        for nova_pozicija in vrati_poteze(trenutna_pozicija):
            if nova_pozicija not in poseceni:
                prethodni_cvor[nova_pozicija] = trenutna_pozicija
                if nova_pozicija == odredisna_pozicija:
                    odrediste = True
                    break
                poseceni.add(nova_pozicija)
                queue_pozicija.put(nova_pozicija)

    path = list()
    if odrediste:
        path.append(odredisna_pozicija)
        prev = prethodni_cvor[odredisna_pozicija]
        while prev is not None:
            path.append(prev)
            prev = prethodni_cvor[prev]
            path.reverse()
    return path
#dobra
def proceni_stanje(pozicija_o_levi, pozicija_o_desni, pozicija_x_levi, pozicija_x_desni):
    return float(   min(len(BFSPut(pozicija_o_levi,odrediste2[0])), 
                        len(BFSPut(pozicija_o_levi,odrediste2[1])), 
                        len(BFSPut(pozicija_o_desni,odrediste2[0])), 
                        len(BFSPut(pozicija_o_desni,odrediste2[1]))) - \
                    min(len(BFSPut(pozicija_x_levi,odrediste1[0])),
                        len(BFSPut(pozicija_x_levi,odrediste1[1])),
                        len(BFSPut(pozicija_x_desni,odrediste1[0])),
                        len(BFSPut(pozicija_x_desni,odrediste1[1]))) )                
#dobra
def minmax(pozicija_max_levi, pozicija_max_desni, pozicija_min_levi, pozicija_min_desni, dubina, max_player):

    najbolji_potez = None

    if dubina == 0:
        return proceni_stanje(pozicija_max_levi, pozicija_max_desni, pozicija_min_levi, pozicija_min_desni), najbolji_potez

    if max_player:
        max_ocena = float('inf')
        for potez in vrati_poteze(pozicija_max_levi):
            ocena = minmax(potez, pozicija_max_desni, pozicija_min_levi, pozicija_min_desni, dubina - 1, False)[0]
            max_ocena = min(max_ocena, ocena)
            if max_ocena == ocena:
                najbolji_potez = potez
        for potez in vrati_poteze(pozicija_max_desni):
            ocena = minmax(pozicija_max_levi, potez, pozicija_min_levi, pozicija_min_desni, dubina - 1, False)[0]
            max_ocena = min(max_ocena, ocena)
            if max_ocena == ocena:
                najbolji_potez = potez
        return max_ocena, najbolji_potez

    else:
        min_ocena = float('-inf')
        for potez in vrati_poteze(pozicija_min_levi):
            ocena = minmax(pozicija_max_levi, pozicija_max_desni, potez, pozicija_min_desni, dubina - 1, True)[0]
            min_ocena = max(min_ocena, ocena)
            if min_ocena == ocena:
                najbolji_potez = potez
        for potez in vrati_poteze(pozicija_min_desni):
            ocena = minmax(pozicija_max_levi, pozicija_max_desni, pozicija_min_levi, potez, dubina - 1, True)[0]
            min_ocena = max(min_ocena, ocena)
            if min_ocena == ocena:
                najbolji_potez = potez
        return min_ocena, najbolji_potez
# minmax za postavljanje zidova fali
def minmax_potez(igrac2, igrac1):

    potez = minmax(igrac2[0], igrac2[1], igrac1[0], igrac1[1], 1, True)[1]
    if potez in vrati_poteze(igrac2[0]):
        pomeri_figuru(igrac2[0], potez, 0)
    else:
        pomeri_figuru(igrac2[1], potez, 1)
#dobra
    
def igraminmax():

    while not jeste_pobeda():

        print("Igrac X je na potezu! (pomerite figuru) \n")
        akcija_pomeri_figuru(igrac1)
        stampaj_tablu(igrac1)
        stampaj_prostiji_info()
        if jeste_pobeda():
            ocisti_terminal()
            stampaj_tablu(igrac1)
            stampaj_prostiji_info()
            print("Igrac X je pobedio! CESTITAMO.\n")
            break
        if broj_zidova[0] > 0:
            print("Igrac X je na potezu! (postavite zid) \n")
            akcija_postavi_zid(0)
            stampaj_tablu(igrac1)
            stampaj_prostiji_info()
        
        minmax_potez(igrac2,igrac1)
        stampaj_tablu(igrac2)
        stampaj_prostiji_info()
        print("AI agent je odigrao potez!")
        if jeste_pobeda():
            ocisti_terminal()
            stampaj_tablu(igrac2)
            stampaj_prostiji_info()
            print("AI agent je pobedio! CESTITAMO.\n")
            break
        if broj_zidova[1] > 0 and not jeste_pobeda():
            print("AI je na potezu! (postavite zid) \n")
            akcija_postavi_zid(1)
            stampaj_tablu(igrac2)
            stampaj_prostiji_info()
#dobra 
def igra():

    ko_pocinje_igru()

    while not jeste_pobeda():

        if pocinje_igru_igrac == 0:

            print("Igrac X je na potezu! (pomerite figuru) \n")
            akcija_pomeri_figuru(igrac1)
            stampaj_tablu(igrac1)
            stampaj_prostiji_info()
            if jeste_pobeda():
                ocisti_terminal()
                stampaj_tablu(igrac1)
                stampaj_prostiji_info()
                print("Igrac X je pobedio! CESTITAMO.\n")
                break
            if broj_zidova[0] > 0:
                print("Igrac X je na potezu! (postavite zid) \n")
                akcija_postavi_zid(0)
                stampaj_tablu(igrac1)
                stampaj_prostiji_info()

            print("Igrac O je na potezu! (pomerite figuru) \n")
            akcija_pomeri_figuru(igrac2)
            stampaj_tablu(igrac2)
            stampaj_prostiji_info()
            if jeste_pobeda():
                ocisti_terminal()
                stampaj_tablu(igrac2)
                stampaj_prostiji_info()
                print("Igrac O je pobedio! CESTITAMO.\n")
                break
            if broj_zidova[1] > 0:
                print("Igrac O je na potezu! (postavite zid) \n")
                akcija_postavi_zid(1)
                stampaj_tablu(igrac2)
                stampaj_prostiji_info()

        if pocinje_igru_igrac == 1:

            print("Igrac O je na potezu! (pomerite figuru) \n")
            akcija_pomeri_figuru(igrac2)
            stampaj_tablu(igrac2)
            stampaj_prostiji_info()
            if jeste_pobeda():
                ocisti_terminal()
                stampaj_tablu(igrac2)
                stampaj_prostiji_info()
                print("Igrac O je pobedio! CESTITAMO.\n")
                break
            if broj_zidova[1] > 0:
                print("Igrac O je na potezu! (postavite zid) \n")
                akcija_postavi_zid(1)
                stampaj_tablu(igrac2)
                stampaj_prostiji_info()

            print("Igrac X je na potezu! (pomerite figuru) \n")
            akcija_pomeri_figuru(igrac1)
            stampaj_tablu(igrac1)
            stampaj_prostiji_info()
            if jeste_pobeda():
                ocisti_terminal()
                stampaj_tablu(igrac1)
                stampaj_prostiji_info()
                print("Igrac X je pobedio! CESTITAMO.\n")
                break
            if broj_zidova[0] > 0:
                print("Igrac X je na potezu! (postavite zid) \n")
                akcija_postavi_zid(0)
                stampaj_tablu(igrac1)
                stampaj_prostiji_info()
#dobra


def blocade():

    ocisti_terminal()
    unos_dimenzija_table()
    unos_kordinata_figura()
    stampaj_prostiji_info()
    print("(1) Player VS Player")
    print("(2) Player VS AI\n")

    while True:
        unos = input("Izaberite tip igre: ")
        if unos not in ['1', '2']:
            ocisti_zadnju_liniju_terminala()
            continue
        else:
            ocisti_zadnju_liniju_terminala()
            ocisti_zadnju_liniju_terminala()
            ocisti_zadnju_liniju_terminala()
            ocisti_zadnju_liniju_terminala()
            if unos == '1':
                igra()
                break
            else:
                igraminmax()
                break
#dobra



blocade()