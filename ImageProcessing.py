import os
from numpy import asarray
import cv2
import matplotlib.pyplot as plt


def GetPathOfImage():
    # work on that
    return 1


def TranslateImageTo2DArray(path):
    original = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    (thresh, black_white) = cv2.threshold(original, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    half_sized = cv2.resize(black_white, (0, 0), fx=0.5, fy=0.5)

    return asarray(half_sized)
