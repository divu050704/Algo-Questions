#This program is used to rotate the list
def rotate(x):
    print('Original list:\t',x)#We eill first print teh original list
    size = int(len(x))-1
    main=x[size]#We first the last value of the list in the form of a variable
    x.pop(size)#Remove the element
    x.insert(0,main)#Then insert the main value at 0 index
    print('Rotated list:\t',x)#Finally prints the final list
x = [1,2,3,4]
rotate(x)
'''
OUTPUT OF THE PROGRAM
Original list:   [1, 2, 3, 4]
Rotated list:    [4, 1, 2, 3]
'''
