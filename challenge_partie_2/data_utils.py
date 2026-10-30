'''Mon module incluant basiques des mathématiques et statistiques utiles'''

PI = 3.141592653589793      # Rapport constant entre la circonférence d'un cercle
E = 2.718281828459045       # Le nombre d'Euler, qui sert de base aux logarithmes naturels (népériens)

def carre(x):
    """Retourne le carré de x."""
    return x ** 2


def cube(x):
    """Retourne le x au cube."""
    return x ** 3


def factorielle(n):
    """Renvoie n! (n doit être un entier non négatif)."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def valeur_absolue(x):
    """Renvoie la valeur absolue de x."""
    if x < 0:
        return -x
    return x


def maximum(liste):
    """Renvoie le plus grand élément d'une liste."""
    biggest = liste[0]
    for value in liste:
        if value > biggest:
            biggest = value
    return biggest


def minimum(liste):
    """Renvoie le plus petit élément d'une liste."""
    smallest = liste[0]
    for value in liste:
        if value < smallest:
            smallest = value
    return smallest


def moyenne(liste):
    """Renvoie la moyenne d'une liste de nombres."""
    return sum(liste) / len(liste)


def ecart_type(liste):
    """Renvoie l'écart-type (de la population) d'une liste de nombres."""
    mean = moyenne(liste)
    total = 0
    for x in liste:
        total += (x - mean) ** 2
    variance = total / len(liste)
    return variance ** 0.5


def mediane(liste):
    """Renvoie la médiane d'une liste de nombres."""
    sorted_list = sorted(liste)
    n = len(sorted_list)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_list[middle - 1] + sorted_list[middle]) / 2
    return sorted_list[middle]
