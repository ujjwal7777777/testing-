algorithm = 'neural networks'
print(len(algorithm))
#print(f"The total number of characters in the list of algorithm is : {len(algorithm)}")
##################
superhero = 'spiderman'
print(len(superhero))
#print(f"The total number of characters in the list of superhero is : {len(superhero)}")
# using  count() to the follwing terms in the string
books = "Python for everyone"
e_counts = books.lower().count('e')
print("The total number of 'e's in the list of book is : " + str(e_counts))
##############
books = "python is the only programming language that you need to learn"
e_counts = books.lower().count('o')
print(f"The total number of 'o's in the list of book is : {e_counts}")
###############
city = "my city is shamli and shamli is my hometown"
print(city.count("shamli"))
#print(f"The total number of 'shamli's in the list of city is : {city.count('shamli')}")
###############
city  ="my city is shamli and shamli is my hometown"
print(city.count("is"))
#print(f"The total number of 'is's in the list of city is : {city.count('is')}")