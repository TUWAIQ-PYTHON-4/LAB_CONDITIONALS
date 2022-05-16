# Create a variable for the movie (choose any movie you like)
fav_movie = "1917 film"

# Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
rat_movie:int = 3

# Create a popularity score of type float , let it be 72.65
pop_score_movie:float = 72.65

# Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
if rat_movie >= 4 and pop_score_movie > 80 :
    print("Highly recommended")

 # else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
elif rat_movie >= 3 and pop_score_movie > 70 :
    print("I recommended it . It is good")
    
# else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
elif rat_movie <= 2 and pop_score_movie > 60 :
    print("You should check it out!") 

# else the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"
elif rat_movie <=2 and pop_score_movie < 50 :
    print("Don't watch it. It is a waste of time")       