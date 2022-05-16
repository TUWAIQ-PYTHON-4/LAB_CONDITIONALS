#  Create a variable for the movie (choose any movie you like)
movieName:str="zero Day"
# Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
rate:int = 3
# Create a popularity score of type float , let it be 72.65
popularScore:float =72.65
# Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
if rate >=4 and popularScore > 80:
    print("Highly recommended")
# the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
elif rate >=3 and popularScore > 70:
    print("I recommended it . It is good") 
# the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
elif rate <= 2 and popularScore > 60:
    print("You should check it out!")
# the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"
else:
    print("Don't watch it. It is a waste of time")