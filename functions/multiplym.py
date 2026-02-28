def multiplym(m1, m2):
    ans = [
        [0 for i in range(len(m2[0]))]
        for i in range(len(m1))
    ]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                ans[i][j] += m1[i][k] * m2[k][j]
    return ans