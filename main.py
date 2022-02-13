# i = 2
# f = 2.414141
# c = 0.5 + 1j
#
# print(float(i), int(f), c)
#
# a = 2 > 1
# print(a)
# print()
# print(type(a))
#
# b = 2.787989 > 3
# print(b)
# print(type(b))
#
# napis = "Ala ma kota"
# print(type(napis))
# print(napis[0])
# print(type(napis[0]))
# print(napis[-3:-1])
# print(napis[::1])
# print(napis[::2])
#
# txt = "datatypes"
# print(txt)
# y = int(len(txt) * 0.5)
# print(txt[y-1:y+2])
#
# s1 = "fullstack"
# s2 = "Python"
# s1_1 = int(len(s1)/2)
# print(s1_1)
# print(s1[:s1_1] +s2 +s1[s1_1:])
# -------------------------------------------------------------------
# CWICZENIE
# Biorąc pod uwagę 2 ciągi, s1 i s2 zwróć nowy ciąg złożony z pierwszego, środkowego i ostatniego znaku
# każdego ciągu wejściowego
# Dane:
# s1 = "America"
# s2 = "Japan"
# Oczekiwany wynik:
# AJrpan
#
# s1 = "America"
# s2 = "Japan"
# # x = s1[0] + s2[0]
# # y = s1[-1] + s2[-1]
# # middle_1 = int(len(s1)/2)
# # middle_2 = int(len(s2)/2)
# # center = middle_1 + middle_2
# # print(x + center + y)
# # # print(x +s1[:middle_1] +s2[:middle_2] + y)
# ----------------------------------------------------------------------
# str1 = "Python"
# str2 = str1[::-1]
# print(str2)
# Jan    = ("Jan", "Kowalski", 33)
# Janina = ("Janina", "Nowak", (21, 12, 1978), 'K')
# print(Jan)
# print(Janina)
#
# imie     = Jan[0]
# nazwisko = Jan[1]
# wiek     = Jan[2]
#
# imie, nazwisko, wiek = Jan
# print(imie, nazwisko, wiek)
# lista = [1, 2, 3, 4, -5, 6, -10]
# print(lista)
#
# liczby = [0.1, 0.2, 0.3, 4.5, -7.3, 6.87, 10]
# print(liczby)
# imiona = ['Ala', 'Zygmunt', "Alojzy", "Bogusława"]
# print(imiona)
# print(type(imiona))
# lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# print(lista)
# print(lista[2:6:2])
# print(lista[:4])
# print(lista[-2:])
# print(lista[::-1])
# lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# print(lista)
# lista = [2, 3, 5, 7, 9]
# print(lista)
# lista[2:4] = ["pies", "a", "2"]
# print(lista)
# lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# lista.append("zebra")
# print(lista)
# lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# lista.insert(2, "zebra")
# print(lista)
# ------------------------------------------------------------------------
# uczestnicy = ["Rafal", "Tomek", "Agata", "Michal", "Robert", "Pawel", "Grzegorz", "Wiktor"]
# nowa_lista = sorted(uczestnicy)
# print(nowa_lista)
# print(len(nowa_lista))
# uczestnicy.sort()
# print(uczestnicy)
# print(len(uczestnicy))
# ----------------------------------------------------------------------
# SŁOWNIK
# slownik = {"ala": "kot", "ola": 1 , "python": True}
# print(slownik)
# tel = {'Maja': 500456, 'Jasio': 343455}
# tel['Ola'] = 3024127
# print(tel)
# del tel['Maja']
# print(tel)
# tel = dict([('Jan', 4139277), ('Kazimierz', 4126327)])
# print(tel)
# ------------------------------------------------------------------------------
# ZBIOR
# zbior = {"ala", "kot", 1, 2.89}
# print(zbior)
# ---------------------------------------------------------------------------
# CWICZENIE
# Napisz program, który będzie prosił użytkownika o podanie dwóch liczb, i wypisze:
# Wynik ich dzielenia, resztę z dzielenia, oraz wynik dzielenia całkowitego
#
# print("Podaj pierwsza liczbe: ")
# x = float(input())
# print("Podaj druga liczbe: ")
# y = float(input())
# wynik_dzielenia = x / y
# reszta_z_dzielenia = x % y
# wynik_dzielenia_calkowitego = x // y
# print("Wynik dzielenia: " +str(wynik_dzielenia))
# print("Reszta z dzielenia: " +str(reszta_z_dzielenia))
# print("Wynik dzielenia calkowitego: " +str(wynik_dzielenia_calkowitego))
# ----------------------------------------------------------------------------
# ĆWICZENIE instrukcji if
# Przypisz 8 do zmiennej x i 15 do zmiennej y
# Utwórz 2 instrukcje warunkowe
# Niech pierwsza wypisze: „Co najmniej jeden z warunków jest spełniony”, jeśli x jest większe niż 3 lub y jest parzyste
# Niech drugi wypisze „Żaden warunek nie jest spełniony”, jeśli x jest mniejsze lub równe 3, a y jest nieparzyste
# Zmień wartości przypisane do x i y i ponownie uruchom komórkę, aby sprawdzić, czy kod nadal działa
# x = 1
# y = 15
# if x > 3 or y % 2 == 0:
#     print("Co najmniej jeden za warunkow jest spelniony")
# if x <= 3 and y % 2 != 0:
#     print("Zaden warunek nie jest spelniony")
# x = True
# if not x:
#     print("warunek spełniony")
# else:
#     print("warunek niespełniony")
# kazda_wartosc = "test" and [123]
# print(kazda_wartosc)
# print("test" or 0)
# print([] and "test")
# ------------------------------------------------------------------------------
# CWICZENIE instrukcji and
# Zwróć True, jeśli oba stwierdzenia są prawdziwe
# x > 3 i x < 10
# Spróbuj!
# x = float(input("Podaj x: "))
# y = x > 3 and x < 10
# print(y)
# x = float(input("Podaj x: "))
# if x > 3 and x < 10:
#     print(True)
# else:
#     print(False)
# --------------------------------------------
# CWICZENIE instrukcji or
# Zwróć wartość True, jeśli jedno ze stwierdzeń jest prawdziwe
# x > 4 lub x < 3
# Spróbuj!
# x = float(input("Podaj x: "))
# y = x > 4 or x < 3
# print(y)
# --------------------------------------------------------------------
# CWICZENIE instrukcji not
# Odwróć wynik, zwróć False, jeśli wynik jest prawdziwy
# nie ( x > 3 i x < 10 )
# Spróbuj!
# x = float(input("Podaj x: "))
# if not x > 4 or x < 3:
#     print(True)
# else:
#     print(False)
# x = 2
# print(not(x > 3 and x < 10))
# wartosc = 0
# wartosc = "warunek spełniony" if True else "warunek niespełniony"
# # if True: wartosc = "warunek spełniony"
# print(wartosc)
# nice = True
# personality = ("wredny", "miły")[nice]
# print("Kot jest", personality)
#PETLE
# string = 'Python'
# for litera in string:
#    print('litera:', litera)
# warzywa = ['marchew', 'kalafior', 'kapusta']
# for warzywo in warzywa:
#     print('warzywo:', warzywo)
# warzywa = ['marchew', 'kalafior', 'kapusta']
# i = 1
# for warzywo in warzywa:
#     print('warzywo:', i, warzywo)
#     i += 1
# -----------------------------------------------------------------------------
# CWICZENIE
# Utwórz listę zawierającą imiona wszystkich kursantów
# Następnie ją posortuj alfabetycznie, oraz
# Policz ile z osób na liście jest kobietami
# W tym celu możesz sprawdzić czy imię kończy się na „a”
# uczestnicy = ["Rafal", "Tomek", "Agata", "Michal", "Robert", "Pawel", "Grzegorz", "Wiktor", "Wiktoria", "Agnieszka"]
# uczestnicy.sort()
# i = 0
# for kobiety in uczestnicy:
#     if kobiety[-1]  == "a":
#         i=i+1
# print(i)
# print("Przykład range() w Pythonie")
# print("Uzyskaj liczby z zakresu od 0 do 5")
# for i in range(6):
#     print(i, end=', ')
# print(range(2, 11, 2))
#
# lista = list(range(2, 11, 2))
# print(lista)
# for i in range(5):
#     print(i)
# else:
#     print("Gotowe!")
# liczby = list()
# i = 2
# while i < 11:
#     liczby.append(i)
#     i += 2
# print(liczby)
# lines = list()
# ----------------------------------------------------------------------------------
#
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')  # reset
# print(lines)
# for num in range(1, 20):
#     if not num % 2:  # num % 2 == 0
#         print('Kolejna liczba parzysta:', num)
#         continue
#     print('Kolejna liczba:', num)
#
# for n in range(2, 100):
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else: # normalny koniec pętli
#         print(n, 'jest liczbą pierwszą')
# --------------------------------------------------------------------------------------
# CWICZENIE
# Napisz program, który policzy największy wspólny dzielnik dwóch liczb podanych przez użytkownika
# W tym celu użyj operatora % oraz pętli for
# x = int(input("Podaj pierwsza liczbe: "))
# y = int(input("Podaj druga liczbe: "))
#
# if x > y:
#     print("x jest wieksze od y")
#     n = y
# else:
#     print("x jest mniejsze od y")
#     n = x
# print(n)
#
# for z in range(n, 0, -1):
#     if x % z == 0 and y % z == 0:
#         print(x, "i" , y, "dzieli sie przez" ,z)
#         break
# --------------------------------------------------------------------------------------
# CWICZENIE
# name = input("Proszę wpisać swoje imię.")
# # Wpisz swoją odpowiedź tutaj.
#
# if len(name) > 0:
#     print(name)
# else:
#     pass
# --------------------------------------------------------------------
# Ćwiczenie
# Znajdź liczby, które są podzielne przez 7 i są wielokrotnością 5 w zakresie
# Napisz program w Pythonie, aby znaleźć liczby podzielne przez 7 i będące wielokrotnością 5 między 1500 a 2700 (obie uwzględnione)
# for number in range(1500, 2701):
#     if number % 7 == 0 and number % 5 == 0:
#         print(number)
# ----------------------------------------------------------------------
# Funkcja definiowania:
#
# def simple_function():
#     print('Hello world!')
#     print('Wikipedia')
#
# simple_function()
#
# def my_function():
#     return 3+3
# print(my_function())
# ---------------------------------------------------------------------------
# Ciag Fibonacciego
#
# def fibbonaci_numbers(n):
#     ''' zwraca liczby Fibonacciego mniejsze od n '''
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#     # while len(wynik) < n:
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik
# ------------------------------------------------------------------------------
# ĆWICZENIE
# Funkcja w Pythonie do obliczania długości łańcucha
#
# def funkcja(x):
#     a = 0
#     for y in x:
#         a = a+1
#     return a
# c = funkcja("Wartosc: ")
# print(c)
# ----------------------------------------------------------------------------
# ĆWICZENIE
# Napisz funkcję w Pythonie, która zsumuje wszystkie elementy na liście.
#
# def lista(l):
#     a = 0
#     for i in l:
#         a +=i
#     return a
# b = lista([1,5,6,8])
# print(b)
# -----------------------------------------------------------------------------
# ĆWICZENIE
# Napisz funkcję w Pythonie, który mnoży wszystkie elementy na liście.
#
# def lista(x):
#     a=x[0]
#     for i in x[1:]:
#         a*=i
#     return a
# b=lista([2,4,5])
# print(b)
# -----------------------------------------------------------------------------
# ĆWICZENIE
# Funkcja w Pythonie, aby uzyskać największą liczbę z listy
#
# def lista(x):
#     a=x[0]
#     for i in x[1:]:
#         if i>a:
#             a=i
#     return a
# b=[4,15,8,11,3,12]
# c=lista(b)
# print(c)
# ------------------------------------------------------------------------------
# ĆWICZENIE
# Napisz funkcję w Pythonie, który zlicza liczbę znaków (częstotliwość znaków) w ciągu tekstowym.
# Przykładowy ciąg tekstowy: google.com
# Oczekiwany wynik: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
#
# def funkcja(x):
#     a = {}
#     for i in x:
#         b = a.keys()
#         if i in b:
#             a[i] = a[i]+1
#         else:
#             a[i] = 1
#     return a
# z = funkcja("policz ilosc znakow")
# print(z)
# ------------------------------------------------------------------------------
# ĆWICZENIE
# Napisz funkcję w Pythonie, który zlicza ciągi znaków, w których długość ciągu wynosi 2 lub więcej,
# a pierwszy i ostatni znak są takie same z podanej listy ciągów.
# Przykładowa lista : ['abc', 'xyz', 'aba', '1221']
# Oczekiwany wynik: 2
#
# def ciag(x):
#     licznik = 0
#     for i in x:
#         if len(i) >= 2 and i[-1] == i[0]:
#             licznik = licznik + 1
#     return licznik
# print(ciag(['abc', 'xyz', 'aba', '1221']))
# -------------------------------------------------------------------------------
# ĆWICZENIE
# Funkcja Pythona do pobrania listy, posortowanej w porządku rosnącym według ostatniego elementu w
# każdej krotce z podanej listy niepustych krotek
# Przykładowa lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Oczekiwany wynik : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#
# def funkcja1(krotka):
#     return krotka[1]
# def sortowanie(lista):
#     posortowana = sorted(lista, key=funkcja1)
#     return posortowana
# print(sortowanie([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
# -------------------------------------------------------------------------------
# ĆWICZENIE
# Funkcja Pythona do pobrania ciągu znaków złożonego z pierwszych 2 i ostatnich 2 znaków z podanego ciągu
# Napisz funkcję w Pythonie, aby uzyskać łańcuch składający się z pierwszych 2 i ostatnich 2 znaków z
# danego łańcucha. Jeśli długość ciągu jest mniejsza niż 2, zwróć zamiast tego pusty ciąg.
# Przykładowy ciąg : Python
# Oczekiwany wynik: Pyon
# Przykładowy ciąg : Py
# Oczekiwany wynik: PyPy
# Przykładowy ciąg : P
# Oczekiwany wynik: pusty ciąg
#
# def ciag(x):
#     i = 0
#     if len(x) < 2:
#         return ""
#     else:
#         return x[:2] + x[-2:]
# print(ciag("Python"))
# --------------------------------------------------------------------------------
# Ćwiczenie
# Napisz program, policzy silnię dla liczby n tj n! = 1*2*3*4...*(n-2)*(n-1)*n
# Zrób to przez napisanie funkcji, która rekurencyjne będzie się odwoływała do samej
# siebie do momentu gdy będzie liczyła silnie dla 1, która wynosi 1.

