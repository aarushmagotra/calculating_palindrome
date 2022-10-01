num = int(input('Enter a number: '))
print("-------------------------")
n = num

while True:
    a = str(num)
    if a[::-1] == a:
        print('The next palindrome of {} is {}'.format(n, a))
        break
    else:
        n += 1 
#code ends here  
