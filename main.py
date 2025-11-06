import QuarterBackInfo
import RunningBackInfo
def main():
    best_team = []

    best_team.append(QuarterBackInfo.sorted_qb_dict[0][0])
    best_team.append(RunningBackInfo.sorted_rb_dict[0][0])

    print(f"The best quarterback is {best_team[0]} with a score of {QuarterBackInfo.sorted_qb_dict[0][1]:.2f}")
    print(f"The best running back is {best_team[1]} with a score of {RunningBackInfo.sorted_rb_dict[0][1]:.2f}")
main()