# def silnia(n):
#     if n == 1:
#         return 1
#     # silnia(n) = silnia(n-1) * n
#     return silnia(n-1)*n
# print(silnia(3))
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Rekurencyjny ciąg Fibonacciego
#
# def ciag(n):
#     if n <=1:
#         return n
# #     n = (n-1)+(n-2)
#     return ciag(n-1) + ciag(n-2)
# print(ciag(5))
# ---------------------------------------------------------------------------------
#
# WYJATKI
# print(5 * (1/0))
# print(4 + x * 3)
# print('2' + 2)
# try:
#   ...
#   <linie kodu>
# except Exception as err:
#   <obsługa wyjątku>
# ---------------------------------------------------------------------------------
# import sys
# try:
#     f = open("plik.txt")
#     s = f.readline()
#     i = int(s.strip())  # Usuń spacje
#     print(i)
# except OSError as err:
#     print("Błąd systemu: {0}".format(err))
# except ValueError:
#     print("Nie można dokonać konwersji.")
# except:     # PEP 8: E722 nie używaj pustego 'except'
#     print("Nieoczekiwany wyjątek:", sys.exc_info()[0])
#     raise
# ---------------------------------------------------------------------------------
# try:
#     print("Dzień dobry")
# except:
#     print("Coś poszło nie tak")
# else:
#     print("Nic nie poszło źle")
# ---------------------------------------------------------------------------------
# try:
#     operacja_która_może_wyrzucić_ioerror()
# except IOError:
#     obsłuż_jakoś_wyjątek()
# else:    # nie chcemy złapać IOError, jeśli jest podniesiony
#     kolejna_operacja_która_może_wyrzucić_ioerror()
# finally:
#     coś_co_zawsze_trzeba_zrobić()
# ---------------------------------------------------------------------------------
# try:
#     print("x")
# except:
#     print("Coś poszło nie tak")
# finally:
#     print("Klauzula „try except" jest zakończona")
# ---------------------------------------------------------------------------------
#Blok try zgłosi błąd podczas próby zapisu do pliku tylko do odczytu::
#
# try:
#     file = open("demofile.txt")
#     try:
#         file.write("Lorum Ipsum")
#     except:
#         print("Coś poszło nie tak podczas ZAPISYWANIA do pliku")
#     finally:
#         file.close()
# except:
#     print("Coś poszło nie tak podczas OTWIERANIA pliku")
# ---------------------------------------------------------------------------------
# CWICZENIE 1
# Podczas pisania funkcji najlepiej jest przeprowadzić walidację liczb. Jeśli użytkownicy wprowadzą tekst, pojawi
# się błąd podczas próby konwersji na int. Napisz program, który poprosi użytkownika o podanie dwóch liczb. Dodaj
# i wydrukuj wynik. Jeśli nie zostanie wprowadzona liczba, zwróć komunikat o błędzie i poproś ponownie.
#
# while True:
#     try:
#         x= input("Podaj pierwsza liczbe: ")
#         y= input("Podaj druga liczbe: ")
#         print(int(x)+int(y))
#         break
#     except ValueError:
#         print("Error")
# ---------------------------------------------------------------------------------
# Wyjątek ZeroDivisionError z instrukcjami try except
# Ćwiczenie
# Podziel przez siebie dwie liczby # Umieść:
# result = "Nie możesz podzielić przez 0"
# we właściwym miejscu, aby program uniknął ZeroDivisionError
# Podpowiedź 1: Po prostu umieść przypisanie wartości dla wyniku po linii Except
# Podpowiedź 2: Zwróć uwagę na wcięcia
# a = 4
# b = 5
# try:
#     result = a/b
# except ZeroDivisionError:
#     result = "Nie możesz podzielić przez 0"
# print(result)
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Napisz dowolny kod. # Wychwyć w nim wyjątek, ale nic nie rób.
# Polecenie except, który nic nie robi
#
# a = 3
# b = "trzy"
# try:
#     result = a + b
# except TypeError:
#     pass
# ---------------------------------------------------------------------------------
# Wyjątek Exception z instrukcjami try except
# Ćwiczenie
# Spróbuj dodać int do ciągu. # Umieść:
# msg = "Nie możesz dodać int do string"
# aby program uniknął błędu BaseException. # Możesz użyć wyjątku Exception, chociaż zwykle powinno się
# ostrożnie używać tak potężnych instrukcji wyjątków.
# a = 5
# b = "a"
# try:
#     msg=a+b
# except SystemError:
#     msg = "Nie mozesz dodac int do string"
# print(msg)
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Stwórz trójelementową listę.
# Spróbuj wydrukować piąty element.
# Umieść:
# msg = "Jesteś poza zakresem listy"
# aby uniknąć wyjątku IndexError.
#
# x = [3, "cztery", 5.7]
# try:
#     msg = x[4]
# except IndexError as err:
#     msg = err
#     # msg = "Jesteś poza zakresem listy"
# print(msg)
# ---------------------------------------------------------------------------------
# Słowo kluczowe else
# Ćwiczenie
# Spróbuj otworzyć do czytania plik (podpowiedź: f = open(arg, "r")). # W razie braku możliwości otwarcia pliku,
# obsłuż wyjątek. # W przeciwnym przypadku wypisz:
# Nazwę pliku;
# Liczbę wierszy (podpowiedź: len(f.readlines()).
# Na koniec zamknij ten plik (podpowiedź: f.close()).
# arg = "nic.py"
# try:
#     f = open(arg, "r")
# except IOError:
#     print("Nie można otworzyć pliku")
# else:
#     print("Ilość wierszy: " + str(len(f.readlines())))
#     f.close()
# ---------------------------------------------------------------------------------
# Słowo kluczowe finally
#Ćwiczenie
# Użyj finally do zamykania obiektów i czyszczenia zasobów.
# Spróbuj otworzyć i zapisać (podpowiedź: write) w pliku, którego nie można zapisać.
# Zapewnij, aby program mógł kontynuować bez pozostawiania otwartego obiektu pliku.
#
# try:
#     f=open("f.txt", "r")
#     f.write("string")
# except IOError:
#     print("Cos poszlo nie tak")
# finally:
#     f.close()
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# f = open('write_file_name', 'w')
# f = open('append_file_name', 'a')
# f = open('read_file_name', 'r')
#
# f.read()
#
# f.readline()
# ---------------------------------------------------------------------------------
# f.write('Witaj\n')
# value = 42
# f.write(value)
#
# >>>Traceback (most recent call last):
# >>> File "<stdin>", line 1, in <module>
# >>>TypeError: must be str, not int
#
# s = str(value)
# f.write(s)
# ---------------------------------------------------------------------------------
# text.txt:
# Co to jest język Python?
# Python jest szeroko stosowanym dynamicznym językiem programowania wysokiego poziomu, ogólnego przeznaczenia. Jego filozofia projektowania kładzie nacisk na czytelność kodu, a jego składnia pozwala programistom na wyrażanie koncepcji w mniejszej liczbie wierszy kodu niż jest to możliwe w językach takich jak C++ lub Java.
# Python obsługuje wiele paradygmatów programowania, w tym programowanie obiektowe, imperatywne i funkcjonalne oraz style proceduralne. Posiada dynamiczny system typów i automatyczne zarządzanie pamięcią oraz dużą i wszechstronną bibliotekę standardową.
# Najlepszym sposobem nauki języka Python są ćwiczenia i pytania z ćwiczeniami.
# ---------------------------------------------------------------------------------
# Otwórz plik
# fo = open("text.txt", "r")
# print("Nazwa pliku: ", fo.name)
#
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Ponownie ustaw wskaźnik na początek
# fo.seek(0, 0)  # fo.seek(0)
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Zamknij otwarty plik
# fo.close()
# ---------------------------------------------------------------------------------
# Otwórz plik
# fo = open("text.txt", "r")
# print("Nazwa pliku: ", fo.name)
#
# # Uzyskaj aktualną pozycję pliku.
# pos = fo.tell()
# print("Aktualna pozycja: " + str(pos))
#
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Uzyskaj aktualną pozycję pliku.
# pos = fo.tell()
# print("Aktualna pozycja: " + str(pos))
#
# # Zamknij otwarty plik
# fo.close()
# ---------------------------------------------------------------------------------
# CWICZENIE
# Odczytywanie i wyświetlanie całego pliku tekstowego
# Napisz program w Pythonie, aby odczytać i wyświetlić cały plik tekstowy.
# ---------------------------------------------------------------------------------
# CWICZENIE
# Odczytywanie pliku wiersz po wierszu i zapisywanie go na liście
# Napisz program w Pythonie, który odczyta plik tekstowy wiersz po wierszu i zapisze go na liście content_list.
# content_list to lista zawierająca przeczytane wiersze.
# Możesz skorzystać z podpowiedzi (podanej dalej).

