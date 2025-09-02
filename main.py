import playerslist
def main():

    joe_burrow = playerslist.point_calc(4918, 9, 43)
    jared_golf = playerslist.point_calc(4629, 12, 37)
    baker_mayfield = playerslist.point_calc(4500, 16, 41)
    geno_smith = playerslist.point_calc(4320, 15, 21)
    sam_darnold = playerslist.point_calc(4319,12,35)
    lamar_jackson = playerslist.point_calc(4172, 4, 41)
    patrick_mahomes = playerslist.point_calc(3928, 11, 26)
    aaron_rogers = playerslist.point_calc(3897, 11, 28)
    justin_herbert = playerslist.point_calc(3870, 3, 23)
    brock_purdy = playerslist.point_calc(3864, 12, 20)
    kyler_murray = playerslist.point_calc(3851, 11, 21)
    bo_nix = playerslist.point_calc(3775, 12, 29)
    matthew_stafford = playerslist.point_calc(3762, 8, 20)
    josh_allen = playerslist.point_calc(3731, 6, 28)
    cj_stroud = playerslist.point_calc(3727, 12, 20)
    jayden_daniels = playerslist.point_calc(3568, 9, 25)
    caleb_williams = playerslist.point_calc(3541, 6, 20)
    kirk_cousins = playerslist.point_calc(3508, 16, 18)
    jordan_love = playerslist.point_calc(3389, 11, 25)
    jalen_hurts = playerslist.point_calc(2903, 5, 18)
    tua_tagovailoa = playerslist.point_calc(2867, 7, 19)
    russell_wilson = playerslist.point_calc(2482, 7, 19)
    bryce_young = playerslist.point_calc(2403, 9, 15)
    drake_maye = playerslist.point_calc(2276, 10, 15)
    derek_carr = playerslist.point_calc(2145, 5, 15)


    qb_dict = {
        "Joe Burrow": joe_burrow,
        "Jared Golf": jared_golf,
        "Baker Mayfield": baker_mayfield,
        "Geno Smith": geno_smith,
        "Sam Darnold": sam_darnold,
        "Lamar Jackson": lamar_jackson,
        "Patrick Mahomes": patrick_mahomes,
        "Aaron Rogers": aaron_rogers,
        "Justin Herbert": justin_herbert,
        "Brock Purdy": brock_purdy,
        "Kyler Murray": kyler_murray,
        "Bo Nix": bo_nix,
        "Matthew Stafford": matthew_stafford,
        "Josh Allen": josh_allen,
        "C.J. Stroud": cj_stroud,
        "Jayden Daniels": jayden_daniels,
        "Caleb Williams": caleb_williams,
        "Kirk Cousins": kirk_cousins,
        "Jordan Love": jordan_love,
        "Jalen Hurts": jalen_hurts,
        "Tua Tagovailoa": tua_tagovailoa,
        "Russell Wilson": russell_wilson,
        "Bryce Young": bryce_young,
        "Drake Maye": drake_maye,
        "Derek Carr": derek_carr

        }

    sorted_dict = sorted(qb_dict.items(), key=lambda item: item[1])
    
    print(qb_dict)
    print(sorted_dict)



main()