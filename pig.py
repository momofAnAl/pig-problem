def pig_latin(sentence):
    """
    take a string and return a string with first word move to the last position and add "ay"
    if the word start with vowel like a, i, u, o, e then we not switch
    it's empty string, return empty string
    do we handle case insensitive as uppercase or I can assume its call lowercase
    """
    
    # I create a list for all vowel letters
    vowels_list = ['a', 'e', 'i', 'u', 'o']
    
    # create empty list to convert all letters to the list
    new_list = sentence.split()
    print(new_list)
    # I can loop through to the sentence
    
    # update_list = []
    new_sentence = ""
    for word in new_list:
        if word[0] not in vowels_list:
            first_letter = word[0]
            rest_letter = word[1:]
            new_word = rest_letter + first_letter + "ay"
            new_sentence = new_sentence + new_word + " "
        else:
            new_sentence = new_sentence + word + " "
            
    new_sentence = new_sentence[:-1]
    return new_sentence
        
    # new_word = " ".join(update_list)
    # return new_word           
                
    # I can get first element and check it: if it in the vowel list , then I return as it is
    #if not , move the first element to the last and append to empty list 
    # using .join() to make it as a string

# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")