# Podpowiedź
# Instrukcja with w Pythonie jest używana w obsłudze wyjątków, aby kod był czystszy i
# bardziej czytelny. Upraszcza zarządzanie wspólnymi zasobami, takimi jak strumienie plików.
# Zwróć uwagę na następujący przykład kodu, w jaki sposób użycie instrukcji with sprawia, że kod
# jest czystszy.

# 1) bez użycia instrukcji with
# file = open('file_path', 'w')
# file.write('hello world !')
# file.close()

# 2) bez użycia instrukcji with
# file = open('file_path', 'w')
# try:
#     file.write('hello world')
# finally:
#     file.close()

# 3) używanie instrukcji with
# with open('file_path', 'w') as file:
# 	file.write('hello world !')

# Zauważ, że w przeciwieństwie do pierwszych dwóch implementacji, nie ma potrzeby
# wywoływania file.close() podczas używania instrukcji with. Sama instrukcja with zapewnia właściwe
# pozyskiwanie i uwalnianie zasobów. Wyjątek podczas wywołania file w pierwszej implementacji może
# uniemożliwić poprawne zamknięcie pliku, co może wprowadzić kilka błędów w kodzie, np. wiele zmian
# w plikach nie będzie obowiązywać, dopóki plik nie zostanie poprawnie zamknięty.

