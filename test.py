# # def CountOccurrences(S):
# #     # Your code goes here
# #     data_count = dict((letter, S.count(letter)) for letter in set(S))
# #     ans = []
# #     for i in S:
# #         if i not in ans:
# #             ans.append(i)
# #             ans.append(str(data_count[i]))
# #
# #     return ''.join(ans)
# #
# #
# # S = "occurrences"
# # print(CountOccurrences(S))
#
# # name = input()
# # print(name[::-1])
# a = None
# print(a[0])
# no_of_day = int(input())
# profit_on_each_day = list(map(int, input().split()))
# # print(profit_on_each_day)
# # no_of_query = int(input())
# #
# # while no_of_day :
# #     count = 0
# #     no_of_day -= 1
# #     profit_range = list(map(int, input().split())).sort()
# #     for i in profit_on_each_day:
# #         if i in range(profit_range[0], profit_range[1]):
# #         # if i >= profit_range[0] and i <= profit_range[1]:
# #             count += 1
# #
# #     print(count)
#
#
# no_of_candy = int(input())
# candy = list(map(int, input().split()))
# candy.sort()
# q_r_pair = list(map(int, input().split()))
# no_of_queries = q_r_pair[0]
# # no_of_int = q_r_pair[1]
# ans = []
# while no_of_queries:
#     i_x_k_pair = list(map(int, input().split()))
#     candy[i_x_k_pair[0]-1] = i_x_k_pair[1]
#     candy.sort()
#     ans.append(candy[i_x_k_pair[2]-1])
#     no_of_queries -= 1
#
# print(' '.join(map(str, ans)))
#

# data = [int(i) for i in input().split()]
# print(data)

with open('demo.txt', 'rw') as f:
    for line in f:
        f.writelines(4435 + line)
