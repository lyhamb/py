# Ask the user to choose the longest row of the triangle
while True:
    triangle_width = int(input("Please enter the desired width of the triangle: "))
    if triangle_width > 50:
        print("Please enter a number between 0 and 50.")
    elif triangle_width < 0:
        print("Please enter a number between 0 and 50.")
    else:
        break
        
# Ask the user to choose the character to be repeated within the triangle
while True:
    pattern = str(input("What character would you like to display? "))
    
    if len(pattern) == 1:
        break
    else:
        print("Please enter only one character.")
    
# Start loop to create the triangle pattern based on user inputs
for num in range(1, (triangle_width * 2)):

    # Add a pattern instance until row number is equal to width variable
    if num <= triangle_width:
        print_pattern = pattern * num

    # Remove a pattern instance for each row number greater than the width variable
    else:
        count_down = (triangle_width * 2) - num
        print_pattern = pattern * count_down

    # Output triangle
    print(print_pattern)