# Drugie podejście w powyższym przykładzie zajmuje się wszystkimi wyjątkami, ale użycie
# instrukcji with sprawia, że kod jest zwarty i znacznie bardziej czytelny. W ten sposób instrukcja
# with pomaga uniknąć błędów i wycieków, zapewniając, że zasób zostanie prawidłowo wydany, gdy
# kod korzystający z zasobu zostanie całkowicie wykonany. Instrukcja with jest powszechnie używana
# ze strumieniami plików, jak pokazano powyżej oraz z blokadami, gniazdami, podprocesami i telnetami
# itp.

# with open ("text.txt", "r") as tekst:
#     tresc = tekst.readlines()
#     print(tresc)
# ---------------------------------------------------------------------------------
# CWICZENIE
# Napisz program w Pythonie, który znajdzie najdłuższe słowa w pliku tekstowym.

# with open ("text.txt", "r") as text:
#     a = text.read()
# b = a.split()
# c = ""
# for n in b:
#     if len(n) > len(c):
#         c=n
# print(c)
# ---------------------------------------------------------------------------------
# CWICZENIE
# Napisz program w Pythonie, który zapisze listę do pliku.

# lista = ["a", "b", "c", "1", 1, 3]
# with open ("new.txt", "w") as file:
#     for i in lista:
#         file.write(str(i) + "\n")
# ---------------------------------------------------------------------------------
# CWICZENIE
# Napisz program w Pythonie, aby ocenić, czy plik jest zamknięty, czy nie.
#
# file = open ("new.txt", "r")
# print(file.closed)
# if not file.closed:
#     file.close()
# print(file.closed)
# ---------------------------------------------------------------------------------
# ZADANIE DOMOWE
# Napisz program, który otworzy plik sonety.txt i sprawdzi liczbę słów w całym tekście
# Dodatkowo, napisz funkcję, która zlicza słowa tylko w co 7 linijce tekstu
# ---------------------------------------------------------------------------------
#
# import os
# os.system("dir")
# ---------------------------------------------------------------------------------
# import time
# print("Dobranoc")
# time.sleep(2)
# print("Dzień dobry")
# ---------------------------------------------------------------------------------
# from time import sleep
# print("Dobranoc")
# sleep(2)
# print("Dzień dobry")
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Zaimportuj moduł matematyczny i wywołaj funkcję sinusoidalną.

# from math import sin, pi
# a = sin(pi*2)
# print(a)
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Tworzenie modułu (z przykładem) Aby utworzyć moduł, utwórz plik w języku Python
# Następnie zaimportuj go jak każdy inny moduł. Stwórz swój moduł (fruit.py)

# def lemon(l):
#     print('Lemoniada nr', l)

# Następnie stwórz swój program (example.py) i wywołaj funkcję:
# import fruit
# from fruit import lemon

# fruit.lemon(5)
# lemon(5)
# ---------------------------------------------------------------------------------
# def c_sum(x, y):
#     return x + y
# l_sum = lambda x, y: x + y
# print(c_sum(3, 4))
# print(l_sum(3, 4))
# ---------------------------------------------------------------------------------
# temperatury = [
#     37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
#     35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
#     39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
#     36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
#     33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
#     39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
#     34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
#     34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
#     34.2, 40.2, 34.3, 35.3
# ]
#
# wynik = list(filter(lambda x: x >= 40.0, temperatury))
# print(wynik)
# wynik_sort = sorted(wynik)
# print(wynik_sort)
# ---------------------------------------------------------------------------------
# from statistics import mean
# sr_temp = mean(temperatury)
# print(sr_temp)
#
# odch = list(map(lambda x: x - sr_temp, temperatury))
# print(odch)
#
# odch = list(map(lambda x: round(x - sr_temp, 1), temperatury))
# print(odch)
#
# from functools import reduce
# nums = [1, 2, 3, 4, 5]
# print(reduce(lambda a, b: a + b, nums))
# ---------------------------------------------------------------------------------
# szesciany = []
# for x in range(10):
#     szesciany.append(x**3)
# print(szesciany)
# ---------------------------------------------------------------------------------
# kwadraty = [el**2 for el in range(1, 102) if el % 2 != 0]
# print(kwadraty)
# ---------------------------------------------------------------------------------
# tekst = "abracadabra"
# wystapienia = {znak: tekst.count(znak) for znak in tekst}
# print(wystapienia)
# ---------------------------------------------------------------------------------
# list_comp = [x ** 0.5 for x in range(1, 11)]
# gene_expr = (x ** 0.5 for x in range(1, 11))
# for x in list_comp:
#     print(x)
# ---------------------------------------------------------------------------------
# list_comp = [x ** 0.5 for x in range(1, 50000001)]
# sum = 0
# for x in list_comp:
#     sum += x
# print(sum)
# ---------------------------------------------------------------------------------
# gene_expr = (x ** 0.5 for x in range(1, 50000001))
# # gene_expr nie obliczyło jeszcze tych milionów pierwiastków
# sum = 0
# for x in gene_expr:
#     # teraz już kolejne elementy wyrażenia generatorowego są obliczane
#     sum += x
# print(sum)
# ---------------------------------------------------------------------------------
# ĆWICZENIE
# Utwórz funkcję lambda, która przyjmuje jeden parametr (a) i zwraca go
#
# x = lambda a : a
# print(x(5))
# ---------------------------------------------------------------------------------
# ĆWICZENIE
# Napisz program w Pythonie, aby utworzyć funkcję lambda, która dodaje 15
# do podanej liczby przekazanej jako argument i zwraca to wynik. Następnie wydrukuj wynik.
#
# x = lambda a : a + 15
# print(x(7))
# ---------------------------------------------------------------------------------
# ĆWICZENIE
# Utwórz funkcję lambda, która mnoży argument x przez argument y i zwraca to wynik.
# Następnie wydrukuj wynik.

