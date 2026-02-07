import random
from password_utils.characters import obtain_characters

def obtain_password(size, lower_case=True, upper_case=True, numbers=True, symbols=True):

    characters = obtain_characters(lower_case, upper_case, numbers, symbols)

    if not characters:
        raise ValueError("You must select at least one type of characters")
    
    characters_list = [random.choice(characters) for _ in range(size)]
    password = "".join(characters_list)
    
    return password