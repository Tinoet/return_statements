# a keyword arguement is when we have a parameter assigned to value
# add two line breaks when a funtion is defined
def greet_user(first_name, last_name):
  print(f'hi {first_name},{last_name} !')
  print('welcome aboard')

# when dealing with functions that have key record values we should use keyword arguement
# always use the positional argument before using keyword arguments
print('start')
greet_user (first_name='Elijah', last_name='Tochi')
print('finish')
# argument is the vale we apply to a function