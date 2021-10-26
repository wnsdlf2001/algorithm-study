def solution(lottos, win_nums):
    # 0개 6등 2개 5등 3개 4등 ~

    acc = 0
    mis = 0
    for num in lottos:
        if num in win_nums:
            acc += 1
        if num == 0:
            mis += 1

    max_val = acc + mis
    min_val = acc

    if max_val == 0:
        max_val = 6
    else:
        max_val = 7 - max_val

    if min_val == 0:
        min_val = 6
    else:
        min_val = 7 - min_val

    answer = [max_val, min_val]
    return answer


# lottos	win_nums	result
# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
# [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
# [45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]