# r = lambda x, y: x * y
# print(r(3, 4))
# ---------------------------------------------------------------------------------
# ĆWICZENIE
# Napisz program w Pythonie wsparcia sortowania listy krotek za pomocą lambda po drugim elemencie

# subject_marks = [('Język angielski', 88),
#                  ('Nauka',           90),
#                  ('Matematyka',      97),
#                  ('Nauki społeczne', 82)]
#
# print(sorted(subject_marks, key = lambda krotka: krotka[1]))
# ---------------------------------------------------------------------------------
# ĆWICZENIE
# Napisz program w Pythonie, aby posortować za pomocą lambda listę słowników po kluczu model lub kolor.
#
# models = [{'marka': 'Nokia',   'model': '3310',   'kolor': 'Czarny'},
#           {'marka': 'Apple',   'model': '11',     'kolor': 'Złoty'},
#           {'marka': 'Samsung', 'model': 'Galaxy', 'kolor': 'Srebrny'}]
#
# print(sorted(models, key = lambda a: a['model']))
# ---------------------------------------------------------------------------------
# ĆWICZENIE
# Napisz program w Pythonie, aby sprawdzić, czy dany ciąg (str) zaczyna się od znaku ‘P’,
# używając lambda # Podpowiedź: skorzystaj z funkcji (metody) startswith()

# x = "Python"
# y = lambda i: i.startswith('P')
# print(y(x))
# ---------------------------------------------------------------------------------
# ĆWICZENIE
# Napisz program w Pythonie, aby wyodrębnić rok, miesiąc, dzień i godzinę za pomocą lambda
# Podpowiedź: skorzystaj z modułu datetime:
# now = datetime.datetime.now() - przypisuje do nowaktualną lokalną datę i godzinę.
# now.year - wyodrębnia i zwraca rok z now.
# now.month - wyodrębnia i zwraca miesiąc z now.
# now.day - wyodrębnia i zwraca dzień z now.
# now.time() - wyodrębnia i zwraca godzinę z now.

# import datetime
# now = datetime.datetime.now()
#
# year = lambda i: i.year
# month = lambda b: b.month
# day = lambda c: c.day
# hour = lambda d: d.time()
#
# print(year(now))
# print(month(now))
# print(day(now))
# print(hour(now))
# ---------------------------------------------------------------------------------
# ĆWICZENIE
# Napisz program w Pythonie, aby sprawdzić, czy dany ciąg jest liczbą, czy nie, używając lambda
# Podpowiedź: przydatna metoda to
# string.replace(oldvalue, newvalue, count)
# Składnia parametrów:
# oldvalue – Wymagany; ciąg do wyszukania
# newvalue – Wymagany; ciąg znaków, który ma zastąpić starą wartość
# count – Opcjonalny; liczba określająca, ile wystąpień starej wartości chcesz zastąpić;
# domyślnie są to wszystkie wystąpienia
#
# x = "4.50"
# y = lambda i: i.replace(".", "", 1).isdigit()
# z = lambda j: y(j[1:]) if j[0]== "-" else y(j)
# print(z(x))
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Napisz program w Pythonie do filtrowania listy liczb parzystych i nieparzystych całkowitych za pomocą lambda i filter
#
# lista = [1,2,3,4,5,6,7,8,9,10]
# wynik = list(filter(lambda x: x % 2 == 0, lista))
# print(wynik)
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Napisz program w Pythonie, aby znaleźć przecięcie dwóch podanych list za pomocą lambda i filter
#
# array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
# array_nums2 = [1, 2, 4, 8, 9]
# czesc_wspolna = list(filter(lambda x: x in array_nums1, array_nums2))
# print(czesc_wspolna)
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Napisz program w Pythonie, aby policzyć parzyste i nieparzyste liczby w danej tablicy liczb całkowitych, używając lambda i filter
#
# lista = [1,2,3,4,5,6,7,8,9,10]
# wynik = list(filter(lambda x: x % 2 == 0, lista))
# print(len(wynik))
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Napisz program w Pythonie, aby znaleźć wartości o długości sześć na podanej liście za pomocą funkcji lambda i filter
#
# weekdays = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
# wynik = list(filter(lambda x : len(x) == 6, weekdays))
# print(wynik)
# ---------------------------------------------------------------------------------
# Ćwiczenie
#
# Napisz program w Pythonie, aby znaleźć liczby podzielne przez dziewiętnaście lub trzynaście z listy liczb za pomocą lambda i filter
#
# nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# wynik = list(filter(lambda x : x % 19 == 0 or x % 13 == 0, nums))
# print(wynik)
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Napisz program w Pythonie, aby znaleźć palindromy na podanej liście ciągów za pomocą lambda i filter
# Palindrom – wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# Przykładem palindromu jest: „kobyła ma mały bok”
#
# texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
# palindrom = list(filter(lambda x: x[0:] == x[::-1],texts))
# print(palindrom)
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Napisz program w Pythonie, który zsumuje długość imion z danej listy imion po usunięciu imion zaczynających się od małej litery
# Użyj funkcji lambda
#
# sample_names = ['antoni', 'Jakub', 'zuzanna', 'Julia', 'Jan', 'szymon']
# duze_imiona = list(filter(lambda x: x[0].isupper() and x[1:].islower(), sample_names))
# x= ", ".join(duze_imiona)
# print(len(duze_imiona))
# print(len(x))
# print(x)
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Napisz program w Pythonie podnoszący do kwadratu i sześcianu każdą liczbę z podanej listy liczb całkowitych, używając lambda i map

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista = list(map(lambda x: x**2, nums))
# print(lista)
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Napisz program w Pythonie, aby dodać dwie podane listy za pomocą map i lambda
#
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# lista = list(map(lambda x,y: x+y ,nums1, nums2))
# print(lista)
# ---------------------------------------------------------------------------------
# Ćwiczenie
# Napisz program w Pythonie, który za pomocą funkcji lambdamnoży każdą liczbę z podanej listy przez określoną liczbę
# Wydrukuj wynik
#
# nums = [2, 4, 6, 9, 11]
# n = 2
# lista = list(map(lambda x: x*n , nums))
# print(lista)
# ---------------------------------------------------------------------------------
# Ćwiczenie
#
# Napisz program w Pythonie, który usuwa liczby dodatnie z podanej listy liczb. Zsumuj liczby ujemne i wydrukuj wartość bezwzględną
# za pomocą tworzenia listy – ang. list comprehension. Wydrukuj wynik
#
# nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
# print(abs(sum([x for x in nums if x<0])))
# ---------------------------------------------------------------------------------
# Ćwiczenie
#
# Napisz program w Pythonie, aby zmienić kolejność liczb dodatnich i ujemnych w danej liście (najpierw wszystkie ujemne,
# potem wszystkie dodatnie) za pomocą tworzenia listy – ang. list comprehension
#
# array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
# nums = [x for x in array_nums if x<0] + [x for x in array_nums if x>0]
# print(nums)
# ---------------------------------------------------------------------------------
# Ćwiczenie
#
# Napisz program w Pythonie, aby:
# Znaleźć liczby z podanego ciągu
# Zapisać je na liście
# Wyświetlić liczby w posortowanej formie
# Użyj funkcji tworzenia listy – ang. list comprehension, aby rozwiązać problem
#
# str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
# new_list = str1.split()
# numery = sorted([int(z) for z in new_list if z.isdigit()])
# print(numery)
# ---------------------------------------------------------------------------------
# PROGRAMOWANIE OBIEKTOWE

