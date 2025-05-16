def slice_me(family: list, start: int, end: int) -> list:
    """
    Affiche la forme de la liste 2D 'family' et retourne une version tronquée
    selon les indices 'start' et 'end'.

    Args:
        family (list): Liste 2D à traiter.
        start (int): Indice de début du slicing.
        end (int): Indice de fin du slicing.

    Returns:
        list: Liste 2D tronquée.

    Raises:
        TypeError: Si 'family' n'est pas une liste de listes.
        ValueError: Si les sous-listes n'ont pas la même taille.
    """
    if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
        raise TypeError("family doit être une liste de listes.")
    row_lengths = [len(row) for row in family]

    if len(set(row_lengths)) != 1:
        raise ValueError("Toutes les sous-listes doivent avoir la même taille.")
    
    print(f"My shape is : ({len(family)}, {row_lengths[0]})")
    sliced = family[start:end]
    if sliced:
        print(f"My new shape is : ({len(sliced)}, {len(sliced[0])})")
    else:
        print("My new shape is : (0, 0)")
    return sliced
