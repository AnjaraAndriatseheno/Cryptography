import cv2
import numpy as np

def affichage_pixel(img, x, y):
    print(f"Valeur du pixel ({x},{y}) :", img[y, x])

def convertir_pixels_pairs(img):
    return img - (img % 2)

def encoder_message(img, message_binaire):
    img_encoded = img.copy()
    h, w, _ = img.shape
    index = 0

    for y in range(h):
        for x in range(w):
            for c in range(3):
                if index >= len(message_binaire):
                    return img_encoded
                bit = int(message_binaire[index])
                if bit == 1 and img_encoded[y, x, c] % 2 == 0:
                    img_encoded[y, x, c] += 1
                index += 1
    return img_encoded

def text_to_binary(text):
    return "".join(format(ord(char), '08b') for char in text)

if __name__ == "__main__":
    img = cv2.imread('fire_force.jpg')

    img_pairs = convertir_pixels_pairs(img)
    cv2.imwrite("image_pairs.png", img_pairs)

    affichage_pixel(img_pairs, 60, 100)

    message = input("Message à encoder : ")
    message_bin = text_to_binary(message)

    print("Message en binaire :", message_bin)

    img_encoded = encoder_message(img_pairs, message_bin)
    cv2.imwrite("image_encodee.png", img_encoded)

    affichage_pixel(img_encoded, 60, 100)

    print("Images générées : image_pairs.png et image_encodee.png")
