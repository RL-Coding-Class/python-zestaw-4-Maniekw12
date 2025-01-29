from multipledispatch import dispatch
import math

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    def __init__(self, x: int, y: int):
        super().__init__()
        print("Prostokat init")
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    def __init__(self, x: int):
        super().__init__(x, x)
        print("Kwadrat init")

class Kolo(Figura):
    def __init__(self, r: float):
        super().__init__()
        print("Kolo init")
        self.r = r



@dispatch(Figura)
def pole(fig: Figura):
    """Domyślna wersja dla klasy Figura"""
    print("pole(Figura) - domyślna implementacja")
    return 0

@dispatch(Prostokat)
def pole(p: Prostokat):
    print("pole(Prostokat) - bez zmiany")
    return p.x * p.y

@dispatch(Prostokat, int, int)
def pole(p: Prostokat, x: int, y: int):
    print("pole(Prostokat, int, int) - zmiana wymiarów")
    p.x = x
    p.y = y
    return p.x * p.y

@dispatch(Kwadrat)
def pole(k: Kwadrat):
    print("pole(Kwadrat) - bez zmiany")
    return k.x * k.y  # w Kwadracie x == y

@dispatch(Kwadrat, int)
def pole(k: Kwadrat, bok: int):
    print("pole(Kwadrat, int) - zmiana boku")
    k.x = bok
    k.y = bok
    return k.x * k.y

@dispatch(Kolo)
def pole(k: Kolo):
    print("pole(Kolo) - bez zmiany")
    return math.pi * (k.r ** 2)

@dispatch(Kolo, float)
def pole(k: Kolo, r: float):
    print("pole(Kolo, float) - zmiana promienia")
    k.r = r
    return math.pi * (k.r ** 2)


def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(f"Pole obiektu: {pole(i)}")


if __name__ == "__main__":
    # Tworzenie obiektów
    print("=== Tworzenie obiektów ===")
    a, b, c, d = Figura(), Prostokat(2, 4), Kwadrat(2), Kolo(3)

    # Wywołania funkcji pole
    print("\n=== Wywołania funkcji pole ===")
    print(f"Pole prostokąta (2x4): {pole(b)}")
    print(f"Pole kwadratu (bok=2): {pole(c)}")
    print(f"Pole koła (r=3): {pole(d)}")

    # Zmiana wymiarów za pomocą funkcji pole
    print("\n=== Zmiana wymiarów ===")
    print(f"Pole prostokąta po zmianie na 5x6: {pole(b, 5, 6)}")
    print(f"Pole kwadratu po zmianie boku na 7: {pole(c, 7)}")
    print(f"Pole koła po zmianie promienia na 4: {pole(d, 4.0)}")

    # Polimorfizm
    print("\n=== Polimorfizm w czasie wykonywania ===")
    polaPowierzchni([a, b, c, d])
