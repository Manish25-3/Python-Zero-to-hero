import array as arr

a = arr.array('i', [2, 3, 4, 5])

print("Prime numbers are :", end=" ")

for i in a:
    num = i
    j = 2
    f = 1
    while j < num:
        if num % j == 0:
            f = 0
            break
        j = j + 1

    if f == 1:
        print(num, end=" ")

'''        
output :

Prime numbers are : 2 3 5

'''

