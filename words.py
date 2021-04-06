#function to print all items in a list completely in uppercase letters
def print_upper_words(list):

    for words in list:
        print(words.upper())

print_upper_words(["santana", "taylor", "leonard"])


#function to print all words in a list that start with the letter "e" in all uppercase
def letter_e(list_e):

    for word in list_e:
        if word.startswith("e") or word.startswith("E"):        
            print(word.upper())

letter_e(["elephant", "emo", "igloo", "apple"])


#function to print only words in a list that start with a given letter in all uppercase
def print_start(list, start_with):

    for word in list:
        for letter in start_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_start(["santana", "taylor", "leonard", "samantha"], "s")