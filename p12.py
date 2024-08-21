#program to find perfect square
import math
input_number=int(input('enter the input number'))
route_number=math.sqrt(input_number)
route_number=math.floor(route_number)
product_nuber=route_number*route_number
if route_number==input_number:
    print('input number is perfect square')
else:
    print('input number is not perfect square')