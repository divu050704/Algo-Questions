#This program will minimze the maximum difference between heights
# The value of 'k' is first subtracted from each element one by one and if the value of the number after subtraction comes negative then it will add the value of 'k' instead of subtraction and then will edit the original list
def minimize_hieghts(x,k):#given the list as 'x' and the value of k as 'k' only
    size = len(x)#size of the list
    for i in range(size):#Till end of the list
        number = x[i] - k#First we will try subtraction
        if number < 0:# and if the number is negative 
            number  = k+x[i]#We will add it with k instead of subtraction
        l.pop(i)#First remove the old number 
        l.insert(i,number)#and insert the new number at its place
    l.sort()#First sort the list to get the maximum and minimum number 
    print(l[int(size-1)]-l[0])#Then finally subtract the larget number from lowest number in the list(last - first)
l = [1,5,8,10]
k = 2
minimize_hieghts(l,k)
'''
Output of the program
5
'''