# x = 4
# print(type(x))
#
# x = 'Hello'
# print(type(x))
#
# x = 3.14565
# print(type(x))
#
# x = 4
# print(id(x))
#
# x = 'Hello'
# print(id(x))
#
# x = 4.14567
# print(id(x))
#
# lst = [1,2,3]
# print(id(lst))
# print(type(lst))
#
# L = [1,2,3]
# L.append(100)
# print(L)
#
# x = 4.5
# print(x.real, "+", x.imag, 'i')
#
# f = open("test.txt", "w")
# print(type(f))
#
# numbers = [6,9,3,1]
# print(sorted(numbers))
#
# x = 4.0
# print(x)
# print(type(x))
# print(x.real, "+", x.imag, 'i')
# print(x.is_integer())
# ---------------------------------------------------------------------------------
# KLASY
#
# class NazwaKlasy:
#     pass
#
# obiekt = NazwaKlasy()
# instancja = NazwaKlasy()
#
# print(type(obiekt))
# print(type(instancja))
# print(id(obiekt))
# print(id(instancja))
# print(obiekt)
# ---------------------------------------------------------------------------------
# class NazwaKlasy:
#     def nazwa_metody(self, argument1, argument2): # jedno wcięcie
#         print(argument1) # drugie wcięcie
#         print(argument2)
# obiekt = NazwaKlasy()
# obiekt.nazwa_metody("arg1", "arg2")
#
#
# """Dokumentacja modułu"""
#
# class MyClass:
#     """Dokumentacja klasy"""
#
#     def my_method(self):
#         """Dokumentacja metody"""
#
# def my_function():
#     """Dokumentacja funkcji"""
#
# help(MyClass)
# help(MyClass.my_method)
#
# class NazwaKlasy:
#     atrybut_pierwszy = "Wartość"
#     atrybut_drugi = 123.0
# class NazwaKlasy:
#     def __init__(self, trzeci):
#      self.atrybut_pierwszy = "Wartość"
#      self.atrybut_drugi = 123.0
#      self.atrybut_trzeci = trzeci
# instancja = NazwaKlasy("trzeci")
# print(instancja.atrybut_pierwszy)
# print(instancja.atrybut_drugi)
# print(instancja.atrybut_trzeci)
#
# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)
#
# class Parrot:
#     pass
# obj = Parrot()
# ---------------------------------------------------------------------------------
# class Parrot:
#
#     # atrybut klasy
#     species = "ptak"
#     # atrybut instancji
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# # utworzenie instancji klasy Parrot
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)
# # uzyskanie dostępu do atrybutów klasy
# print("Blu to", blu.__class__.species)
# print("Woo to również", woo.__class__.species)
# # za chwilę wytłumaczymy sobie dokładniej o co chodzi z __class__
# # uzyskanie dostępu do atrybutów instancji
# print(blu.name, "ma", blu.age, "lat")
# print(woo.name, "ma", woo.age, "lat")
# ---------------------------------------------------------------------------------
# class Parrot:
#
#     # atrybuty instancji
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # metoda instancji
#     def sing(self, song):
#         return self.name + " śpiewa " + song
#
#     def dance(self):
#         return self.name + " teraz tańczy"
# # utworzenie wystąpienia obiektu
# blu = Parrot("Blu", 10)
# ---------------------------------------------------------------------------------
#
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Person("Jan", 36)
# print(p1.name)
# print(p1.age)
# ---------------------------------------------------------------------------------
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Cześć, mam na imię " + self.name)
# p1 = Person("Jan", 36)
# p1.myfunc()
# ---------------------------------------------------------------------------------
#
# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age
#
#     def myfunc(abc):
#         print("Cześć, mam na imię " + abc.name)
# p1 = Person("Jan", 36)
# p1.myfunc()
# ---------------------------------------------------------------------------------
# CWICZENIE
# Klasa o nazwie MyClass z atrybutem o nazwie x No to jeszcze raz! Utwórz klasę o
# nazwie MyClass z atrybutem o nazwie x = 5. Teraz użyj klasy o nazwie MyClass do
# stworzenia obiektu. Utwórz obiekt o nazwie p1 i wydrukuj wartość x.
#
# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)
# ---------------------------------------------------------------------------------
# CWICZENIE
#
# class KontoBankowe:
#     def __init__(self, nazwa, stan = 0):
#         self.nazwa = nazwa
#         self.stan = stan
#
#     def info(self):
#         print("nazwa:", self.nazwa)
#         print("stan:", self.stan)
#
#     def wyplac(self, ilosc):
#         self.stan -= ilosc
#
#     def wplac(self, ilosc):
#         self.stan += ilosc
#
# jk = KontoBankowe("Jan Kowalski", 1000)
# jk.info()
# jk.wplac(2000)
# jk.wyplac(2500)
# jk.info()
# jk.stan = 0  # Dostęp do składowej `stan`
# jk.info()
# ---------------------------------------------------------------------------------
# CWICZENIE
# Klasa (class) dotycząca wyimaginowanego inwentarza odrzutowca jest już # dla Was
# zdefiniowana. Również instancja tej klasy Jets jest stworzona i przypisana do zmiennej first_item.
# Wydrukuj name z first_item.
# Wskazówka: Atrybut name można wywołać dodając go do instancji class, na
# przykład: anyinstance.name
#
# class Jets:
#
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
# first_item = Jets("F16", "USA")
#
# a=first_item.name
# print(a)
# ---------------------------------------------------------------------------------
# CWICZENIE
# Tym razem wydrukuj origin z first_item.
#
# class Jets:
#     model = None
#     country = 0
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
# first_item = Jets("F16", "USA")
#
# a=first_item.name
# b=first_item.origin
#
# print(a,b)
# ---------------------------------------------------------------------------------
# CWICZENIE
# Utwórz klasę Vehicle z atrybutami instancji max_speed i mileage. Stwórz obiekt i
# w trakcie inicjacji przypisz jego atrybutom (odpowiednio) wartości 240 i 18.
# Wydrukuj te atrybuty.
#
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
# a = Vehicle(240, 18)
#
# print(a.max_speed,",",a.mileage)
# ---------------------------------------------------------------------------------
# CWICZENIE
# Utwórz klasę Car z dwoma atrybutami instancji:
# .color, który przechowuje nazwę koloru samochodu jako ciąg testowy (str)
# .mileage, który przechowuje liczbę kilometrów przejechanych przez samochód jako liczbę całkowitą (int)
# Następnie utwórz instancję dwóch obiektów Car - niebieski samochód mający 20 000 kilometrów przebiegu
# i czerwony samochód mający 30 000 kilometrów przebiegu - i wydrukuj ich kolory oraz przebiegi.
# Twój wynik powinien wyglądać następująco:
# Niebieski samochód ma 20,000 kilometrów przebiegu.
# Czerwony samochód ma 30,000 kilometrów przebiegu.
#
# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
# x = Car(color = "niebieski" , mileage = 20000)
# y = Car(color = "czerwony", mileage =30000)
# z = Car(color = "zielony", mileage =40000)
# print(x.color, x.mileage)
# print(y.color, y.mileage)
# print(z.color, z.mileage)
#
# for petla in (x,y,z):
#     print(petla.color, petla.mileage)
# ---------------------------------------------------------------------------------
# CWICZENIE
# Stwórz nowe instancje od pierwszej do szóstej pozycji w tej kolejności: F14, SU 33, AJS37, Mirage 2000, Mig 29, A10.
# Możesz sprawdzić Podpowiedź 1, aby sprawdzić origin.
# Wskazówka 1
# SU33: Rosja
# AJS37: Szwecja
# Mirage2000: Francja
# F14: USA
# Mig29: ZSRR
# A10: USA
# Wskazówka 2
# Możesz utworzyć instancje w następujący sposób:
# first_item=Jets(name, country)
#
# class Jets:
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#     def x(self, drugi):
#         print(self.name, self.origin)
#         print(drugi.name, drugi.origin)
#
# first_item=Jets(name = "F14", country = "USA")
# second_item=Jets(name = "SU33", country = "Rosja")
# third_item=Jets(name = "AJS37", country = "Szwecja")
# fourth_item=Jets(name = "Mirage2000", country = "Francja")
# fifth_item=Jets(name = "Mig29", country = "ZSRR")
# sixth_item=Jets(name = "A10", country = "USA")
#
# first_item.x(second_item)
# third_item.x(second_item)
#
# first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
#
# print(first_army)
# ---------------------------------------------------------------------------------
# CWICZENIE
# Dodaj kolejny atrybut o nazwie „quantity” do metody inicjalizacji (zwykle nazywanej konstruktorem lub __init__).
# Następnie zdefiniuj przypisanie tego atrybutu do atrybutu self.quantity wewnątrz konstruktora.
# Następnie utwórz 2 instancje dla: F14 i Mirage2000 z ilościami 87 i 35.
# Wskazówka 1
# Możesz dodać parametr quantity do konstruktora w następujący sposób:
# def __init__(self, name, country, quantity):
# Następnie musisz przypisać ten parametr do atrybutu self, aby istniało sensowne połączenie między parametrem a atrybutem.
# Wskazówka 2
# Możesz dodać parametr quantity do konstruktora w następujący sposób:
# def __init__(self, name, country, quantity):
#
#     self.name = name
#     self.origin = country
#     self.quantity = quantity
# Następnie musisz przypisać ten parametr do atrybutu self, aby istniało sensowne połączenie między parametrem a atrybutem.
# Wskazówka 3
# Możesz tworzyć instancje klasy Jets jak poniżej:
# first_item=Jets("F14","USA",87)
# second_item=Jets("Mirage2000","France",35)
#
# class Jets:
#     def __init__(self, name, country, quantity):
#         self.name = name
#         self.origin = country
#         self.quantity = quantity
# first_item=Jets("F14","USA",87)
# second_item=Jets("Mirage2000","France",35)
#
# total= first_item.quantity + second_item.quantity
# print(total)
#
# OOP - dziedziczenie
#
# class KontoBankowe:
#     def __init__(self, nazwa, stan=0):
#         self.nazwa = nazwa
#         self.stan = stan
#
#     def info(self):
#         print("nazwa:", self.nazwa)
#         print("stan:", self.stan)
#
#     def wyplac(self, ilosc):
#         self.stan -= ilosc
#
#     def wplac(self, ilosc):
#         self.stan += ilosc
#
# class KontoDebetowe(KontoBankowe):
#     pass
#
# class KontoDebetowe(KontoBankowe):
#     def __init__(self, nazwa, stan=0, limit=0):
#         KontoBankowe.__init__(self, nazwa, stan)
#         self.limit = limit
#
#     def wyplac(self, ilosc):
#         """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
#         if (self.stan - ilosc) < (-self.limit):
#             print("Brak srodkow na koncie")
#         else:
#             KontoBankowe.wyplac(self, ilosc)
#
# account = KontoDebetowe("Jan Nowak", 0, 1000)
# account.info()
# account.wplac(500)
# account.info()
# account.wyplac(1000)
# account.info()
# account.wyplac(1000)
# account.info()
#
# # # bylo:
# # def __init__(self, nazwa, stan=0, limit=0):
# #     KontoBankowe.__init__(self, nazwa, stan)
# #     self.limit = limit
# #
# # # jest:
# # def __init__(self, nazwa, stan=0, limit=0):
# #     super().__init__(nazwa, stan)
# #     self.limit = limit
#
# class KontoDebetowe(KontoBankowe):
#     def __init__(self, nazwa, stan=0, limit=0):
#         super().__init__(nazwa, stan)
#         self.limit = limit
#
#     def wyplac(self, ilosc):
#         """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
#         if (self.stan - ilosc) < (-self.limit):
#             print("Brak srodkow na koncie")
#         else:
#             super().wyplac(ilosc)
# ---------------------------------------------------------------------------------
# class A:
#     """Rodzic pierwszy"""
#
#     def __init__(self):
#         super().__init__()
#         self.a = "A"
#
#     def fa(self):
#         print("a:", self.a)
#
# class B:
#     """Rodzic drugi"""
#
#     def __init__(self):
#         super().__init__()
#         self.b = "B"
#
#     def fb(self):
#         print("b:", self.b)
#
#
# class Pochodna(B, A):
#     """Dziecko"""
#
#     def __init__(self):
#         super().__init__()
#
# print(A.__doc__)
# print(B.__doc__)
# print(Pochodna.__doc__)
#
# d = Pochodna()
# print(d.a)
# print(d.b)
# d.fa()
# d.fb()
# ---------------------------------------------------------------------------------
# CWICZENIE - KOŁO
#
# import math
#
# class Figura:
#     def obwod(self):  # L
#         """Obliczanie obwodu."""
#         raise NotImplementedError
#
#     def pole(self):  # S/P
#         """Obliczanie pola powierzchni."""
#         raise NotImplementedError
#
# class Kolo(Figura):
#     def __init__(self, r):
#         self.r = r
#     def obwod(self):
#         return 2 * math.pi * self.r
#     def pole(self):
#         return self.r ** 2 * math.pi
#
# k = Kolo(5)
# o = Kolo(5)
# print(k.pole())
# print(o.obwod())
# ---------------------------------------------------------------------------------
# CWICZENIE - TRÓJKĄT
#
# import math
#
# class Figura:
#     def obwod(self):  # L
#         """Obliczanie obwodu."""
#         raise NotImplementedError
#
#     def pole(self):  # S/P
#         """Obliczanie pola powierzchni."""
#         raise NotImplementedError
#
# class Trojkat(Figura):
#     def __init__(self, a):
#         self.a = a
#     def obwod(self):
#         return 3 * self.a
#     def pole(self):
#         return self.a ** 2 * 3 **(1/2)/4
#
# p = Trojkat(3)
# print(p.obwod())
# print(p.pole())
# ---------------------------------------------------------------------------------
# CWICZENIE - PROSTOKĄT
#
# import math
#
# class Figura:
#     def obwod(self):  # L
#         """Obliczanie obwodu."""
#         raise NotImplementedError
#
#     def pole(self):  # S/P
#         """Obliczanie pola powierzchni."""
#         raise NotImplementedError
#
# class Prostokat(Figura):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def obwod(self):
#         return 2*self.a + 2*self.b
#     def pole(self):
#         return self.a * self.b

