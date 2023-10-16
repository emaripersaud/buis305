number1=input('enter number1')
number2=input('enter number2')
number3=input('enter number3')

print(number1,number2,number3)

sum =int(number1)+int(number2)
print(sum)

difference =int(number1)-int(number2)
multiplication =int(number1)*int(number2)
division =int(number1)/int(number2)
print(difference,multiplication,division)

sum =int(number1)+int(number2)+int(number3)
difference =int(number1)-int(number2)-int(number3)
multiplication =int(number1)*int(number2)*int(number3)
division =int(number1)/int(number2)/int(number3)
print(sum,difference,multiplication,division)

#Return the value of 9 raised to the power of 3
import math
print(math.pow(9,3))

#Rounds a number up to the nearest integer
print(math.ceil(18.7))

#Checks whether a value is infitnite or not
print(math.isinf(7))

#Returns the square root of a number
print(math.sqrt(16))

#Checks whether a number if finite or not
print(math.isfinite(56))

#Returns the hyperbolic tangent of a number
print(math.tanh(89))

#Returns the inverse hyperbolic cosine of a number
print(math.acosh(75))

#Returns the absolute value of a number
print(math.fabs(8))

#Returns the greatest common divisor of two integers
print(math.gcd(25,5))

#Checks whether two values are close to each other, or not
print(math.isclose(59,32))

#Rounds a square root number downwards to the nearest integer
print(math.isqrt(64))