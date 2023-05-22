#calculating Volume of triangular prism
def calculate(int1, int2, int3):
	volume_of_triangle= 0.5*int1*int2*int3
	return volume_of_triangle

base=int(input("enter base\n"))
height=int(input("enter height\n"))
length=int(input("enter length\n"))
a=calculate(base, height, length)
print('Volume of triangle with', 'base: ', base , 'height: ', height, 'length: ', length,'is:',  a )


