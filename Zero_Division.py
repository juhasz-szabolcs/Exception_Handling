osztando = 10
try:
    oszto = int(input(f"Mennyivel osszam el a {osztando}-es számot? "))
    print(f"A két szám osztásának eredménye: {osztando/oszto}")
except ZeroDivisionError:
    print("Nullával nem osztunk")
