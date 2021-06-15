#This program will mrge all the elements of two lists in a singlie sorted list without using extra space
def merge_list(x,y):#Function for two lists x and y
    print('First list:\t',x)
    print('Second list:\t',y)
    main = []#Created an empty list for merging
    size= len(x)#length of first list
    size1 = len(y)#length of second list 
    for i in range(size):#Till end of the first list
        main.append(x[i])#Will append all the elements in the empty list main
    for i in range(size1):#Till end of second list 
        main.append(y[i])#Will append all the elements in the list main
    main.sort()# finally sorted the list main
    print('Merged list:\t',main)#Printed the merged list 
n = [1,3,5,7]
m = [0,2,6,8,9]
merge_list(n,m)
'''
OUTPUT OF PROGRAM
First list:      [1, 3, 5, 7]
Second list:     [0, 2, 6, 8, 9]
Merged list:     [0, 1, 2, 3, 5, 6, 7, 8, 9]
'''
