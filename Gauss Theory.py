  GNU nano 4.8                                                                 Project_3.2.py                                                                            
#!/usr/bin/python3

highNum = input("Enter Number to be Gaussed: ")
whileVar = int(highNum) / 2
listNum = int(highNum) + 1

listNum = [i for i in range(1,int(listNum))]

#while loop
i = 0
popval = int(highNum) - 2
totalCount = 0
count = 0
#Gauss Mult
lowNum = 1
gaussNum = 0

while i < int(whileVar):
        x = listNum.pop(0)
        y = listNum.pop(popval)
        print("{} + {}".format(x, y))
        sum = x + y
        print("Partial Sum of numbers: {}".format(sum))

        i += 1
        count += 1
        popval -= 2
        totalCount +=1
        print("Number of Partial Sums: {}\n".format(count))

print("Total Parial Sums: {}\n".format(totalCount))

print("({} + {}) * ({})".format(lowNum, highNum, totalCount))
gaussNum = (int(lowNum) + int(highNum)) * (totalCount)
print("Gaussed Number: {}".format(gaussNum))
