import cv2
import numpy as np

img = cv2.imread("cara.jpg")
img_c = cv2.resize(img,(500,650))

def F_H(img, Blue, Green, Red):
    L_img = np.shape(img)
    H = np.zeros((L_img[0], L_img[1]))
    for j in range(0, L_img[1]):
        for i in range(0, L_img[0]):
            b = Blue[i, j]
            g = Green[i, j]
            r = Red[i, j]
            aux1 = .5 * ((r - g) + (r - b))
            aux2 = np.sqrt(((r - g) ** 2) + ((r - b) * (g - b)))
            if aux1 == 0 or aux2 == 0:
                aux3 = 0
            else:
                aux3 = aux1 / aux2
            H[i, j] = np.arccos(aux3)
    return H

def F_S(img, Blue, Green, Red):
    L_img = np.shape(img)
    S = np.zeros((L_img[0], L_img[1]))
    for j in range(0, L_img[1]):
        for i in range(0, L_img[0]):
            b = Blue[i, j]
            g = Green[i, j]
            r = Red[i, j]
            aux1 = min(r, g, b)
            aux2 = r + g + b
            if aux1 == 0 or aux2 == 0:
                aux3 = 0
            else:
                aux3 = aux1 / aux2
            S[i, j] = 1 - 3 * aux3
    return S

def F_I(img, Blue, Green, Red):
    L_img = np.shape(img)
    I = np.zeros((L_img[0], L_img[1]))
    for j in range(0, L_img[1]):
        for i in range(0, L_img[0]):
            b = Blue[i, j]
            g = Green[i, j]
            r = Red[i, j]
            if b == 0 and g == 0 and r == 0:
                I[i, j] = 0
            else:
                I[i, j] = (1 / 3) * (b + g + r)
    return I

BGR = np.float32(img_c)/255
Blue, Green, Red = cv2.split(BGR)
H = F_H(img_c, Blue, Green, Red)
S = F_S(img_c, Blue, Green, Red)
I = F_I(img_c, Blue, Green, Red)
HSI = cv2.merge([H, S, I])
L_img = np.shape(img_c)
H_bin = np.zeros((L_img[0], L_img[1]))
for j in range(0, L_img[1]):
    for i in range(0, L_img[0]):
        if H[i, j] < .358:
            H_bin[i, j] = 1
        else:
            H_bin[i, j] = 0

cv2.imshow('Imagen recortada',img_c)
cv2.imshow("Blue", Blue)
cv2.imshow("Green", Green)
cv2.imshow("Red", Red)
cv2.imshow('HSI',HSI)
cv2.imshow("H", H)
cv2.imshow("S", S)
cv2.imshow("I", I)
cv2.imshow("Imagen binaria", H_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()