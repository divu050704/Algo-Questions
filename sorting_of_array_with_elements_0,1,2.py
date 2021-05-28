def sorting(x):
    print('Original list:\t',x)
    size = int(len(x)-1)#length of the list - 1 because the index starts with 0
    for i in range(size):
        if x[i] == 0:#We will check whether 0 is in the list or not 
            x.pop(i)#we will first remove 0
            x.insert(0,0)#and insert it in the 0 index
        if x[i] == 2:#We will check whether 3 is in the list or not
            x.pop(i)# We will first remove 2 
            x.insert(size,2)# and insert it in the last index
        # We need not to make any change for 1 because it will automatically move to the middle if all the zeroes will be in the starting and all the 2s will be in the end 
    print('Sorted list:\t',x)#finally we will print the required list
l = [1,0,0,2,1]
sorting(l)
'''
Original list:   [1, 0, 0, 2, 1]
Sorted list:     [0, 0, 1, 1, 2]
'''
