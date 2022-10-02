user_password = input("Podaj swoje hasło: ")
attention = "Twoje hasło nie jest bezpieczne. Dostosuj się do poniższych wytycznych:"
good_password = "Twoje hasło jest bepieczne."
toshort = "- Hasło musi mieć minimum 8 znaków"
nolower = "- Hasło powinno mieć minimum jedną małą literę"
noupper = "- Hasło powinno mieć minimum jedną wielką literę"
nospecial = "- Hasło powinno mieć minimum jeden znak specjalny"
nospace = "- Hasło nie może zawierać spacji lub tabulatora"
islower = False
isupper = False
isspace = False
isspecial = False
islenght = len(user_password) >= 8
for char in user_password:
    if char.islower():
        islower = True
    elif char.isupper():
        isupper = True
    elif char.isspace():
        isspace = True
    elif not char.isdigit():
        isspecial = True
iscorrect = islenght and islower and isupper and isspecial and not isspace
if iscorrect:
    print(good_password)
else:
    print(attention)
    if not islenght:
        print(toshort)
    if not islower:
        print(nolower)
    if not isupper:
        print(noupper)
    if not isspecial:
        print(nospecial)
    if isspace:
        print(nospace)
