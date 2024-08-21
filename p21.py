#x shaed *
number_of_lines=int(input('enter the number of lines to draw the star shaped '))
for i in range(1,number_of_lines+1):
    for j in range(1,number_of_lines+1):
        if i==j or j==number_of_lines-i+1:
            print('*',end=" ")
        else:
            print(' ',end='')
    print()