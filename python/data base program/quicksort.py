def partition_array(array):
    pivot=array[-1]
    j=0
    for i in range(len(array)-1):
        if array[i]<array[-1]:
            array[j], array[i]=array[i], array[j]
            j += 1
    array[j], array[-1]=array[-1], array[j]

array=[12,19,3,8,7,20,25]
print(array)

partition_array(array)
print(array)