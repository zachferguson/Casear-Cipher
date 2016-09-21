import enchant
import re


def unknowncaesar():
    dictio = enchant.Dict("en_US")
    alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

    def decode(cyphertext, cypherkey):
        alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
        cypherlist = []
        decodedlist = []

        for letter in cyphertext:
            cypherlist.append(letter)

        shift = alphalist.index(cypherkey)
        for letter in cypherlist:
            if letter.isalpha() is True:
                letter = letter.lower()
                if (alphalist.index(letter) - shift) < 0:
                    decodedlist.append(alphalist[alphalist.index(letter) - shift + 26])
                if (alphalist.index(letter) - shift) >= 0:
                    decodedlist.append(alphalist[alphalist.index(letter) - shift])

            if letter.isalpha() is False:
                decodedlist.append(letter)

        decodedlist = ''.join(decodedlist)
        return decodedlist

    def wordsplit(ctext):
        return re.compile('\w+').findall(ctext)

    def decypher(original):
        print('Decypher entered')
        alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
        caesartotal = []
        positives = []
        keys = []
        x = 0
        while x < 26:
            temptext = decode(original, alphalist[x])
            caesartotal.append("")
            caesartotal[x] = temptext
            x += 1

        strcount = 0
        while strcount < 26:
            testtext = caesartotal[strcount]
            count = 0
            ewords = 0
            lowcount = wordsplit(testtext)
            while count < 10:
                if ewords == 7:
                    positives.append(testtext)
                    keys.append(alphalist[strcount])
                    break
                tstxlist = wordsplit(testtext)

                if len(lowcount) == count:
                    if dictio.check(tstxlist[0]) == True or dictio.check(tstxlist[1]) == True:
                        positives.append(testtext)
                        keys.append(alphalist[strcount])
                        break

                    if dictio.check(tstxlist[0]) == False and len(lowcount) == count:
                        break

                if dictio.check(tstxlist[count]) == True:
                    ewords += 1
                    count += 1
                    continue

                if dictio.check(tstxlist[count]) == False:
                    count += 1
                    continue
            strcount += 1
        ctr = 0
        print("")
        print("Results:")
        print("Positive results = " + str(len(positives)) + ".")
        while ctr <= (len(positives) - 1):
            if len(positives) == 0:
                print("This is not encoded with a Caesar Cypher.")
                break
            print("Key = " + str(keys[ctr]))
            print("Decyphered text = " + positives[ctr])
            ctr += 1

    text = input("Type 'Q' to quit to the main menu, or enter the text to be deciphered:")
    if text == 'q' or text == 'Q':
        mainprog()

    decypher(text)


def encode():
    alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    textlist = []
    text = input("Please enter the text to be encoded.")
    shift = input("Please enter a letter to equal 'A' in the Caesar Cypher encoded text.")
    encoded = []
    for letter in text:
        textlist.append(letter)

    shift = alphalist.index(shift)

    for letter in textlist:
        letter = letter.lower()
        if letter.isalpha() is True:
            if (alphalist.index(letter) + shift) >= 25:
                encoded.append(alphalist[alphalist.index(letter) + shift - 26])
            if (alphalist.index(letter) + shift) < 25:
                encoded.append(alphalist[alphalist.index(letter) + shift])
        if letter.isalpha() is False:
            encoded.append(letter)
    cyphertext = ''.join(encoded)
    print("Your encoded text: " + cyphertext)
    mainprog()

def decode():
    alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    cyphertext = input("Please enter the text to be decoded.")
    cypherkey = input("Please enter the Caesar Cypher key (the letter that equals 'A').")
    cypherlist = []
    decodedlist = []

    for letter in cyphertext:
        cypherlist.append(letter)

    shift = alphalist.index(cypherkey)
    for letter in cypherlist:
        if letter.isalpha() is True:
            letter = letter.lower()
            if (alphalist.index(letter) - shift) < 0:
                decodedlist.append(alphalist[alphalist.index(letter) - shift + 26])
            if (alphalist.index(letter) - shift) >= 0:
                decodedlist.append(alphalist[alphalist.index(letter) - shift])

        if letter.isalpha() is False:
            decodedlist.append(letter)

    decodedtext = ''.join(decodedlist)
    print(decodedtext)
    mainprog()

def mainprog():
    print("")
    print("Caesar Cypher")
    print("")
    select = input('''Menu:
    1 - Encode text.
    2 - Decode text with known key.
    3 - Decode unknown Caesar Cypher.
    4 - Quit program.
    ''')
    print("")
    while True:
            if select == "1":
                encode()
            if select == "2":
                decode()
            if select == "3":
                unknowncaesar()
            if select == "4":
                quit()
            if select not in {"1", "2", "3", "4"}:
                print("That is not a valid selection. Please try again.")
                print("")

mainprog()