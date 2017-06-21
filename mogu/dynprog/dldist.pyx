cdef extern from "dldist.h"
    int damerau_levenshtein(char *word1, char *word2)