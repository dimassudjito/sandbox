def productFib(prod):
    fib = [0, 1]
    counter_before = 0
    counter_after = 1
    for i in range (0, 100):
        num = fib[counter_before] + fib[counter_after]
        fib.append(num)
        counter_before += 1
        counter_after += 1

    prod_fib = [fib[i] * fib[i+1] for i in range(len(fib)-1)]

    counter = 0
    for item in prod_fib:
        if item == prod:
            result = [fib[counter], fib[counter+1], True]
            break
        elif item > prod:
            result = [fib[counter], fib[counter+1], False]
            break
        counter += 1

    return result

productFib(3825251)

# Best practice
# def productFib(prod):
#   a, b = 0, 1
#   while prod > a * b:
#     a, b = b, a + b
#   return [a, b, prod == a * b]


### Test ###
# x = range(0, 10)
# print(x)