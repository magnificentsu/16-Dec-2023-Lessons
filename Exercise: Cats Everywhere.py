class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Kitten 1', 10)
cat2 = Cat('Kitten 2', 20)
cat3 = Cat('Kitten 3', 30)

def oldest_cat(*args):
    return max(args)

oldest = oldest_cat(cat1.age, cat2.age, cat3.age)

print(f'The oldest cat is {oldest} years old')


# This is the first way I did it, but not the way I was asked to do it.
# I was supposed to do it using a function that I defined/created.
# I did this one first as a check, also a way for me to recall some of the thing I learned previously.
oldest_cat_age = max(cat1.age, cat2.age, cat3.age)

print(f'The oldest cat is {oldest_cat_age} years old.')