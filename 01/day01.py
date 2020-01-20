with open('data.txt', 'r') as f:
    data = f.readlines()

# doors = [x for x in data[0].split('')]
# print(doors)

doors = data[0]
print(doors)
print(len(doors))


floor = 0
position = 0
for x in doors:
    position += 1
    if x == '(':
        floor += 1
    if x == ")":
        floor -= 1
        if floor == -1:
            print(position)
            
        
print(floor)

