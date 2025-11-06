# running back fantasy points are calculated by rushing yard (1 point per 10 yards), rush td (6 points each), reception (1 point each), receiving yards (1 point per 10 yards), receiving td (6 points each), fumbles lost (-2 points each)
def point_calc(rushing_yards, rushing_tds, fumbles_lost):
    return (rushing_yards / 10) + (6 * rushing_tds) - (2 * fumbles_lost)
saquon_barkley = point_calc(1032, 5, 1)
derrick_henry = point_calc(2027, 17, 2)
bijan_robinson = point_calc(1072, 12, 0)
jonathan_taylor = point_calc(911, 11, 3)
jahmyr_gibbs = point_calc(809, 5, 1)
josh_jacobs = point_calc(1298, 12, 2)
kyren_williams = point_calc(625, 3, 0)
chubba_hubbard = point_calc(1012, 7, 1)
aaron_jones = point_calc(799, 7, 1)
bucky_irving = point_calc(847, 5, 2)
james_conner = point_calc(741, 6, 1)
rico_dowdle = point_calc(533, 4, 0)
tony_pollard = point_calc(568, 3, 1)
najee_harris = point_calc(679, 5, 2)
joe_mixon = point_calc(616, 4, 1)
james_cook = point_calc(544, 3, 0)
chase_brown = point_calc(576, 2, 1)
dandre_swift = point_calc(530, 3, 1)
alvin_kamara = point_calc(516, 2, 0)
lamar_jackson = point_calc(423, 1, 0)
devon_achane = point_calc(420, 2, 0)
jk_dobbins = point_calc(429, 3, 1)
jayden_daniels = point_calc(389, 2, 0)

rb_dict = {
    "Saquon Barkley": saquon_barkley,
    "Derrick Henry": derrick_henry,
    "Bijan Robinson": bijan_robinson,
    "Jonathan Taylor": jonathan_taylor,
    "Jahmyr Gibbs": jahmyr_gibbs,
    "Josh Jacobs": josh_jacobs,
    "Kyren Williams": kyren_williams,
    "Chubba Hubbard": chubba_hubbard,
    "Aaron Jones": aaron_jones,
    "Bucky Irving": bucky_irving,
    "James Conner": james_conner,
    "Rico Dowdle": rico_dowdle,
    "Tony Pollard": tony_pollard,
    "Najee Harris": najee_harris,
    "Joe Mixon": joe_mixon,
    "James Cook": james_cook,
    "Chase Brown": chase_brown,
    "D'Andre Swift": dandre_swift,
    "Alvin Kamara": alvin_kamara,
    "Lamar Jackson": lamar_jackson,
    "Devon Achane": devon_achane,
    "J.K. Dobbins": jk_dobbins,
    "Jayden Daniels": jayden_daniels
}
sorted_rb_dict = sorted(rb_dict.items(), key=lambda item: item[1], reverse=True)