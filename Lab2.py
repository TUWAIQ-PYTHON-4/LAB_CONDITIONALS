movie:str = "Doctor strange madness of multiverse"
rating_movie:int = 3
popularity:float = 72.65
if rating_movie >= 4 and popularity > 80:
    print("Highly recommended")
elif rating_movie >= 3 and popularity >= 70:
    print("I recommended it . It is good")
elif rating_movie <= 2 and popularity > 60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")