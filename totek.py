        #importowanie
import random

        #Pokazanie możliwości losów
print('wybierz pojedynczo 6 liczb z poniżej podanych')
print('|01|02|03|04|05|06|07|08|09|10|')
print('|11|12|13|14|15|16|17|18|19|20|')
print('|21|22|23|24|25|26|27|28|29|30|')
print('|31|32|33|34|35|36|37|38|39|40|')
print('|41|42|43|44|45|46|47|48|49|..|')


def user(a=6, n=0, lista=None):
    if lista is None: 
        lista = []
    
    while a > n:
        try:
            liczba = int(input(f'Podaj liczbę ({n+1}/{a}) ---> '))
            if liczba < 1 or liczba > 49:
                print('Liczba',liczba,' nie znajduje się w zakresie 1-49!')

            elif liczba in lista:
                print('!! Ta liczba jest już w liście !!')

            else:
                lista.append(liczba)
                n += 1  

        except ValueError:
            print('To nie jest liczba! Spróbuj ponownie.')

    return lista  

def losowe():
    losowe = []
    losowe.append = random.sample(range(1, 50), 6)

"""def sortowanie():
    wynik.sort()
    lotto.sort()"""






# Uruchomienie programów
wynik = user()
lotto = losowe()
"""Lsort = sortowanie()"""

print('Twoja lista liczb punktów -->',)
print('Twoja lista liczb to -->', wynik)
print('Wylosowanie liczby to -->', lotto)