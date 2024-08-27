def imsertion_sort():
    list=[]
    for i in range(1,len(list)):
        element=array[i]
        j=i-1
        while j>=0 and element<=array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=element
    
 names = []
print(f'Enter the {n} names')
for i in range(n):
    names.append(input())   
