def validate_pin(pin):
    valid = True
    if len(pin) != 4 and len(pin) != 6:
        valid = False
    elif not pin.isdigit():
        valid = False
    print(valid)

validate_pin('-234')
