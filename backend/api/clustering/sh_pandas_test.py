from api.models import Profile, Movie
from pandas import DataFrame

movies = Movie.objects.all()

print('movies', movies)

Data = {'movie': [25, 34, 22, 27, 33, 33, 31, 22, 35, 34, 67, 54, 57, 43, 50, 57, 59, 52, 65, 47, 49, 48, 35, 33, 44, 45, 38, 43, 51, 46],
        'rating': [79, 51, 53, 78, 59, 74, 73, 57, 69, 75, 51, 32, 40, 47, 53, 36, 35, 58, 59, 50, 25, 20, 14, 12, 20, 5, 29, 27, 8, 7]
        }

df = DataFrame(Data, columns=['movie', 'rating'])
print(df)
