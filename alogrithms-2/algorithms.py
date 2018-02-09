# def smallest_number(x):
#     flag = False
#     while flag == False:
#         truth_tester = []
#         for i in range(1, x):
#             if x % i != 0:
#                 truth_tester.append(False)
#             else:
#                 truth_tester.append(True)
#         for i in range(len(truth_tester) -1) :
#             if truth_tester[i] and truth_tester[i + 1] == True:
#                 flag = True
#                 print truth_tester
#             else:
#                 flag = False
#                 x += 1
#                 break
#         if flag == True:
#             break
#     return x


# print smallest_number(3)        

def isPalindrome(x):
    reversed_number = []
    x = str(x)
    length = len(x)
    
    for i in range(length, 0, -1):
        reversed_number.append(x[i - 1])
    reversed_number = ''.join(reversed_number) 
    
    # print reversed_number
    
    if reversed_number == x:
        return True
    else:
        return False
# assert(isPalindrome(404) != True) 'This number is not a palindrome'
# print isPalindrome(404)

def get_largest_palindrome(x):
    y = x
    for i in range(x, 0, -1):
        product = x * y
        
        if isPalindrome(product) == True:
            return product
        else:
            x -= 1

# print get_largest_palindrome(999)

# assert isPalindrome(0) == True, 'This number is not a palindrome'
# assert isPalindrome(292) == True, 'This number is not a palindrome'
# assert isPalindrome(323) == True, 'This number is not a palindrome'
# assert isPalindrome(131) == True, 'This number is not a palindrome'

def sing_along(x):
    for i in range(x,0,-1):
        beer = 'beer'
        if i % 7 == 0:
            beer = 'Miller'
        elif i % 5 ==0:
            beer = 'Lite Beer'
        elif i % 5 == 0 and i % 7 == 0:
            beer = 'Miller Lite'
        
        return '%d bottles of %s on the wall, %d bottles %s, take one down pass it around. %d bottles of %s on the wall' % (i, beer, i, beer, i, beer)
        
print sing_along(99)
