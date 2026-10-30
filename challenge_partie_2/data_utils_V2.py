"""Deuxième version du module utilitaire (nouvelles fonctions)."""


def somme_cumulee(liste):
    """Renvoie la somme cumulée d'une liste sous forme de liste : [1, 2, 3] -> [1, 3, 6]."""
    result = []
    total = 0
    for value in liste:
        total += value
        result.append(total)
    return result


def compter_occurrences(liste):
    """Renvoie un dictionnaire avec le nombre d'occurrences de chaque élément."""
    counts = {}
    for element in liste:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts


def inverser_dict(dictionnaire):
    """Inverse les clés et les valeurs d'un dictionnaire : {'a': 1} -> {1: 'a'}."""
    inverted = {}
    for key, value in dictionnaire.items():
        inverted[value] = key
    return inverted


def filtrer_pairs(liste):
    """Renvoie une nouvelle liste contenant uniquement les nombres pairs de la liste d'entrée."""
    evens = []
    for number in liste:
        if number % 2 == 0:
            evens.append(number)
    return evens


def celsius_to_fahrenheit(celsius):
    """Convertit une température de Celsius en Fahrenheit."""
    return celsius * 9 / 5 + 32


def trouver_doublons(liste):
    """Renvoie les éléments qui apparaissent plus d'une fois (chaque élément listé une seule fois)."""
    duplicates = []
    for element in liste:
        if liste.count(element) > 1 and element not in duplicates:
            duplicates.append(element)
    return duplicates


def calculer_moyenne_ponderee(valeurs, poids):
    """Renvoie la moyenne pondérée des valeurs avec les poids correspondants (arrondie à 2 décimales)."""
    total = 0
    for i in range(len(valeurs)):
        total += valeurs[i] * poids[i]
    return round(total / sum(poids), 2)


'''Partie Bonus'''

def analyser_texte(texte):
    """Renvoie un dictionnaire de statistiques sur un texte."""
    mots = []
    for mot in texte.split():
        mots.append(mot.strip(".,;:!?"))  # Supprime la ponctuation autour de chaque mot

    plus_long = mots[0]
    total_lettres = 0
    for mot in mots:
        total_lettres += len(mot)
        if len(mot) > len(plus_long):
            plus_long = mot

    return {
        "total_mots": len(mots),
        "caracteres_avec_espaces": len(texte),
        "caracteres_sans_espaces": len(texte.replace(" ", "")),
        "mot_le_plus_long": plus_long,
        "longueur_moyenne_mot": round(total_lettres / len(mots), 2),
    }
