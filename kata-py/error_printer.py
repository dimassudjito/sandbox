def printer_error(s):
    error_count = 0
    for letter in s:
        if ord(letter) > 109:
            error_count += 1

    print("{}/{}".format(error_count, len(s)))


s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s)

### test ###
# c = ord("c")
# print(c)


