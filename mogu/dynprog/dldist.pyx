
import numpy as np
cimport numpy as np

def damerau_levenshtein(unsigned char[:] word1, unsigned char[:] word2):
    cdef int len1 = word1.shape[0]
    cdef int len2 = word2.shape[0]

    cdef int i, j
    cdef int cost, delcost, inscost, subcost, score

    cdef int[:, :] matrix = np.zeros((len1+1, len2+1));

    for i in range(len1+1):
        matrix[i][0] = i
    for j in range(len2+1):
        matrix[0][j] = j

    for i in range(len1+1):
        for j in range(len2+1):
            cost = 0
            if (word1[i]!=word2[j]):
                cost = 1
            delcost = matrix[i-1][j] + 1
            inscost = matrix[i][j-1] + 1
            subcost = matrix[i-1][j-1] + cost
            score = min(min(delcost, inscost), subcost)
            if ((i>1) & (j>1) & (word1[i]==word2[j-1]) & (word1[i-1]==word2[j])):
                score = min(score, matrix[i-2][j-2]+cost)
            matrix[i][j] = score

    return matrix[len1][len2]
