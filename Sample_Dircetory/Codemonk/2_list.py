companies = ["hackerearth", "google", "facebook"]

print(len(companies))
print(companies[0])
print(companies[1])
print(companies[2])

companies.append('classic crafts')
companies.insert(2, 'my venture')
print(companies)

comp2 = ['abc', 'xyz']

companies.extend(comp2)
print(companies)
m1 = [1, 3, 6, 7, 10, 4]
print(m1)
# m1.reverse()
# print(m1)
print(reversed(m1))
print(sorted(m1))
print(len(m1))