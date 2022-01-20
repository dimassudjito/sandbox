def create_phone_number(n):
    i = 0
    while i < len(n):
        n[i] = str(n[i])
        i += 1

    text = ''.join(n)
    phone = '(' + text[0:3] + ') ' + text[3:6] + '-' + text[6:11]

    print(phone)

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8 ,9, 0])