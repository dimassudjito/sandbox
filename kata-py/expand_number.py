def expanded_form(num):
    num_list = list(str(num))
    dig_list = []
    for number in num_list:
        if number != '0':
            zero = '0' * (len(num_list) - num_list.index(number) - 1)
            digit = number + zero
            dig_list.append(digit)

    print(' + '.join(dig_list))



expanded_form(98486)