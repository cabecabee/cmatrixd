def addm(m1, m2):
    ans = []
    for i in range(len(m1)):
        line = []
        for j in range(len(m1[0])):
            line.append(m1[i][j] + m2[i][j])
        ans.append(line)
    return ans
