import cv2

img = cv2.imread('fire_force.jpg')

cv2.imshow('Image', img)

cv2.waitKey(0)

def affichage_pixel (img, x, y):
    pixel_val = img[x, y]
    print(f"Valeur du pixel {x}, {y} : {pixel_val}")

affichage_pixel(img, 60, 100)