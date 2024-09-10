# ++++++++++++++ Write a Function to Calculate and return the Square of a Number ++++++++++++++++++

inputNum = int(input('Please Enter a number Whose Square You want: '))

def numSquare():
   print(f'The Square of ',inputNum, 'is ',inputNum * inputNum)
   return inputNum * inputNum
   

result = numSquare()
print(result)
    