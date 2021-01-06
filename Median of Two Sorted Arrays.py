num1 = [1,3]
num2 = [2 , 4]

num3 = num1 + num2
num3 = sorted(num3)

sumlen = len(num1) + len(num2)

if sumlen%2 == 0:
    med = int((sumlen)/2)
    med2 = int(((sumlen)/2) -1)
    print((med+med2)/2)
else:
    l = int((sumlen)/2)
    print(num3[l])
