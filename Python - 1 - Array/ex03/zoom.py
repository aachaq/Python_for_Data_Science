from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def ft_zoom(img: np.ndarray) -> np.ndarray:
    """
    Zoom sur la zone du visage de l'animal (400x400) en niveaux de gris.
    """
    try:
        start_y = 90
        end_y = start_y + 400
        start_x = 420
        end_x = start_x + 400

        zoomed = img[start_y:end_y, start_x:end_x, 0]
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        return zoomed
    except Exception as e:
        print(f"Erreur lors du zoom: {e}")
        return None


def display_image(img: np.ndarray):
    """
    Affiche l'image zoomée en noir et blanc avec les axes X/Y.
    """
    try:
        plt.imshow(img, cmap='gray')
        plt.show()
    except Exception as e:
        print(f"Erreur d'affichage: {e}")

def main():
    image = ft_load("animal.jpeg")
    if image is not None:
        zoomed = ft_zoom(image)
        if zoomed is not None:
            display_image(zoomed)


if __name__ == "__main__":
    main()
