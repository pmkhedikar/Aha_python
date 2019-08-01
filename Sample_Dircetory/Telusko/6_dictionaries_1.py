farm_animals = {'cow', 'ox', 'hourse'}
print(farm_animals)
for animals in farm_animals:
    print(animals)

forest_animals = set(['lion', 'Elephant', 'beer'])
print(forest_animals)
for animals in forest_animals:
    print(animals)

forest_animals.add('goat')
farm_animals.add('goat')

print(forest_animals)
print(farm_animals)
