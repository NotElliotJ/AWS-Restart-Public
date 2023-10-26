def prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return False
 
with open('results.txt', 'w') as f:
    for i in range(2, 251):
        if prime(i):
            print(i)
            f.write(str(i) + '\n')
