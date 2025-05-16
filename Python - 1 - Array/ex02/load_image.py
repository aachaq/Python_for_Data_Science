from PIL import Image
import numpy as np
import array


def ft_load(path: str) -> array:
    """
    Charge une image, affiche son format et retourne son contenu en RGB.

    Args:
        path (str): Chemin vers le fichier image.

    Returns:
        np.ndarray: Tableau NumPy représentant l'image en RGB.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
        ValueError: Si le format de l'image n'est pas pris en charge.
        Exception: Pour d'autres erreurs lors du chargement de l'image.
    """
    try:
        with Image.open(path) as img:
            if img.format not in ['JPEG', 'JPG']:
                raise ValueError(f"Format d'image non pris en charge: {img.format}")
            
            img = img.convert('RGB')
            data = np.array(img)
            print(f"The shape of image is: {data.shape}")
            return data
    except FileNotFoundError:
        print(f"Erreur: Le fichier '{path}' est introuvable.")
    except ValueError as ve:
        print(f"Erreur: {ve}")
    except Exception as e:
        print(f"Erreur lors du chargement de l'image: {e}")
    return None
