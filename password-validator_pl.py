user_password = input("Wprowadź hasło do walidacji: ")
good_password = "Wprowadozne hasło jest bepieczne."
attention = "Wprowadzone hasło nie jest bezpieczneo. Dobre hasło powninno:"
to_short = "- mieć długość przynajmniej 8 znaków"
no_lower = "- zawierać przynajmniej 1 małą literę"
no_upper = "- zawierać przynajmniej 1 wielką literę"
no_special = "- zawierać przynajmniej 1 znak specjalny"
no_digit =  "- zawierać przynajmniej 1 cyfrę"
no_space = "- nie zawierać spacji ani tabulatorów"
is_lenght = len(user_password) >= 8
is_lower = False
is_upper = False
is_space = False
is_special = False
is_digit = False
for char in user_password:
    if char.islower():
        is_lower = True
    elif char.isupper():
        is_upper = True
    elif not char.isalpha() and not char.isdigit() and not char.isspace():
        is_special = True
    elif char.isdigit():
        is_digit = True
    elif char.isspace():
        is_space = True
is_correct = is_lenght and is_lower and is_upper and is_special and is_digit and not is_space
if is_correct:
    print(good_password)
else:
    print(attention)
    if not is_lenght:
        print(to_short)
    if not is_lower:
        print(no_lower)
    if not is_upper:
        print(no_upper)
    if not is_special:
        print(no_special)
    if not is_digit:
        print(no_digit)
    if is_space:
        print(no_space)
