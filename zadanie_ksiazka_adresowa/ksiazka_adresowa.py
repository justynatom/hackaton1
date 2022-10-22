#kontakty = [['Jan Kowalski', '123456789', 'jankow@wp.pl'],['Adam Malysz', '999222333', 'orzelzwisly@onet.pl']]

ksiazka_adresowa={
    "imie_nazwisko": ['Jan Kowalski', 'Adam Małysz'],
    "telefon": ['123456789', '342456987'],
    "email": ['jan@gmail.com','orzelzwisly@wp.pl']
}


# dodanie_nowego_uzytkownika=[]
# for dodanie_nowego_uzytkownika not in ksiazka_adresowa:
#     podaj_imie_nazw=input("Podaj imie i nazwisko ")
#     dodanie_nowego_uzytkownika.insert(1, podaj_imie_nazw)
#     podaj_telefon=input("podaj numer telefonu: ")
#     dodanie_nowego_uzytkownika.insert(2, podaj_telefon)
#     podaj_emaila=input("podaj emaila: ")
#     dodanie_nowego_uzytkownika.insert(3, podaj_emaila)

# uzytkownik=input("podaj cokolwiek lub pusty znak")
# if uzytkownik == "":
#     print("koniec programu")
# else:
#     print(uzytkownik)

print("Wpisz 1, jeśli chcesz wyświetlić wszystkich użytkowników\n"
      "Wpisz 2, jeśli chcesz dodać nowy wpis z danymi\n"
      "Wpisz 3, jeśli chcesz usunąć wpis\n"
      "Wpisz 0, jeśli chcesz zakończyć program")

wybor_uzytkownika=1

while wybor_uzytkownika != "0":
    wybor_uzytkownika=input("Podaj liczbę: ")
    if wybor_uzytkownika == "1":
        for index in range(len(ksiazka_adresowa["imie_nazwisko"])):
            print(index)
            print("imie i nazwisko:", ksiazka_adresowa['imie_nazwisko'][index], ',', "telefon:", ksiazka_adresowa['telefon'][index],
                  ',', "email:", ksiazka_adresowa['email'][index])
    elif wybor_uzytkownika == "2":
        nowy_wpis_z_danymi=input("Podaj imie i nazwisko nowego znajomego")
        ksiazka_adresowa["imie_nazwisko"].append(nowy_wpis_z_danymi)
        nowy_wpis_telefon=input("Podaj numer telefonu nowego znajomego: ")
        ksiazka_adresowa["telefon"].append(nowy_wpis_telefon)
        nowy_wpis_email=input("Podaj maila nowego znajomego: ")
        ksiazka_adresowa["email"].append(nowy_wpis_email)
        print(ksiazka_adresowa)
    elif wybor_uzytkownika == "3":
        index_od_uzytkownika=int(input("podaj numer indeksu, ktory chesz usunac: "))
        ksiazka_adresowa["imie_nazwisko"].pop(index_od_uzytkownika)
        ksiazka_adresowa["telefon"].pop(index_od_uzytkownika)
        ksiazka_adresowa["email"].pop(index_od_uzytkownika)
        print(ksiazka_adresowa)
    elif wybor_uzytkownika == "0":
        print("Pa pa")
    else:
        print("Nie ma takiej opcji. Ponów wybór opcji. ")