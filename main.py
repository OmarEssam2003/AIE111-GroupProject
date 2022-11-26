import os
import ImageProcessing as IP
import PathFindingAlgorithms as PF


def main():
    # path = IP.GetPathOfImage()
    PIXELS = IP.TranslateImageTo2DArray(r"C:\Users\user\OneDrive\Desktop\debug.jpg")
    # returns a 2d numpy array
    print(PIXELS)


if __name__ == "__main__":
    main()
