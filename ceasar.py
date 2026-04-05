from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def print_logo():
    print(logo)

def encrypt(word, shift):
    enc_word = ""
    for i in word:
        alphabet_index = alphabet.index(i) + shift
        alphabet_index %= len(alphabet)
        enc_word += alphabet[alphabet_index]
    print(f"Encrypted word: {enc_word}")

encrypt("abc",52)