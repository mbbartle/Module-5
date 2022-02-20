# Create a tuple named pokemon that holds the strings 'picachu', 'charmander', and 'bulbasaur'.
pokemon = ('picachu', 'charmander', 'bulbasaur')

# Using index notation, print() the string that located at index 1 in pokemon
print(pokemon[1])

# Unpack the values of pokemon into the following three new variables with names starter1, starter2, starter3.
starter1, starter2, starter3 = pokemon

# Create a tuple using the tuple() built-in, that contains the letters of your name.
my_name = tuple('michael')

# Check whether the character i is in your tuple representation of your name.
is_i_in_tuple = 'i' in my_name

# Write a for loop that prints out the integers 2 through 10, each on a new line, by using the range() function.
for i in range(2,11):
    print(i)

# Use a while loop that prints out the integers 2 through 10.
while_variable = 2
while while_variable < 11:
    print(while_variable)
    while_variable += 1

# Write a for loop that iterates over the string 'This is a simple string' and prints each character.
for i in 'This is a simple string':
    print(i)

# Using a nested for loop, iterate over the following set ('this', 'is', 'a', 'simple', 'set') and print each word, three times.
for i in ('this', 'is', 'a', 'simple', 'set'):
    for j in range(3):
        print(i)