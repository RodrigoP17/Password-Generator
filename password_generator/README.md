# Password Generator 

A simple Python command-line **password generator** that creates secure passwords based on user-defined options and evaluates their strength.

## Features

- Custom password length (minimum 4 characters)

- Optional character types:

    -   Lowercase letters

    -   Uppercase letters

    - Numbers

    - Symbols

- Password strength evaluation

- Interactive CLI interface

- Uses only Python standard library

## Project Structure
```bash
password_generator/
├── app.py
└── password_utils/
    ├── generator.py
    ├── avaliator.py
    ├── characters.py
```
## Requirements

Python 3.11+

## Usage

Run the application from the project root:
```bash
python app.py
```

Follow the prompts to choose the password length and character types.

## Example
```bash
Password generated: A9#fL!2kP@qR
Password strength: Strong
```
## Notes

- At least one character type must be selected

- Password strength is based on length and character variety