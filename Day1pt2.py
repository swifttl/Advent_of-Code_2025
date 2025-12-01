input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2025/Day1/Day1Input', 'r').read().splitlines()
start = 50

password = 0
for rotations in input:
    quotient = 0
    direction = rotations[0]
    clicks = int(rotations[1:])
    #LEFT
    if direction == 'L':
        quotient = abs((start-clicks)//100)
        #If the rotation will land on 0/100
        if (start-clicks)%100==0:
            password +=1
            #Determine count how many crosses
            if quotient != 0:
                password += quotient
            elif quotient == 0:
                pass
        ###If the rotation lands anywhere else
        else:
            if start !=0:
                password+=quotient
            else:
                #starting at 0 will cause the quotient to count an extra crossing
                password+=quotient-1
        start =(start-clicks)%100
    #RIGHT
    else:
        quotient = (start+clicks)//100
        #If the rotation will land on factor of 100
        if (start+clicks)%100 == 0:
            password += quotient
        else:
            #Determine how many crosses
            if (start+clicks) >= 100:
                password += quotient
        start = (start+clicks)%100
print('The password is', password)
