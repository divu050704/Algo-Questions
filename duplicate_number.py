#This program will find the duplicate elements in the lsit
def duplicate(x):#Initiated a function 
    print('Original list:\t',l)
    size  = len(x)#Length of the list
    for i in range(size):#This will complete the loop till the end of list
        for j in range(i):#Initiated another loop which will check list except the i 
            '''
            if i = 0
            then it will check 1,2,3,4 
            '''
            if x[i] == x[j]:#if it will find the duplicate element in the list then it will print the elemnt
                print('Duplicate element:\t',x[i])
l = [1,3,4,2,2]
duplicate(l)
'''
OUTPUT OF THE PROGRAM
Original list:   [1, 3, 4, 2, 2]
Duplicate element:       2
'''        
