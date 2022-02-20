# Create a list named food with two elements 'rice' and 'beans'.
food = ['rice', 'beans']

# Append the string 'broccoli' to food using .append().
food.append('broccoli')

# Add the strings 'bread' and 'pizza' to food using .extend().
food.extend(['bread', 'pizza'])

# Print the first two items in the food list using print() and slicing notation.
print(food[:2])

# Print the last item in food using print() and index notation.
print(food[-1])

# Create a list called breakfast from the string "eggs,fruit,orange juice" using the split() method.
breakfast = "eggs,fruit,orange juice".split(',')

# Verify that breakfast has 3 elements using the len built-in.
len(breakfast) == 3

# prompts the user for a floating-point value until they enter stop. Store their entries in a list, and then find the average, min, and max of their entries and print them those values.
users_values = []
while True:
    input_val = input('Enter a floating-point, or "stop": ')
    if input_val == 'stop':
        break
    try: # Adding try-except because case where user does not put in a floating point value.
        users_values.append(float(input_val))
    except ValueError:
        pass
    
print(f''' Thank you!
    Average is {sum(users_values)/len(users_values)}, 
    min is {min(users_values)}, 
    max is {max(users_values)}. 
    :) '''
    )