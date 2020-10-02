total = int(input('Enter the no of numbers you want to find the palindrome of: '))
lst = []
for i in range(total):
    num = int(input('Enter a number: '))
    print()
    lst.append(num)
    
for values in lst:
    a = value
    while True:
        n = str(a)
        
        if str (n[::-1]) == str (n):
            if a == value:
                print('{} itself is a palindrome'.format(value))
                break
            else:
                print('The next palindrome of {} is {}'.format(n, a))
                break
        a += 1
        
  
