beer1_sgend = [1,0.5,0.3,0.5,0.4]
beer1_sgstart = [2.0,0.6,0.4,0.9,0.7]
beer2_sgend = [0.3,0.2,0.4,1,1.5]
beer2_sgstart = [0.6,0.4,0.5,1.5,2]
beer3_sgend = [0.7,0.2,0.3,0.4,0.8]
beer3_sgstart = [0.9,0.5,0.7,0.8,2]
def ABV(beer_sgstart, beer_sgend):
  beer_len = len(beer_sgstart)
  beer_abv = []
  for i in range(beer_len):
    abv = ((1.05/0.79)*((beer_sgstart[i] - beer_sgend[i]) / beer_sgend[i])) * 100
    beer_abv.append(abv)
  return beer_abv

def avg_abv(beer_abv):
    return round(sum(beer_abv)/len(beer_abv), 3)


def abv_type(avg_abv):
  if(avg_abv > 6):
    return "strong"
  elif(avg_abv >= 5):
    return "medium"
  else:
    return "weak"

print(ABV(beer1_sgstart, beer1_sgend))
print(ABV(beer2_sgstart, beer2_sgend))
print(ABV(beer3_sgstart, beer3_sgend))


print("The average AVG of beer variety {} is {}".format("beer1",avg_abv(ABV(beer1_sgstart, beer1_sgend))))
print("The average AVG of beer variety {} is {}".format("beer2",avg_abv(ABV(beer2_sgstart, beer2_sgend))))
print("The average AVG of beer variety {} is {}".format("beer3",avg_abv(ABV(beer3_sgstart, beer3_sgend))))

print(abv_type(avg_abv(ABV(beer1_sgstart, beer1_sgend))))
print(abv_type(avg_abv(ABV(beer2_sgstart, beer2_sgend))))
print(abv_type(avg_abv(ABV(beer3_sgstart, beer3_sgend))))
