number_of_lines=int(input('enter the number of lines to draw the star shaped '))
for i in range(1,number_of_lines+1):
    for j in range(1,number_of_lines+1):
        if j==1 or j==number_of_lines or i==1 or j==number_of_lines:
            print('*',end=" ")
        else:
            print(' ',end=' ')
    print()