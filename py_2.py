movie:str="AL-ostoorh"
rating:int=3
popularity:float=72.65

if rating == 4 and popularity >80:
    print("Highly recommended")
elif rating == 3 and popularity > 70:
    print("I recommended it . It is good")
elif rating == 3 and popularity >=60:
    print("ou should check it out!")  
else:
     print("Don't watch it. It is a waste of time")
  