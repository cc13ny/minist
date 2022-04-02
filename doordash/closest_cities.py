city_locs = []
city_locs.append(('new_york_city', 1, 3))

city_locs.append(('ny_1', 1, 4))
city_locs.append(('ny_2', 2, 3))

city_locs.append(('ny_3', 1, 5))
city_locs.append(('ny_4', 3, 3))
city_locs.append(('boston', 2, 4))
city_locs.append(('maryland', 4, 6))
city_locs.append(('mr_1', 4, 7))

import collections
import bisect

# 1. It's easy to cause errors by Copy and Paste
# 2. bisect_left instead of bisect
# 3. pay attention
#      if the absolute difference is the same, we should assign the city name based on the alphabetic order


def find_closest_cities(city_locs_tuple, city_queries):
    def assign_closest_city(cur_diff, next_diff, cur_city, next_city):
        print(cur_diff, next_diff, cur_city, next_city)
        if next_diff < cur_diff:
            cur_diff = next_diff
            cur_city = next_city

        if next_diff == cur_diff:
            cur_city = min(cur_city, next_city)

        print(cur_diff, cur_city)
        print('=' * 20)
        return cur_diff, cur_city

    # Step 1:
    x_cities, y_cities = collections.defaultdict(list), collections.defaultdict(list)
    city_locs = {}
    for city, x, y in city_locs_tuple:
        bisect.insort(x_cities[x], (y, city))
        bisect.insort(y_cities[y], (x, city))
        city_locs[city] = (x, y)

    # Step 2:
    res = []
    for city in city_queries:
        diff = float('inf')
        ncity = 'None'

        if city not in city_locs:
            res.append(ncity)
            continue

        x, y = city_locs[city]
        cities1, cities2 = x_cities[x], y_cities[y]
        # print(cities1)
        # print(cities2)

        ny = bisect.bisect_left(cities1, (y, city))
        nx = bisect.bisect_left(cities2, (x, city))

        if ny+1 < len(cities1):
            print('Step 1')
            y_diff = cities1[ny+1][0] - y
            y_city = cities1[ny+1][1]

            diff, ncity = assign_closest_city(diff, y_diff, ncity, y_city)

        if 0 <= ny - 1:
            print('Step 2')
            print(y)
            print(ny)
            print(cities1)
            y_diff = y - cities1[ny-1][0]
            y_city = cities1[ny-1][1]

            diff, ncity = assign_closest_city(diff, y_diff, ncity, y_city)

        if nx+1 < len(cities2):
            print('Step 3')
            x_diff = cities2[nx+1][0] - x
            x_city = cities2[nx+1][1]

            diff, ncity = assign_closest_city(diff, x_diff, ncity, x_city)

        if 0 <= nx - 1:
            print('Step 4')
            x_diff = x - cities2[nx-1][0]
            x_city = cities2[nx-1][1]

            diff, ncity = assign_closest_city(diff, x_diff, ncity, x_city)

        res.append(ncity)

    print(x_cities)
    print(y_cities)
    return res


# ['new_york_city', 'boston', 'maryland', 'ny_2']
# [boston', 'maryland', 'ny_2']

print(find_closest_cities(city_locs, ['new_york_city', 'boston', 'maryland', 'ny_2']))




