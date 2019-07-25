import random
# This is more of a Caesar Cipher + Rail Fence Cipher.
# With Rail Fence only, when the number of row randomly
# generated is greater than or equal to the word, it returns
#  the same word. To avoid that, I used Caesar cipher to encrypt
#  words less than or equal to row to make it more difficult to decrypt.
# 'row' can always be changed to key to decrypt

row = random.randint(3, 5)

def rail_fence(word):
    """
    :param word: -> str
    :return: encrypted word -> str
    """
    if type(word) != str:
        raise TypeError("Word given is not a string")

    # remove all white spaces
    word = "".join(word.split()).upper()

    cypher = [""] * row

    if len(word) <= row:
        #encrypt using caesar cippher

        # for constant time lookup
        alphabet_set = {"A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L", "M",
                    "N", "O", "P", "Q", "R", "S", "T", "U", "V" "W", "X", "Y", "Z"}
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for elem in word:
            if elem in alphabet_set:
                i = (alphabet.index(elem) + row) % 26
                cypher[0] += alphabet[i]
            else:
                cypher[0] += elem

        return cypher[0]

    index = 0

    for elem in word:
        if index == 0:
            cypher[index] += elem
            move = 1
            index += move
        elif index == len(cypher) - 1:
            cypher[index] += elem
            move = -1
            index += move
        else:
            cypher[index] += elem
            index += move
    return "".join(cypher)

def test_cipher():
    #Testing the normal cases
    if row == 3:
        assert rail_fence("TERRAGONISHIRING") == "TAIRERGNSIIGROHN", "wrong answer"
    elif row == 4:
        assert rail_fence("TERRAGONISHIRING") == "TOREGNIIRAIHNRSG", "wrong answer"
    elif row == 5:
        assert rail_fence("TERRAGONISHIRING") == "TIENSGROHNRGIIAR", "wrong answer"

    #Testing an edge case
    assert rail_fence("") == "", "wrong answer"

    #The Caesar cipher
    if row == 3:
        assert rail_fence("TE") == "WH", "wrong answer"
    elif row == 4:
        assert rail_fence("TE") == "XI", "wrong answer"
    elif row == 5:
        assert rail_fence("Z.") == "E.", "wrong answer"
        assert rail_fence("ZE") == "EJ", "wrong answer"

test_cipher()
print("Works fine!")