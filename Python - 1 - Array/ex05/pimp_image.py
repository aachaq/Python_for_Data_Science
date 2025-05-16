import numpy as np
import matplotlib.pyplot as plt
import array

def ft_invert(array) -> array:
    """
    Inverts the color of the image received.
    """
    result = 255 - array
    return result

def ft_red(array) -> array:
    """
    Keeps only the red channel of the image.
    """
    result = array * [1, 0, 0]  # garde R, met G et B à 0
    return result

def ft_green(array) -> array:
    """
    Keeps only the green channel of the image.
    """
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]  # R - R = 0
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]  # B - B = 0
    return result

def ft_blue(array) -> array:
    """
    Keeps only the blue channel of the image.
    """
    result = array.copy()
    result[:, :, 0] = 0  # red = 0
    result[:, :, 1] = 0  # green = 0
    return result

