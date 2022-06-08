import cv2 as cv
import numpy as np


def fill_holes(src):
    contours, hierarchy = cv.findContours(src, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    dst = np.zeros(src.shape, np.uint8)
    for index in range(len(contours)):
        cv.drawContours(dst, contours, index, 255, -1, 8, hierarchy, 0)
    return dst
