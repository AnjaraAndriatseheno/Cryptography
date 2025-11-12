# Chiffrement de César

# def cesar_uncypher(cypted_message, key):
#     return cesar_cypher(crypted_message, key)

# message = "chocolat"
# crypted_message = cesar_cypher(message, 53120000)



def cesar(string, decalage):
    lower_string = [char.lower() if char.isupper() else char for char in string]
    result = ""
    for char in lower_string:
        if char.isalpha():
            # on décale le caractère 
            shifted = ord(char) + decalage
            # si le décalage dépasse z on retourne au début 
            if shifted > ord('z'):
                shifted = shifted - 26
            # si le on le décalage est inférieur à a on va à la fin
            elif shifted < ord('a'):
                shifted = shifted + 26
            # le caractère décalé s'ajoute au résultat
            result += chr(shifted)
        else:
            result += char
    return result

    def normalize_input(word):
        lower_word = [element.lower() if type(element) == str else element for element in word]
        return lower_word 
# Déchiffrement de César
def decesar(string, decalage):
    return cesar(string, -decalage)
# -> Va nous sortir toutes les décalage de 1 à 25 (26 exclu)
def brute_force(string):
    for decalage in range(26):
        print(f'Décalage {decalage} : {decesar(string, decalage)}') 
        
# Chiffrement de vigenère
def vigenere(string, key):
    # Convertir tout en minuscules (plus simple qu'une condition ternaire)
    string = string.lower()
    key = key.lower()
    if not key:
        raise ValueError('La clé ne peut pas être vide')
    if not key.isalpha():
        raise ValueError('La clé ne doit contenir que des lettres')

    result = ""  # Chaîne pour accumuler le résultat
    key_length = len(key)

    #  -> Parcourir chaque lettre du message net
    for i, char in enumerate(string):
        # NE TRAITE QUE LES LETTRES (ignore espaces, chiffres, accents...)
        if char.isalpha():
         # Convertir lettre en indice (A = 0, B= 1, ..., Z = 25)
            indice = ord(char) - ord('a')  # 0-25
            indice_key = ord(key[i % key_length]) - ord('a')  # Clé répétée
            # Calculer l'indice crypté (modulo 26 pour rester dans l'alphabet)
            indice_crypted = (indice + indice_key) % 26
            result += chr(indice_crypted + ord('a'))  # Ajouter à la chaîne (pas réaffecter)
        else:
            # Conserver les caractères non alphabétiques (espaces, ponctuation...)
            result += char

    return result 
# Déchiffrement de Vigenère
def devigenere(string, key):
    string = string.lower()
    key = key.lower()

    if not key:
        raise ValueError('La clé ne peut pas être vide')
    if not key.isalpha():
        raise ValueError('La clé ne doit contenir que des lettres')

    result = ""  # Utiliser une chaîne (plus simple que une liste pour cet usage)
    key_length = len(key)

    for i, char in enumerate(string):
        if char.isalpha():
            indice = ord(char) - ord('a')
            indice_key = ord(key[i % key_length]) - ord('a')
            # Calcul inverse (ajouter 26 avant modulo pour éviter les négatifs)
            indice_decrypted = (indice - indice_key + 26) % 26
            result += chr(indice_decrypted + ord('a'))  # Ajouter à la chaîne
        else:
            # Conserver les caractères non alphabétiques
            result += char

    return result 