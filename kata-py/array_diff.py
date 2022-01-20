def array_diff(a, b):
    for element_a in a:
        for element_b in b:
            if element_a == element_b:
                while element_a in a:
                    a.remove(element_a)

    print(a)

array_diff([1, 2, 3], [3])