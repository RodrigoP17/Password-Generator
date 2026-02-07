import string

def obtain_characters(lower_case, upper_case, numbers, symbols):

    characters = ""

    if lower_case:
        characters += string.ascii_lowercase

    if upper_case:
        characters += string.ascii_uppercase

    if numbers:
        characters += string.digits
    
    if symbols:
        characters += string.punctuation

    return characters