import cv2

# Affichage d'image 

img = cv2.imread('fire_force.jpg')

cv2.imshow('Image originel', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

def affichage_pixel (img, x, y):
    pixel_val = img[x, y]
    print(f"Valeur du pixel {x}, {y} : {pixel_val}")

def convertir_pixels_pairs(img):
    img_paire = img.copy()
    img_paire = img_paire - (img_paire % 2)
    return img_paire

affichage_pixel(img, 60, 100)

img_pairs = convertir_pixels_pairs(img)
cv2.imshow('Image convertie (valeurs paires)', img_pairs)
cv2.waitKey(0)
cv2.destroyAllWindows()

affichage_pixel(img_pairs, 60, 100)




# def text_to_binary(text) :
#     binary_result = "".join(format(ord(char), '08b') for char in text)
#     return binary_result


# if __name__ == "__main__":
#     message = input("Entrer un message à convertir en binaire :")

# print(f"Texte original : {message}")
# print(f"Binaire : {text_to_binary(message)}")