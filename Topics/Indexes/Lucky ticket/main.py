# Save the input in this variable
ticket = list(input())

# Add up the digits for each half
half_1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
half_2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

# Thanks to you, this code will work
if half_1 == half_2:
    print("Lucky")
else:
    print("Ordinary")
