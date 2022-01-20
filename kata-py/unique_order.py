def unique_in_order(iterable):
    current = ''
    list = []
    for element in iterable:
        if element != current:
            list.append(element)
            current = element
    print(list)

unique_in_order([1, 1, 2, 3])

### test ###
