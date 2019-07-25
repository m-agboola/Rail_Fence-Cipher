import random
# This is more of a Caesar Cipher + Rail Fence Cipher.
# With Rail Fence only, when the number of row randomly
# generated is greater than or equal to the word, it returns
#  the same word. To avoid that, I used Caesar cipher to encrypt
#  words less than 3.
# 'row' can always be changed to key to decrypt
def rail_fence(word):
    """
    :param word: -> str
    :return: encrypted word -> str
    """
    if type(word) != str:
        raise TypeError("Word given is not a string")

    # remove all white spaces
    word = "".join(word.split())
    row = random.randint(3, 7)
    cypher = [""] * row

    if len(word) < 3:
        #encrypt using caesar cippher
        for elem in word:
            cypher[0] += chr(ord(elem) + row)
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


