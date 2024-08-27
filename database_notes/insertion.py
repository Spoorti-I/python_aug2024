list=[]

for i in range(1,len(list)):
    element=array[i]
    j=i-1
    while j>=0 and element<=array[j]:
        array[j+1]=array[j]
        j=j-1
    array[j+1]=element