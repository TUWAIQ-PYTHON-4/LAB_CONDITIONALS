movie="Spy"
the_rating_of_the_movie_of5:int=3
popularity_score:float=72.65
#Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
if the_rating_of_the_movie_of5 >=4 and popularity_score>80:
    print("highly recomended")
elif the_rating_of_the_movie_of5 >=3 and popularity_score>70:
    print("I recommended it . It is good")
elif the_rating_of_the_movie_of5 <=2 and popularity_score>60:
    print("You should check it out!")
elif the_rating_of_the_movie_of5 <=2 and popularity_score<50:
    print("Don't watch it. It is a waste of time")