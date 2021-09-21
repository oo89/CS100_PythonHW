
# Exercise 1
print("Exercise 1")
print("Type students grades in capital letters separate with a comma")
grades=input()
#I did this because I was learning how to input in this language. The code without the input is there too.
#grades = ['A', 'A', 'A', 'A', 'A', 'B', 'A', 'C', 'A', 'B']
frequency = [grades.count('A'),grades.count('B'),grades.count('C'),grades.count('D'),grades.count('F')]
print(frequency)
print('\n')

# Exercise 2
print("Exercise 2a")
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuhua']
print(dog_breeds)
print('\n')

print("Exercise 2b")
herding_dogs = dog_breeds[0:2]
print(herding_dogs)
print('\n')

print("Exercise 2c")
tiny_dogs = [dog_breeds[-1]]
print(tiny_dogs)
print('\n')

print("Exercise 2d")
appears = 'Persian' in dog_breeds
print(appears)
