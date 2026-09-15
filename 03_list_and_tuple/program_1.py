# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

movies = []
for i in range(3):
    movies.append(input("Enter the name of your favorite movie: "))
print(movies)