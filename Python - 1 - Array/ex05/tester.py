from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
# from pimp_image import ft_grey
import matplotlib.pyplot as plt


array = ft_load("landscape.jpg")
arrayNames = []
arrayNames.append(ft_invert(array))
arrayNames.append(ft_red(array))
arrayNames.append(ft_green(array))
arrayNames.append(ft_blue(array))
# arrayNames.append(ft_grey(array))
print(ft_invert.__doc__)


for name_array in arrayNames:
    plt.imshow(name_array, cmap='gray')
    plt.show()