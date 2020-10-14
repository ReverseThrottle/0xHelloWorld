GNU nano 4.8                                                                 Project_3.2.py                                                                  Modified  
#!/usr/bin/python3

#highNum = input("Enter Even Number: ")
#print(highNum)
listNum = [i for i in range(1,int(101))]
#while loop
i = 0
popval = 98
totalCount = 0
count = 0
#Gauss Mult
highNum = 100
lowNum = 1
gaussNum = 0
gaussDiv = 2

while i < 50:
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

print("({} + {}) * ({} / {})".format(lowNum, highNum, highNum, gaussDiv))
gaussNum = (lowNum + highNum) * (highNum / gaussDiv)
print("Gauss Multiplication: {}".format(gaussNum))
