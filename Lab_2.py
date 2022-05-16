movie_1 = "Memory"

#value rating the movie 
rating_movie1: int = 3

#value popularity score the movie
popularity_score: float = 72.65

if rating_movie1 > 4 and popularity_score > 80:
    print(movie_1 +" "+ "Highly recommended")

elif rating_movie1 >= 3 and popularity_score > 70:
    print(movie_1 +" "+ "I recommended it . It is good")

elif rating_movie1 <= 2 and popularity_score > 60:
    print(movie_1 +" "+ "You should check it out!")
else :
    print(movie_1 +" "+ "Don't watch it. It is a waste of time")