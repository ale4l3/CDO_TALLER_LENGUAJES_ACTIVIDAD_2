def is_word(word):
    if word.isalpha:
        word = str(word)
        word.strip().lower()
        if any(c.isdigit() for c in word):
            print("La palabra tiene digitos")
        else:
            return word
    else:
        print("El valor ingresado no es alfanumerico")

def is_anagram(word_1, word_2):
    word_1 = list(word_1)
    word_2 = list(word_2)
    len_word_1 = len(word_1)
    len_word_2 = len(word_2)
    if len_word_1 == len_word_2:
        list_set = set(zip(word_1, word_2))
        len_list_set = len(list_set)
        if len_list_set == len_word_1:
            print("Son anagramas")
        else:
            print("No son anagramas")
    else:
        print("Las palabras no tienen la misma cantidad de letras")