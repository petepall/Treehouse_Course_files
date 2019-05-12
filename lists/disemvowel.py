def disemvowel(word):
    vowels = 'aeiou'
    # remove = list(word)

    # for letter in word:
    #     if letter.lower() in vowels:
    #         remove.remove(letter)
    #     else:
    #         new_word += letter

    new_word = [char for char in word if char.lower() not in vowels]
    new_word = ''.join(new_word)

    word = new_word
    return word


print(disemvowel("RVqnUDo"))
