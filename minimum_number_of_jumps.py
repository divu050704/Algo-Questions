#This program will count how many minimum steps will be taken to reach the end if we will add the element of the index of the last added number of index
def minimum_number_of_jumps(x):#function defined for a list 'x'
    k = []#defined an empty list for further operations 
    size = len(x)# lenght of the list
    start = l[0]#starting position will be first element  
    c = 'Y'#Declared a variable with a value
    while c == 'Y':#Initiated an infinity loop
        start += l[start]#added the value of last number to new index element
        k.append(start)#appened the empty list 
        if start >= (size-1):#If the number has reached the elements or crossed the last element 
            break#break the infinity loop
    print(len(k)+1)#Print number of steps (number of elements in the list ), added 1 because it will not count the first element 
l = [1,3,5,8,9,2,6,7,6,8,9]
minimum_number_of_jumps(l)
'''
Output of the program
3
'''    
