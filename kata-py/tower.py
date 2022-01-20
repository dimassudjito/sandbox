def tower_builder(n_floors):
    num_list = [1]
    for number in range(0, n_floors-1):
        num_list.append(num_list[number]+2)
    tower_list = []
    for number in num_list:
        space = ' ' * int(((num_list[n_floors-1]-number)/2))
        tower_list.append(space + ('*' * number) + space)

    return tower_list


tower_builder(4)