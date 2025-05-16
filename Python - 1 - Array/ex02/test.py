from PIL import Image
import numpy as np
import os


# Ouvre l'image
image = Image.open("landscape.jpg")

# Convertit en tableau numpy
image_array = np.array(image)

# Affiche la forme (dimensions)
print("Forme du tableau :", image_array.shape)

# Affiche un aperçu du tableau
print(image_array)


# with open("/home/aachaq/Desktop/python_for_data_science/Python_for_Data_Science_github/Python - 1 - Array/ex02/landscape.jpg", "rb") as fichier:
#     contenu = fichier.read()
# ()
# # img = fichier.convert('RGB')


# print(contenu)
# fichier.close