# p = Prostokat(3,4)
# print(p.obwod())
# print(p.pole())
#
# ---------------------------------------------------------------------------------
# CWICZENIE - KWADRAT - DZIEDZICZENIE PO PROSTOKACIE
#
# import math
#
# class Figura:
#     def obwod(self):  # L
#         """Obliczanie obwodu."""
#         raise NotImplementedError
#
#     def pole(self):  # S/P
#         """Obliczanie pola powierzchni."""
#         raise NotImplementedError
#
# class Kwadrat(Prostokat):
#     def __init__(self, a):
#         self.a = a
#         self.b = a
#     # def obwod(self):
#     #     return 4*self.a
#     # def pole(self):
#     #     return self.a ** 2
#
# p = Kwadrat(3)
# print(p.obwod())
# print(p.pole())
#
# ---------------------------------------------------------------------------------
# CWICZENIE - RÓWNOLEGŁOBOK
#
# import math
#
# class Figura:
#     def obwod(self):  # L
#         """Obliczanie obwodu."""
#         raise NotImplementedError
#
#     def pole(self):  # S/P
#         """Obliczanie pola powierzchni."""
#         raise NotImplementedError
#
# class Rownoleglobok(Figura):
#     def __init__(self, a, b, h):
#         self.a = a
#         self.b = b
#         self.h = h
#     def obwod(self):
#         return 2*self.a + 2*self.b
#     def pole(self):
#         return self.a * self.h
#
# p = Rownoleglobok(3,4,6)
# print(p.obwod())
# print(p.pole())
# ---------------------------------------------------------------------------------
# CWICZENIE - TRAPEZ PROSTOKĄTNY
#
# import math
#
# class Figura:
#     def obwod(self):  # L
#         """Obliczanie obwodu."""
#         raise NotImplementedError
#
#     def pole(self):  # S/P
#         """Obliczanie pola powierzchni."""
#         raise NotImplementedError
#
# class Trapez(Figura):
#     def __init__(self, a, b, c, d, h):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.h = h
#     def obwod(self):
#         return self.a + self.b + self.c + self.d
#     def pole(self):
#         return self.h * ((self.a + self.b)/2)
#
# p = Trapez(3,4,6,7,9)
# print(p.obwod())
# print(p.pole())
# ---------------------------------------------------------------------------------
# CWICZENIE
# Utwórz podrzędną klasę Bus, która odziedziczy wszystkie zmienne i metody klasy Vehicle
# Utwórz obiekt klasy Bus, która dziedziczy wszystkie zmienne i metody klasy Vehicle i wyświetli je.
# Oczekiwany wynik: Nazwa pojazdu: Szkolne Volvo Prędkość: 180 Przebieg: 12
#
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
# class Bus(Vehicle):
#     pass
# poj = Bus("Autobus szkolny", 180, 12)
# print(poj.mileage, poj.name, poj.max_speed)
# ---------------------------------------------------------------------------------
# CWICZENIE - dziedziczenie klas
# Utwórz klasę Bus, która dziedziczy po klasie Vehicle. Podaj argument pojemności w metodzie
# Bus.seating_capacity() o domyślnej wartości 50.
# Dane wejściowe:
# Użyj poniższego kodu dla swojej nadrzędnej klasy Vehicle.
# Musisz przesłonić/nadpisać metodę - w klasie pochodnej na specyficznie zaimplementować metodę
# która została już zdefiniowana w klasie bazowej.
#
# Oczekiwany wynik:
# Liczba miejsc siedzących w Szkolne Volvo to 50 pasażerów

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"Liczba miejsc siedzących w {self.name} to {capacity} pasażerów"
#
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity)
#
# k = Bus("bus", 80, 500)
# print(k.mileage, k.name, k.max_speed, k.seating_capacity())
# ---------------------------------------------------------------------------------
# CWICZENIE - Zdefiniuj atrybut (właściwość), który powinna mieć taką samą wartość
# dla każdej instancji klasy
# Zdefiniuj atrybut klasy „color” z domyślną wartością biały. Oznacza to, że każdy Vehicle (pojazd) powinien być biały.
# Użyj poniższego kodu do tego ćwiczenia.
# Oczekiwany wynik:
# Kolor: Biały, Nazwa pojazdu: Szkolne Volvo, Prędkość: 180, Przebieg: 12
# Kolor: Biały, Nazwa pojazdu: Audi Q5, Prędkość: 240, Przebieg: 18
# Podpowiedź: Zmienne utworzone w .__init__() nazywane są zmiennymi instancji. Wartość zmiennej instancji jest specyficzna dla konkretnego wystąpienia klasy.
# Na przykład w rozwiązaniu obiekty wszystkie obiekty Vehicle mają name i max_speed, ale  wartości
# zmiennych name i max_speed będą się różnić w zależności od instancji Vehicle. # Z drugiej
# strony atrybuty klasy to atrybuty, które mają tę samą wartość dla wszystkich instancji klas.
# Możesz zdefiniować atrybut klasy, przypisując wartość do nazwy zmiennej poza .__init__().
#
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#     kolor = "Biały"
#
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# bus = Bus("Volvo", 180, 12)
# car = Car("Audi", 240, 18)
#
# print(bus.kolor)
# print(car.kolor)
# ---------------------------------------------------------------------------------
# CWICZENIE
# Dane:
# Utwórz podrzędną klasę Bus, która dziedziczy po klasie Vehicle. Domyślna opłata za przejazd dla dowolnego pojazdu to liczba miejsc * 100.
# Natomiast jeśli School_bus to instancja klasy Bus, musimy dodać dodatkowe 10% do pełnej ceny jako opłatę za utrzymanie.
# Tak więc łączna opłata za przejazd autobusem stanie się ostateczną kwotą = opłata całkowita + 10% ceny całkowitej.
# Uwaga: autobus może pomieścić 50 osób, więc ostateczna kwota taryfy powinna wynosić 5500. Musisz zastąpić metodę fare() klasy Vehicle w klasie Bus.
# Użyj poniższego kodu dla swojej nadrzędnej klasy Vehicle. Musimy uzyskać dostęp do klasy nadrzędnej z wnętrza metody klasy potomnej.
#
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     def fare(self):
#         kwota = Vehicle.fare(self)
#         return kwota * 1.1
#
# school_bus = Bus("Szkolne Volvo", 12, 50)
# print("Całkowita opłata za przejazd autobusem wynosi:", school_bus.fare())
# ---------------------------------------------------------------------------------
# CWICZENIE
#
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("Szkolne Volvo", 12, 50)
# print(type(School_bus))
# --------------------------------------------------------------------------------------------------------
# ĆWICZENIA 07.02.2022 Z WOJTKIEM

