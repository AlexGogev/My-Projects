alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift_number):
    texter= ""
    for i in text:
        pos = alphabet.index(i)
        new_pos = pos + shift_number
        newletter = alphabet[new_pos]
        texter += newletter 
    print(texter)
encrypt("abba", 5)

def decrypt(text, shift_number):
    texter= ""
    for i in text:
        pos = alphabet.index(i)
        new_pos = pos - shift_number
        newletter = alphabet[new_pos]
        texter += newletter 
    print(texter)
decrypt("fggfa", 5)