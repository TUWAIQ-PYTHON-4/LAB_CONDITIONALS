from ast import IfExp


movie = "mad max"
rate :int =3
score :float =72.64
if(rate>=4 and score>80):
    print("highly recommended")
elif (rate>=3 and score>70):
     print("I recommended it . it is good")
elif(rate<=2 and score >60):
    print("you chould chek it out")     
else:
    print("dont watch it it is waste your time")

