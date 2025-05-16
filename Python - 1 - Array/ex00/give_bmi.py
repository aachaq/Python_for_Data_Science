def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calcule l'IMC pour chaque paire (taille, poids).

    Args:
        height (List[int | float]): Liste des tailles en mètres.
        weight (List[int | float]): Liste des poids en kilogrammes.

    Returns:
        List[float]: Liste des IMC calculés.
    """
    if len(height) != len(weight):
        raise ValueError("Les listes 'height' et 'weight' doivent avoir la même longueur.")

    bmi_list = []

    for h, w in zip(height, weight):
        if not isinstance(h, int | float) or not isinstance(w, int | float):
            raise ValueError("Les éléments des listes doivent être des entiers ou des flottants.")
        if h <= 0:
            raise ValueError("La taille doit être un nombre positif non nul.")
        bmi = w / (h ** 2)
        bmi_list.append(bmi)
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Vérifie si chaque IMC dépasse une limite donnée.

    Args:
        bmi (list[int | float]): Liste des valeurs d'IMC.
        limit (int): Limite à comparer.

    Returns:
        list[bool]: Liste de booléens indiquant si chaque IMC dépasse la limite.

    Raises:
        TypeError: Si 'limit' n'est pas un entier.
    """
    if not isinstance(limit, int):
        raise TypeError("La limite doit être un entier.")
    
    result = []
    for value in bmi:
        if not isinstance(value, int | float):
            raise TypeError("Les éléments de la liste 'bmi' doivent être des entiers ou des flottants.")
        result.append(value > limit)
    return result
