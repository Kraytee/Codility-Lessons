
"""""
this code is asking the user to input a valid number in the range given and makes sure that it meets the specifications using a while and if loop.
while True:
    number = int(input(("Type a number between 1 and 2,147,483,647: ")))
    if number > 21474836474 or number < 0:
        print("Error! Please Type in a number within the specified paramters")
    else:
        print("Thank you!")
        break

binary = bin(number)[2:]
print(binary)

so need to write a program that takes the binary form of a number. Checks first number, is it a 1 or a zero? if a zero add one to the counter if not
"""
#here we are asking for the user to input an integer that we can find the binary gap for
N = int(input(("Number: ")))
#this code will convert the number into binary form
print(bin(N)[2:])

def solution(N):
    binary = bin(N)[2:]
    #set the initial amount of zeros to 0
    zeros = 0
    #create a variable to store the highest binary gap (number of zeros in a row) found
    maxZeros = 0
    #create a for loop that loops the length of the binary number 
    for i in range(len(binary)):
        #if position i in the binary number is a 0 then add 1 to the zeros counter
        if binary[i] == '0':
            zeros = zeros + 1
        #if position i in the binary number is a 1 and the highest amount of zeros (maxZeros) is greater than the current amount of zeros
        #then maxzeros stays as max zeros 
        elif binary[i] == '1':
            if maxZeros > zeros:
                maxZeros = maxZeros
            #if maxzeros is less than the current amount of zeros then update that the maxzeros is the current zeros and reset the zeros counter
            else:
                maxZeros = zeros
                zeros = 0
    return(maxZeros)

print(solution(N))
    
