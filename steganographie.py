import cv2

# Affichage d'image 

img = cv2.imread('fire_force.jpg')

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

def affichage_pixel (img, x, y):
    pixel_val = img[x, y]
    print(f"Valeur du pixel {x}, {y} : {pixel_val}")

# def convert_pixel (pixel_val) : 
#     if pixel_val % 2 == 0 : 
#         pixel_val = pixel_val+ 1
#         print(pixel_val)
#     else : 
#         print(pixel_val)

# affichage_pixel(img, 60, 100)




def text_to_binary(text) :
    binary_result = "".join(format(ord(char), '08b') for char in text)
    return binary_result


if __name__ == "__main__":
    message = input("Entrer un message à convertir en binaire :")

print(f"Texte original : {message}")
print(f"Binaire : {text_to_binary(message)}")