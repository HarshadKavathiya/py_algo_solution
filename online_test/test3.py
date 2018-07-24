total_team = int(input())

count = total_team/2

while True:
    score_a = 0
    score_b = 0
    no_of_player_in_each_team = input()
    # team_a_score_list = [int(i) for i in input().split()]
    # team_b_score_list = [int(i) for i in input().split()]
    team_a_score_list = tuple(map(int, input().split()))
    team_b_score_list = tuple(map(int, input().split()))

    for a, b in zip(team_a_score_list, team_b_score_list):
        if a > b:
            score_a += 1
        if a < b:
            score_b += 1

    print(score_a, score_b)
    count -= 1
    if count == 0:
        break

