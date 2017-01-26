def encrypt (text, rot):
    secretMessage = ""
    for char in text:
        newChar = rotate_character (char, rot)
        secretMessage = secretMessage + newChar
    return secretMessage

def alphabet_position(letter):
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    Alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if letter in alphabet:
        charPos = alphabet.find(letter)
        return charPos
    elif letter in Alphabet:
        charPos = Alphabet.find(letter)
        return charPos
    else:
        return letter

def rotate_character (char, rot):
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    Alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    charPos = alphabet_position (char)
    if char not in Alphabet and char not in alphabet:
        return char
    else:
        charPos = int(charPos)
        rot = int(rot)
        newPos = charPos + rot
        if newPos >= 26:
            newPos = newPos % 26
        else:
            newPos = newPos
        if char in Alphabet:
            return Alphabet[newPos]
        else:
            return alphabet[newPos]
