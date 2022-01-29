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

