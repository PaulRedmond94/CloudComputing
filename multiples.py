#declare variables
sum = 0
for x in range (0,1000):
	if x % 3 == 0:
		sum+=x
	elif x%5 == 0:
		sum+=x

print("The sum of the values is: " )
print(sum)

#I used a for loop for this as it goes through each number individually
"""I checked the modulus of the number to make sure that only the right numbers would be added. I then printed the sum"""