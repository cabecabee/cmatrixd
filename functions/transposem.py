def transposem(m):
    transposetuples = zip(*m)
    transpose = [list(row) for row in transposetuples]
    return transpose