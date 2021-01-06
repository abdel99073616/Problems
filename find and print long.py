str = input("Enter String -->  ")

n = len(str)

st = 0

pos = {}

for i in range(1,n):
    pos[str[i]] = i


print(list(pos.keys()))