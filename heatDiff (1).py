#Marcus Barnes
#mbb11d
import numpy
import matplotlib.pyplot as plt

# DARKBLUE = '072343'
# BLUE = '07305F'
# CYAN = '065CBF'
# GREEN = '1B9A08'
# YELLOW = 'EFEF0C'
# ORANGE = 'EFB20C'
# RED = 'EF230C'
# MAROON = '8D0505'


textIn = input("Please enter the starting temperature")
graphsize = int(textIn)

blankTemp = numpy.zeros((graphsize + 2, graphsize +2 ))
blankTemp[0:, 0] = graphsize
newTemp = numpy.copy(blankTemp)  #recomended to do this copy bc otherwise you will have anormal bugs
oldTemp = numpy.copy(blankTemp)
c1, c2, c3, c4, c5, c6, c7, c8 = 'darkred', 'red', 'orange', 'yellow','lawngreen', 'aqua', 'blue', 'darkblue'
sliced = graphsize/8
s1, s2, s3, s4, s5, s6, s7, s8 = sliced, 2*sliced, 3*sliced, 4*sliced, 5*sliced, 6*sliced, 7*sliced, 8*sliced

print(newTemp)

print("Please wait, calculation could take a while...")
counter = 0
isDone = False
while counter < 3000 and isDone is False:
    for i in range(1, graphsize + 1):
        for j in range (1, graphsize + 1):
            temp = (oldTemp[i-1,j] + oldTemp[i+1,j] + oldTemp[i,j-1] + oldTemp[i,j+1])
            newTemp[i,j] = temp/4
            if numpy.array_equal(newTemp, oldTemp)is False:
                oldTemp = numpy.copy(newTemp)
                continue
            else:
                isDone = True
                break
        if isDone is True:
            break
    else:
        counter = counter + 1

print(" done with while loop")
for i in range(1, graphsize + 1):
    for j in range(1, graphsize + 1):
        current = newTemp[i, j]
        if current >= 0 and current < s1:
            plt.plot(j, i, color=c8, markeredgecolor='black', marker='o')
        if current >= s1 and current < s2:
            plt.plot(j, i, color=c7, markeredgecolor='black', marker='o')
        if current >= s2 and current < s3:
            plt.plot(j, i, color=c6, markeredgecolor='black', marker='o')
        if current >= s3 and current < s4:
            plt.plot(j, i, color=c5, markeredgecolor='black', marker='o')
        if current >= s4 and current < s5:
            plt.plot(j, i, color=c4, markeredgecolor='black', marker='o')
        if current >= s5 and current < s6:
            plt.plot(j, i, color=c3, markeredgecolor='black', marker='o')
        if current >= s6 and current < s7:
            plt.plot(j, i, color=c2, markeredgecolor='black', marker='o')
        elif current >= s7 and current < s8:
            plt.plot(j, i, color=c1, markeredgecolor='black', marker='o')

print("after calc", newTemp)
plt.show()
# array2 = []
# for x in startingTemp:
#     for y in startingTemp:
#         array [x] [y] = 0   #setting array all to 0
#
#     array.append(for y in starting)
