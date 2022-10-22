haslo='skrzydłokwiat'

print("""Twoim zadanie będzie odgadnięcie hasła. 
Za każdym razem możesz podać jedną literę albo od razu podać całe hasło.""")

ilosc_prob=len(haslo)+7
print("Hasło sklada się z : ", len(haslo))
print("Twoja ilość prób wynosi: ",ilosc_prob)


tablica_z_rozwiazaniem=[]
for i in range(len(haslo)):
    tablica_z_rozwiazaniem.append('-')

tablica=[]
for i in tablica_z_rozwiazaniem:
        print(i,  end="")
print()

for i in range(ilosc_prob):
    tryb_wyboru=input("Wpisz 1 jeśli chcesz podać 1 literę albo wpisz 2 jeśli chcesz odgadnąć całe hasło: ")
    if tryb_wyboru == "1":
        litera_uzytkownika = input("podaj litere: ")
        for index_litery_w_hasle in range(len(haslo)):
            if litera_uzytkownika == haslo[index_litery_w_hasle]:
                tablica_z_rozwiazaniem[index_litery_w_hasle] = litera_uzytkownika

        print(tablica_z_rozwiazaniem)
    else:
        haslo_uzytkownika=input("Podaj haslo, jesli myslisz, ze znasz odpowiedz: ")
        if haslo_uzytkownika.lower() == haslo.lower():
            print("Brawo! Udalo Ci sie odgadnac haslo.")
        else:
            print("Niestety, nie udalo sie")

print("Liczba prób została wyczerpana. Wisielec został powieszony.")

# for i in range(0):
#     litera_uzytkownika=input("podaj litere: ")
#     for index_litery_w_hasle in range(len(haslo)):
#         if litera_uzytkownika == haslo[index_litery_w_hasle]:
#             tablica_z_rozwiazaniem[index_litery_w_hasle] = litera_uzytkownika
#
#     print(tablica_z_rozwiazaniem)
#
# print("Liczba prób została wyczerpana. Wisielec został powieszony.")
#
#
# haslo_uzytkownika=input("Podaj haslo, jesli myslisz, ze znasz odpowiedz: ")
# if haslo_uzytkownika.lower() == haslo.lower():
#     print("Brawo! Udalo Ci sie odgadnac haslo.")
# else:
#     print("Niestety, nie udalo sie")
#
# tryb_wyboru=input("Wpisz 1 jeśli chcesz podać 1 literę albo wpisz 2 jeśli chcesz odgadnąć całe hasło")
# if tryb_wyboru == "1":
#     print("podaj litere: ")
# else:
#     print("podaj cale haslo: ")




#     podaj_litere=input("Podaj litere: ")
#     if podaj_litere in haslo:
#         tablica.append(podaj_litere)
#         print(tablica)
#     else:
#         print("Taka litera nie istnieje w haśle. Podaj inną literę.")


# for j in haslo:
    # print(j)
    # print("litera:", j)