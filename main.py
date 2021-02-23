'''
Review:

while loop
>> Repeats body statement until the condition becomes false

Format:

while (condition):
  Body Statement

else:
  Body Statement


#Expected outputs: 1x Python, 2x bye, 3x Evergreen, 4x 2021

student = 10

while (student > 0):
  if (student >= 11):
    print ("hello")
  elif (student >= 10):
    print ("Python")
  elif (student > 7):
    print ("bye")
  elif (student >= 5):
    print ("Evergreen")
  else:
    print ("2021")

student -= 1

# New Program
Num = random.randint(1,10)
playNum = int(input("Enter a number from the range 1-10"))

while (Num != playNum):
  if (Num > playNum):
    print ("Your number is too low.")
  
  if (playNum > Num):
    print ("Your number is too high.")

  if (Num == playNum):
    print ("Congrats, you guessed the number!")

For loop: Repeats a set of statements a certain number of times.

Formula:

for LVC (Loop Variable Control) in Sequence:
  Body Statement

LVC: an ordinary int variable that is initialized, tested, and changed as the loop executes.

Sequence:
An iteration statement

for n in range(5): # {0,1,2,3,4 which is 5 number}
  print (n)

range() function
1 argument; range(#) --> range(stop)
2 arguments; range(#, #) --> range(start,stop)
3 arguments; range(#, #, #) --> range (start, stop)
'''
