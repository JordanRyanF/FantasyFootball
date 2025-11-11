import QuarterBackInfo
import RunningBackInfo
import WideReceiverInfo
import DefenseInfo
import KickerInfo
def main():
    first_optimal_team = []
    second_optimal_team = []
    third_optimal_team = []
    #first team
    first_optimal_team.append(QuarterBackInfo.sorted_qb_dict[0][0])
    first_optimal_team.append(RunningBackInfo.sorted_rb_dict[0][0])
    first_optimal_team.append(WideReceiverInfo.sorted_wr_dict[0][0])
    first_optimal_team.append(DefenseInfo.sorted_defense_points[0][0])
    first_optimal_team.append(KickerInfo.sorted_kicker_points_dict[0][0])
    #second team
    second_optimal_team.append(QuarterBackInfo.sorted_qb_dict[1][0])
    second_optimal_team.append(RunningBackInfo.sorted_rb_dict[1][0])
    second_optimal_team.append(WideReceiverInfo.sorted_wr_dict[1][0])
    second_optimal_team.append(DefenseInfo.sorted_defense_points[1][0])
    second_optimal_team.append(KickerInfo.sorted_kicker_points_dict[1][0])
    #third team
    third_optimal_team.append(QuarterBackInfo.sorted_qb_dict[2][0])
    third_optimal_team.append(RunningBackInfo.sorted_rb_dict[2][0])
    third_optimal_team.append(WideReceiverInfo.sorted_wr_dict[2][0])
    third_optimal_team.append(DefenseInfo.sorted_defense_points[2][0])
    third_optimal_team.append(KickerInfo.sorted_kicker_points_dict[2][0])

    print(f"1st Optimal Team: \nQuarterback: {first_optimal_team[0]} \nRunning Back: {first_optimal_team[1]}\nWide Receiver: {first_optimal_team[2]}\nDefense: {first_optimal_team[3]}\nKicker: {first_optimal_team[4]}\n")
    print(f"2nd Optimal Team: \nQuarterback: {second_optimal_team[0]} \nRunning Back: {second_optimal_team[1]}\nWide Receiver: {second_optimal_team[2]}\nDefense: {second_optimal_team[3]}\nKicker: {second_optimal_team[4]}\n")
    print(f"3rd Optimal Team: \nQuarterback: {third_optimal_team[0]} \nRunning Back: {third_optimal_team[1]}\nWide Receiver: {third_optimal_team[2]}\nDefense: {third_optimal_team[3]}\nKicker: {third_optimal_team[4]}\n")


main()