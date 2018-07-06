no_of_test = int(input())
ans = []

while(no_of_test >= 1):
    no_of_test -= 1
    no_of_plot_cost = input()
    no_of_plot, cost_limit_for_each_plot = [int(i) for i in no_of_plot_cost.split()]

    all_plot_prize = input()
    all_plot_prize_list = [int(j) for j in all_plot_prize.split()]

    expected_profit_per_plot =  []

    for each_plot in all_plot_prize_list:
        expected_profit_per_plot.append(cost_limit_for_each_plot - each_plot)

    final_profit_list = []
    k = 0
    temp_sum = 0
    while k < no_of_plot:
        if expected_profit_per_plot[k] >= 0:
            temp_sum = temp_sum + expected_profit_per_plot[k]

        if expected_profit_per_plot[k] < 0 or k == no_of_plot-1:
            final_profit_list.append(temp_sum)
            temp_sum = 0

        k = k + 1

    max_val = 0
    for l in final_profit_list:
        if l > max_val:
            max_val = l

    ans.append(max_val)

for each_profit in ans:
    print(each_profit)

