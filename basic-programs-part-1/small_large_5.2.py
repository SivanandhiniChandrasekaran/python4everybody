
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
        
    try :
        inum = int(num)
    except :
        print('Invalid input')
        
    
    if smallest is None :
        smallest = inum
    elif inum < smallest :
        smallest = inum

    if largest is None :
        largest = inum
    elif inum > largest :
        largest = inum

    continue
    
print('Maximum is' , largest)
print('Minimum is' , smallest)


