#declare variables
number1, number2, sum =1, 1, 0

while number2<4000000:
	number1,number2 = number2, number1+number2
	if number1%2==0:
				sum+=number1

#end while

print("The value is: ")
print(sum)

#I used a while loop for this question as I felt that a while loop would be easier to use rather than a for loop. I checked the modulus of the first number to make sure the number was an even number. If it was, I added it to the sum
