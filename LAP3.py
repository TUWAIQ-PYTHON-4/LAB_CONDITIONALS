movie = 'first man '
RatingOfTheMovie = 2
PopularityScore = 72.65
if RatingOfTheMovie >= 4 and PopularityScore > 80:
    print('Highly recommended')
elif RatingOfTheMovie >=3 and PopularityScore >= 70:
    print('I recommended it . It is good')
elif RatingOfTheMovie <=2 and PopularityScore >=60 :
    print('You should check it out!')
else:
    print('Dont watch it. It is a waste of time')
