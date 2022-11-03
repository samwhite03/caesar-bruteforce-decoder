def Setup():
    while True:
        knownPhrase = ""
        encodedMessage = input("Input the string to decode:\n>>>")
        knownPhrase = input("Input a known phrase within the encoded message (default: 'the'):\n>>>")
        if knownPhrase == "":
            knownPhrase = "the"
        Bruteforce(encodedMessage, knownPhrase)


def FindCaps(message):
    capitalPositions = []
    for index in range(len(message)):
        if ord(message[index]) > 64 and ord(message[index]) < 91:
            capitalPositions.append(index)
    return capitalPositions


def Decode(stringToDecode, increment):
    capitals = []
    decodedString = ""
    capitals = FindCaps(stringToDecode)
    for letter in range(len(stringToDecode)):
        convertedLetter = ord(stringToDecode[letter])
        if (convertedLetter > 64 and convertedLetter < 91) or (convertedLetter > 96 and convertedLetter < 123):
            convertedLetter += increment
        if (letter in capitals and convertedLetter > 90) or convertedLetter > 122:
            convertedLetter -= 26       
        decodedString+=chr(convertedLetter)
    return decodedString


def Bruteforce(BruteforceTarget, knownPhrase):
    for offset in range(1, 25):
        attemptedDecode = Decode(BruteforceTarget, offset)
        if attemptedDecode.find(knownPhrase) != -1:
            print("Result found with offset "+str(offset)+":\n"+attemptedDecode+"\n")

Setup()
