import cv2 as cv
import numpy as np
img = cv.imread("apple.jpeg", cv.IMREAD_GRAYSCALE)


def diagonal(img):

    a, b = img.shape
    right_diagonal = np.zeros(a)
    left_diagonal = np.zeros(a)

    k = 0
    l = 0
    for j in range(100):
        if(img[j][j] != 'nan'):
            right_diagonal[k] = img[j][j]
            k = k+1
        if(img[j][99-j] != 'nan'):
            left_diagonal[l] = img[j][99-j]
            l = l+1

    return right_diagonal, (np.sum(right_diagonal)/100), left_diagonal, (np.sum(left_diagonal)/100)


def rows(img):
    a, b = img.shape
    first_thirty = np.zeros(a)
    last_thirty = np.zeros(a)

    k = 0
    l = 0
    for i in range(30):
        for j in range(100):
            if(img[i][j] != 'nan'):
                first_thirty[k] = img[i][j]
                k = k+1
            if(img[i+69][j] != 'nan'):
                last_thirty[l] = img[i+69][j]
                l = l+1
    return first_thirty, np.sum(first_thirty)/3000, last_thirty, np.sum(last_thirty)/3000


def cols(img):
    a, b = img.shape
    first_thirty = np.zeros(a)
    last_thirty = np.zeros(a)

    k = 0
    l = 0
    for i in range(100):
        for j in range(30):
            if(img[i][j] != 'nan'):
                first_thirty[k] = img[i][j]
                k = k+1
            if(img[i][j+69] != 'nan'):
                last_thirty[l] = img[i][j+69]
                l = l+1
    return first_thirty, np.sum(first_thirty)/3000, last_thirty, np.sum(last_thirty)/3000


right_diag, right_sum, left_diag, left_sum = diagonal(img)
first_thiry_rows, sum_first_thiry, last_thiry_rows, sum_last_thiry = rows(img)
first_thiry_cols, sum_first_thiry, last_thiry_cols, sum_last_thiry = cols(img)
