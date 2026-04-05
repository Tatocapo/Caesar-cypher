from ceasar import cesar_c,print_logo
if __name__ == "__main__":
    yes_no = False
    while yes_no != "no":
        print_logo()
        enter_en_dec = input("Enter encode/decode: ")
        enter_word = input("Enter the word you want to encode/decode: ")
        enter_shift = int(input("Enter the shift: "))
        cesar_c(req = enter_en_dec, text = enter_word, shift = enter_shift)
        yes_no = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")

