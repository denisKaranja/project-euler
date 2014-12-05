/*#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 6(Sum square difference)--in Swift language
*/
def sumOfSquares(num):
	if num == 1:
		return 1
	else:
		return num**2 + sumOfSquares(num - 1)

def squareOfSums(num):
	if num == 1:
		return 1
	else:
		return num + squareOfSums(num - 1)

a = sumOfSquares(100)
b = squareOfSums(100)**2

diff = a - b
print abs(diff)
/*

*/

println(anyPower(2.0, 4))

func sumOfSquares(num: Int)->Int
{
	if (num == 1)
	{
		return 1
	}
	else
	{
		return ((num * num)+ sumOfSquares(num -1))
	}
}

func squareOfSums(num: Int)->Int
{
	if(num == 1)
	{
		return 1
	}
	else
	{
		return (num + squareOfSums(num - 1))
	}
}
Int a, b, diff
a = sumOfSquares(100)
b =  (squareOfSums(100) * squareOfSums(100))

diff = ((a - b) * -1)
println(diff)