# import sqlite3
# import io
#
# conn = sqlite3.connect('example.db')

# c = conn.cursor()

# c.execute("INSERT INTO stocks values('2022-02-07', 'BUY', 'RHAT', 100, 34.23)")
#
# conn.commit()
# conn.close()

# t = ('RHAT', )
# c.execute('SELECT * FROM stocks where symbol=?', t)
# print(c.fetchone())
#
# purchases = [
#     ('2022-01-07', 'BUY', 'IBM', 1000, 45.00),
#     ('2021-07-05', 'SELL', 'MSFT', 1000, 72.00),
#     ('2005-05-09', 'SELL', 'APPLE', 500, 53.00)
# ]
#
# c.executemany('INSERT INTO stocks values(?, ?, ?, ?, ?)', purchases)
#
# conn.commit()
#
# for row in c.execute('SELECT * from stocks order by price'):
#     print(row)
#
# with io.open('example_dump.sql', 'w') as f:
#     for line in conn.iterdump():
#         f.write('%s\n' % line)
# print('Kopia zapasowa zostala wykonana pomyslnie.')
# print('Zapisano jako example_dump.sql')
# conn.close()
#
# import numpy as np
#
# print(np.__version__)
# ---------------------------------------------------------------------------------
# tablica liczb zmiennoprzecinkowych
#
# np.array([4.1, 0, 1, 2, 3])
# np.array([range(i, i + 3) for i in [2, 4, 6]])

# Trzy wymiarowa tablica o wymiarach 2x3x4
# z losowymi liczbami całkowitymi z przedziału [0, 100)

# x = np.random.randint(100, size=(2, 3, 4))
# print(x)
#
# print(f"x dtype: {x.dtype}")  # typ danych przechowywanych w tablicy
# print(f"itemsize: {x.itemsize} bytes")  # rozmiar jednego elementu
# print(f"nbytes: {x.nbytes} bytes")  # rozmiar całej tablicy (itemsize x size)
#
# y = np.arange(0, 10)
# print(y)
#
# x = np.array([1, 2, 3])
# print(x.reshape((1, 3))) # dwuwymiarowa tablica z jednym wierszem i trzema kolumnami
# print(x.reshape((3, 1))) # dwuwymiarowa tablica z trzema wierszami i jedną kolumną
#
# x = np.array([1, 2, 3])
# y = np.array([3, 2, 1])
# np.concatenate([x, y])
