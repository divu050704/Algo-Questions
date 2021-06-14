#This program will sort a list in lexographical order
def lexographical_order(x): 
    print('Original list:\t',l)
    size = len(x)
    main = []
    # for converting numericals into words
    for i in range(size):#till end length
        s = str(x[i])#converted ith element of the list to string for easy manipulations
        inte = x[i]#also kept integral value 
        if len(s) == 1:#if length of the element is 1
            # Used brute force 
            if inte == 1:
                main.append('one')
            if inte == 2:
                main.append('two')
            if inte == 3:
                main.append('three')
            if inte == 4:
                main.append('four')
            if inte == 5:
                main.append('five')
            if inte == 6:
                main.append('six')
            if inte == 7:
                main.append('seven')
            if inte == 8:
                main.append('eight')
            if inte == 9:
                main.append('nine')
        if len(s) == 2:#if length of the element is 2
            # for all the double digit numbers(ten's digit)
            if (s[0] == '1') or (s[0] == '2') or (s[0] == '3') or (s[0] == '4') or (s[0] == '5') or (s[0] == '6') or (s[0] == '7') or (s[0] == '8') or (s[0] == '9'):#If the number is double digit then the loop will go ahead
                if s[1] =='0':#for the unit digits only, if unit digit is zero then it will not add anything 
                    i =''
                if s[1] == '1':
                    i = ' one'
                if s[1] == '2':
                    i = ' two'
                if s[1] == '3':
                    i = ' three'
                if s[1] == '4':
                    i= ' four'
                if s[1] == '5':
                    i = ' five'
                if s[1] == '6':
                    i = ' six'
                if s[1] == '7':
                    i= ' seven'
                if s[1] == '8':
                    i=' eight'
                if s[1] == '9':
                    i=' nine'
                if s == '10':
                    main.append('ten')#Used brute force for all the integer in the interval [10,19]
                if s == '13':
                    main.append('thirteen')
                if s == '14':
                    main.append('fourteen')
                if s == '15':
                    main.append('fifteen')
                if s == '16':
                    main.append('sixteen')
                if s == '17':
                    main.append('seventeen')
                if s == '18':
                    main.append('eighteen')
                if s == '19':
                    main.append('nineteen')
                if s[0] == '2':
                    main.append('twenty'+i)#This will add ten's digit and unit digit 
                if s[0] == '3':
                    main.append('thirty'+i)
                if s[0] == '4':
                    main.append('fourty'+i)
                if s[0] == '5':
                    main.append('fifty'+i)
                if s[0] == '6':
                    main.append('sixty'+i)
                if s[0] == '7':
                    main.append('seventy'+i)
                if s[0]=='8':
                    main.append('eighty'+i)
                if s[0] == '9':
                    main.append('ninety'+i)
        if len(s) == 3:
            if s == '100':
                main.append('hundred')
    main.sort()
    #Now loop for converting alphabets to digits
    last =[]#created an empty list
    size = len(main)#length of the list of numbers in words 
    for i in range(size):#loop till size
        ss = str(main[i])#converted each element of the list to string 
        s = ss.split()#splitted the string into words to fing number of words 
        length = len(s)#number of words in the string
        if length == 1:#if number of words in the string is 1 
            if ss == 'hundred':#again used brute force
                last.append(100)
            if ss== 'one':
                last.append(1)
            if ss == 'two':
                last.append(2)
            if ss == 'three':
                last.append(3)
            if ss == 'four':
                last.append(4)
            if ss == 'five':
                last.append(5)
            if ss == 'six':
                last.append(6)
            if ss == 'seven':
                last.append(7)
            if ss=='eight':
                last.append(8)
            if ss == 'nine':
                last.append(9)
            if ss == 'ten':
                last.append(10)
            if ss == 'twenty':
                last.append(20)
            if ss == 'thirty':
                last.append(30)
            if ss == 'fourty':
                last.append(40)
            if ss == 'fifty':
                last.append(50)
            if ss == 'sixty':
                last.append(60)
            if ss == 'seventy':
                last.append(70)
            if ss == 'eighty':
                last.append(80)
            if ss == 'ninety':
                last.append(90)
            if ss == 'eleven':
                last.append(11)
            if ss == 'twelve':
                last.append(12)
            if ss == 'thirteen':
                last.append(13)
            if ss == 'fourteen':
                last.append(14)
            if ss == 'fifteen':
                last.append(15)
            if ss == 'sixteen':
                last.append(16)
            if ss == 'seventeen':
                last.append(17)
            if ss == 'eighteen':
                last.append(18)
            if ss == 'nineteen':
                last.append(19)
        if length == 2:#if number of words in the string is 2
            if s[1] == 'one':
                j = '1'
            if s[1] == 'two':
                j = '2'
            if s[1] == 'three':
                j = '3'
            if s[1] == 'four':
                j = '4'
            if s[1] == 'five':
                j = '5'
            if s[1] == 'six':
                j = '6'
            if s[1] == 'seven':
                j = '7'
            if s[1] == 'eight':
                j= '8'
            if s[1] == 'nine':
                j = '9'
            if s[0] == 'twenty':#mixed one's value with ten's value
                last.append(int('2'+j))
            if s[0] == 'thirty':
                last.append(int('3'+j))
            if s[0] == 'fourty':
                last.append(int('4'+j))
            if s[0] == 'fifty':
                last.append(int('5'+j))
            if s[0] == 'sixty':
                last.append(int('6'+j))
            if s[0] == 'seventy':
                last.append(int('7'+j))
            if s[0] == 'eighty':
                last.append(int('8'+j))
            if s[0] == 'ninety':
                last.append(int('9'+j))
    print('Lexographically sorted list:\t',last)#finally printed the new list at last
l = [99,13,100]#main list 
lexographical_order(l)#used the function
'''
OUTPUT OF THE PROGRAM
Original list:   [99, 13, 100]
Lexographically sorted list:     [100, 99, 13]
'''
