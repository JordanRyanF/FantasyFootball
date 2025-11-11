#WR - 1 pt 10 yards - 6 pts TD - and -2 pts fumble lost
def point_calc(receiving_yards, receiving_tds, fumbles_lost):
    return (receiving_yards / 10) + (6 * receiving_tds) - (2 * fumbles_lost)

ceedee_lamb = point_calc(1287, 9, 1)
davante_adams = point_calc(1231, 12, 0)
jordan_addison = point_calc(1035, 8, 2)
tyreek_hill = point_calc(1196, 12, 1)
jamal_agnew = point_calc(1070, 10, 0)
keenan_allen = point_calc(1005, 8, 1)
calvin_austin = point_calc(1104, 7, 0)
alex_bachman = point_calc(980, 6, 1)
rashod_bateman = point_calc(920, 5, 2)
braxton_berrious = point_calc(890, 4, 0)
jake_bobo = point_calc(850, 5, 1)
kendrick_bourne = point_calc(780, 6, 0)
kayshon_boutte = point_calc(760, 4, 1)
dyami_brown = point_calc(730, 5, 0)
pat_bryant = point_calc(700, 3, 2)
treylon_burks = point_calc(680, 4, 1)
curtis_samuel = point_calc(650, 2, 0)
deebo_samuel = point_calc(620, 3, 1)
tyrell_shaver = point_calc(600, 4, 0)
david_sills = point_calc(580, 2, 1)
devonte_smith = point_calc(550, 3, 0)

wr_dict = {
    "CeeDee Lamb": ceedee_lamb,
    "Davante Adams": davante_adams,
    "Jordan Addison": jordan_addison,
    "Tyreek Hill": tyreek_hill,
    "Jamal Agnew": jamal_agnew,
    "Keenan Allen": keenan_allen,
    "Calvin Austin": calvin_austin,
    "Alex Bachman": alex_bachman,
    "Rashod Bateman": rashod_bateman,
    "Braxton Berrious": braxton_berrious,
    "Jake Bobo": jake_bobo,
    "Kendrick Bourne": kendrick_bourne,
    "Kayshon Boutte": kayshon_boutte,
    "Dyami Brown": dyami_brown,
    "Pat Bryant": pat_bryant,
    "Treylon Burks": treylon_burks,
    "Curtis Samuel": curtis_samuel,
    "Deebo Samuel": deebo_samuel,
    "Tyrell Shaver": tyrell_shaver,
    "David Sills": david_sills,
    "Devonte Smith": devonte_smith
}
sorted_wr_dict = sorted(wr_dict.items(), key=lambda item: item[1], reverse=True)
