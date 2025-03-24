def duplicate(cities):
    result = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2: # 중복값이 들어옴
            result.append(city)
    return result

cities = ['Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul']
# city = {'Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul'}
cities.append('Anyang')
cities.append('Seoul')
print(cities)
print(duplicate(cities))