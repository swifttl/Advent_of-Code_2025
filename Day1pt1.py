input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2025/Day1/Day1Input', 'r').read().splitlines()
start = 50
dialArray = list(range(0,100))
password = 0
for rotations in input:
    direction = rotations[0]
    clicks = int(rotations[1:])
    if direction == 'L':
        start =(start-clicks)%100
    elif direction == 'R':
        start = (start+clicks)%100
    if start == 0:
        password += 1
    print('The dial is rotated ', direction,clicks,' to point at ', start)
print('The total count of "0" for the password is: ', password)
