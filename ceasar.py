from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def print_logo():
    print(logo)

def encrypt(word, shift):
    enc_word = ""
    for i in word:
        alphabet_index = (alphabet.index(i) + shift) % len(alphabet)
        enc_word += alphabet[alphabet_index]
    print(f"Encrypted word: {enc_word}")

def decrypt(word,shift):
    dec_word = ""
    for i in word:
        alphabet_index = (alphabet.index(i) - shift) % len(alphabet)
        dec_word += alphabet[alphabet_index]
    print(f"Decrypted word: {dec_word}")

def cesar_c(req, text, shift):
    word = ""
    if req == "decode":
        shift = -shift
    for i in text:
        al_in = (alphabet.index(i) + shift) % len(alphabet)
        word += alphabet[al_in]
    print(f"Your {req} is: {word}")


