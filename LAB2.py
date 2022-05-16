fav_movie = "1917 film"
rat_movie:int = 3
pop_score_movie:float = 72.65

if rat_movie >= 4 and pop_score_movie > 80:
    print("Highly recommended")
elif rat_movie >= 3 and pop_score_movie > 70:
    print("I recommended it . It is good")

elif rat_movie <= 2 and pop_score_movie > 60:
    print("You should check it out!") 

else: # there is no need to put the condition (else the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time")
    print("Don't watch it. It is a waste of time")       