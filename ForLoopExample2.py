#inputRound = int(input("Please Enter Number : "))
#sum = 0
#for x in range(inputRound):
 #   inputNumber = int(input("x" + str(x+1) + ":"))
  #  sum += inputNumber

# print ("Result", sum)
start = int(input("Start: "))
step  = int(input("Step : "))
result =""
for i in range (5):
    result += str(start+step*i+1)
    print (result)