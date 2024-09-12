cities = ["Mumbai","New York","Paris"]
countries =["India","USA","France"]

z = zip(cities,countries)    #it will create a tuples
for a in z:
    print(a)

d = {city:country for city,country in zip(cities,countries)}
print(d)
