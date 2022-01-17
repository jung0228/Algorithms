def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = [0] * len(id_list)

    check = [[0 for i in range(len(id_list))] for j in range(len(id_list))]
    for i in report:
        a, b = i.split()
        A = id_list.index(a)
        B = id_list.index(b)
        if check[A][B] == 0:
            check[A][B] = 1
            reported[B] += 1

    for i in range(len(id_list)):
        for j in range(len(id_list)):
            if check[i][j] == 1:
                
                if reported[j] >= k:
                    answer[i] += 1

    return answer