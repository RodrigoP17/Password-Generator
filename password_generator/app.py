from password_utils.generator import obtain_password
from password_utils.avaliator import evaluate_password

def obtain_message(message):

    while True:
        response = input(message).lower().strip()

        if response in ["y", "n"]:
            return response == "y"
        else:
            print("Invalid option! Please choose 'y' or 'n'!")

def main():

    print("=" * 50)
    print("GENERATOR OF SAFE PASSWORDS".center(50))
    print("=" * 50)
    print()

    while True:
        try:
            size = int(input("What size do you want your password? (minimum 4): "))

            if size >= 4:
                break
            else:
                print("The minimum size is 4 characters!")

        except ValueError:
            print("Please introduce a valid number!")

    print()
    print("Choose the type of characters to include: ")
    print("=" * 50)

    lower_case = obtain_message("Do you want lower case characters? (y/n)")
    upper_case = obtain_message("Do you want upper case characters? (y/n)")
    numbers = obtain_message("Do you want numbers? (y/n)")
    symbols = obtain_message("Do you want symbols? (y/n)")

    try:
        print("Obtaining password ...")

        password = obtain_password(size, lower_case, upper_case, numbers, symbols)

        print()
        print("=" * 50)
        print("Result".center(50))
        print("=" * 50)
        print()
        
        print(f"Password generated: {password}")
        print(f"Password length: {len(password)}")

        print(f"Password strenght: {evaluate_password(password)}")
        print()

    except ValueError as e:
        print(f"Error: {e}")

    print("=" * 50)
    continuation = obtain_message("Do you want another password? (y/n): ")

    if continuation:
        print()
        main()
    else:
        print("\nThank you for using the password generator!")
        print("Keep your passwords safe! 🔐")

if __name__ == "__main__":
    main()