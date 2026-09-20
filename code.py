for i in range(1, 21):
    if(i % 2 != 0):
        print(i)

for i in range(1, 571):
    if(i % 57 == 0):
        print(i)

for i in range(1, 51):
    if(i == 15):
        continue
    if(i % 3 == 0):
        print(i)

a = int(input("Write 1st num: "))
b = int(input("Write 2nd num: "))

for i in range(1, 1001):
    if(i % a == 0 and i % b == 0):
        print(i)
        break