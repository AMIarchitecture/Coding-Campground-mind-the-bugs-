print('How many cats do you have?')
numCats = input()
try:
    if int (numCats) >=4:
        print ('Thats a lot of cats')
    if int (numCats) <=0:
        print ('Those cats dont exist!')
    if int (numCats) <=3:
        print ('Thats not alot of cats')
except ValueError:
    print ('You did not enter a number')
    
    
