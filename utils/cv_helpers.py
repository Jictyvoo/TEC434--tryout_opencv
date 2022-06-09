import cv2 as cv
import numpy as np
from models.contours import Contours


def fill_holes(src: cv.Mat) -> cv.Mat:
    contours, hierarchy = cv.findContours(src, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    dst = np.zeros(src.shape, np.uint8)
    for index in range(len(contours)):
        cv.drawContours(dst, contours, index, 255, -1, 8, hierarchy, 0)
    return dst


def extract_from_mask(image: cv.Mat, mask: cv.Mat) -> cv.Mat:
    return cv.bitwise_and(image, image, mask=fill_holes(mask))


def draw_contours(image: cv.Mat, contours: Contours, is_small: bool = False) -> cv.Mat:
    # Extract image in given contours
    contour_arr = []
    if is_small:
        contour_arr = contours.smallest
    else:
        contour_arr = contours.biggest
    contours_image = cv.drawContours(image, [contour_arr], 0, (0, 255, 0), 3)
    return contours_image
