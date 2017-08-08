

cdef extern from "dldist.c":
    int damerau_levenshtein(char *word1, char *word2)