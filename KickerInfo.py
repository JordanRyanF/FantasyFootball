# extra point - 1 / field goal 0 - 49 yards - 3 / field goal %)+ yards 5
def calculate_kicker_points(extra_points_made, field_goals_0_49_made, field_goals_50_plus_made ):
    return (extra_points_made * 1) + (field_goals_0_49_made * 3) + (field_goals_50_plus_made * 5)

mason_crosby_points = calculate_kicker_points(2, 3, 1)
harrison_butker_points = calculate_kicker_points(1, 4, 0)
justin_tucker_points = calculate_kicker_points(3, 2, 1)
robbie_gould_points = calculate_kicker_points(0, 5, 0)
nick_folk_points = calculate_kicker_points(4, 1, 0)
ryan_succop_points = calculate_kicker_points(2, 2, 1)
chris_boswell_points = calculate_kicker_points(3, 3, 0)
wil_lutz_points = calculate_kicker_points(1, 4, 1)
dan_bailey_points = calculate_kicker_points(2, 3, 0)
greg_zuerlein_points = calculate_kicker_points(0, 2, 2)
matt_prater_points = calculate_kicker_points(3, 1, 1)
adam_vinatieri_points = calculate_kicker_points(4, 0, 0)
gary_anderson_points = calculate_kicker_points(2, 2, 0)
jason_elam_points = calculate_kicker_points(1, 3, 1)
matt_bryant_points = calculate_kicker_points(3, 2, 0)
lou_graza_points = calculate_kicker_points(0, 4, 0)
dan_bailey_points = calculate_kicker_points(2, 1, 1)
shayne_graham_points = calculate_kicker_points(3, 0, 2)

dict_kicker_points = {
    "Mason Crosby": mason_crosby_points,
    "Harrison Butker": harrison_butker_points,
    "Justin Tucker": justin_tucker_points,
    "Robbie Gould": robbie_gould_points,
    "Nick Folk": nick_folk_points,
    "Ryan Succop": ryan_succop_points,
    "Chris Boswell": chris_boswell_points,
    "Wil Lutz": wil_lutz_points,
    "Dan Bailey": dan_bailey_points,
    "Greg Zuerlein": greg_zuerlein_points,
    "Matt Prater": matt_prater_points,
    "Adam Vinatieri": adam_vinatieri_points,
    "Gary Anderson": gary_anderson_points,
    "Jason Elam": jason_elam_points,
    "Matt Bryant": matt_bryant_points,
    "Lou Groza": lou_graza_points,
    "Dan Bailey": dan_bailey_points,
    "Shayne Graham": shayne_graham_points
}       

sorted_kicker_points_dict = sorted(dict_kicker_points.items(), key=lambda x: x[1], reverse=True)

