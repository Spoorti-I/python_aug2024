#program to find 2nd smallest digit in a number
input_number=int(input('enter a number'))
small_digit=9
smallest_digit=9
temp_number=input_number
while input_number != 0:
    digit=input_number%10
    input_number=input_number//10
    if smallest_digit>digit:
        small_digit=smallest_digit
        smallest_digit=digit
    elif digit < small_digit :
        small_digit=digit
print('2nd smallest digit in is',smallest_digit)
         


