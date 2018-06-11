
import numpy as np
cimport numpy as np

def longest_common_prefix(unsigned char[:] word1, unsigned char[:] word2):
    cdef int len1 = word1.shape[0]
    cdef int len2 = word2.shape[0]

    cdef int lcp = 0
    cdef int i

    for i in range(min(len1, len2)):
        if word1[i] == word2[i]:
            lcp += 1
        else:
            break

    return lcp

