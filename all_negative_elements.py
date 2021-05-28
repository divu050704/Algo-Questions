def move_negative_elements(x):
    print('Original list:\t',x)#We will first print the original list
    size = int(len(x))#Length of the list 
    for i in range(0,size):
        if x[i] < 0:#if x[i] is negative
            main = x[i]#we will first save the element in variable because we are going to pop the element afterwards
            x.pop(i)#We will pop the element 
            x.insert(0,main)#and insert it in the first index
    print('Sorted list:\t',x)#We will print the final list at last
l = [2,3,4,-2,-3,-4]
move_negative_elements(l)
'''
OUTPUT OF THE PROGRAM
Original list:   [2, 3, 4, -2, -3, -4]
Sorted list:     [-4, -3, -2, 2, 3, 4]
'''
