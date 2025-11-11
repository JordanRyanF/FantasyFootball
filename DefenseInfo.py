# sacks 1 pt / intercept 2 pts / fumbs rec 2 pt / safeties 2 pt / def td 6 pts/ pts allowed 0 = 10 pts / 1-6 = 7 pts / 7-13 = 4 pts / 14-20 = 1 pt / 21-27 = 0 pts / 28-34 = -1 pt / 35+ = -4 pts
def calculate_defense_points(sacks, interceptions, fumble_recoveries, safeties, defensive_touchdowns, points_allowed):
    points = 0
    
    # Calculate points from sacks
    points += sacks * 1
    
    # Calculate points from interceptions
    points += interceptions * 2
    
    # Calculate points from fumble recoveries
    points += fumble_recoveries * 2
    
    # Calculate points from safeties
    points += safeties * 2
    
    # Calculate points from defensive touchdowns
    points += defensive_touchdowns * 6
    
    # Calculate points from points allowed
    if points_allowed == 0:
        points += 10
    elif 1 <= points_allowed <= 6:
        points += 7
    elif 7 <= points_allowed <= 13:
        points += 4
    elif 14 <= points_allowed <= 20:
        points += 1
    elif 21 <= points_allowed <= 27:
        points += 0
    elif 28 <= points_allowed <= 34:
        points -= 1
    elif points_allowed >= 35:
        points -= 4
    
    return points

dallas_defense_points = calculate_defense_points(3, 2, 1, 0, 1, 17)
bucs_defense_points = calculate_defense_points(1, 0, 0, 1, 0, 28)
eagles_defense_points = calculate_defense_points(4, 1, 2, 0, 2, 10)
vikings_defense_points = calculate_defense_points(2, 3, 1, 0, 0, 7)
washington_defense_points = calculate_defense_points(0, 1, 0, 0, 0, 35)
rams_defense_points = calculate_defense_points(5, 2, 1, 1, 1, 3)
giants_defense_points = calculate_defense_points(1, 0, 0, 0, 0, 21)
patriots_defense_points = calculate_defense_points(2, 1, 1, 0, 0, 14)
bears_defense_points = calculate_defense_points(3, 2, 0, 0, 1, 0)
packers_defense_points = calculate_defense_points(4, 1, 2, 0, 0, 6)
steelers_defense_points = calculate_defense_points(2, 0, 1, 1, 0, 30)
chiefs_defense_points = calculate_defense_points(1, 1, 0, 0, 0, 27)
raiders_defense_points = calculate_defense_points(3, 2, 1, 0, 1, 12)
bengals_defense_points = calculate_defense_points(0, 0, 0, 0, 0, 40)
lions_defense_points = calculate_defense_points(2, 1, 1, 0, 0, 18)
colts_defense_points = calculate_defense_points(1, 0, 0, 0, 0, 22)
broncos_defense_points = calculate_defense_points(4, 2, 1, 1, 1, 9)
texans_defense_points = calculate_defense_points(0, 1, 0, 0, 0, 33)
chargers_defense_points = calculate_defense_points(3, 0, 1, 0, 0, 15)
jaguars_defense_points = calculate_defense_points(2, 1, 0, 0, 0, 26)
titans_defense_points = calculate_defense_points(1, 2, 1, 0, 0, 5)

dict_defense_points = {
    "Dallas Defense": dallas_defense_points,
    "Bucs Defense": bucs_defense_points,
    "Eagles Defense": eagles_defense_points,
    "Vikings Defense": vikings_defense_points,
    "Washington Defense": washington_defense_points,
    "Rams Defense": rams_defense_points,
    "Giants Defense": giants_defense_points,
    "Patriots Defense": patriots_defense_points,
    "Bears Defense": bears_defense_points,
    "Packers Defense": packers_defense_points,
    "Steelers Defense": steelers_defense_points,
    "Chiefs Defense": chiefs_defense_points,
    "Raiders Defense": raiders_defense_points,
    "Bengals Defense": bengals_defense_points,
    "Lions Defense": lions_defense_points,
    "Colts Defense": colts_defense_points,
    "Broncos Defense": broncos_defense_points,
    "Texans Defense": texans_defense_points,
    "Chargers Defense": chargers_defense_points,
    "Jaguars Defense": jaguars_defense_points,
    "Titans Defense": titans_defense_points
}
sorted_defense_points = sorted(dict_defense_points.items(), key=lambda item: item[1], reverse=True)