n = int(input("Enter a number: "))
first_digit = n//10
second_digit = n%10
swapped_number = (second_digit*10)+first_digit
print (swapped_number)