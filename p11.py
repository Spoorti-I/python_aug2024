input_num=int(input('enter a number to print math table '))
for i in range(1,15):
    print('%02d * %02d = %03d'%(input_num,i,input_num*i))