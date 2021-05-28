def maximum_minimum(x):
    print('Given list:\t',l)
    maximum = x[0]#We will take a constant to check 
    for i in x:#For all the numbers in list
        if maximum < i:#if any number exists larger than maximum, if exists then next number larger than that number and so on
            maximum = i#Gave variable the value of maximum number
    print('Maximum element in the list:\t',maximum)#Printed largest number
    minimum = x[0]#We will againt take 1st number as constant to check
    for i in x:#For all the numbers in the list
        if minimum > i:#if any number exists less than minimum, if exist then if next number is smaller than last number and so on
            minimum = i#Gave variable the value of minimum number
    print('Minimum element in the list:\t',minimum)#Printed smallest number
l = [13,21,32,12]
maximum_minimum(l)
'''
Given list:      [13, 21, 32, 12]
Maximum element in the list:     32
Minimum element in the list:     12
'''
