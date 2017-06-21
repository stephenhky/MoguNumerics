
%module dldist
%{
extern int damerau_levenshtein(char *word1, char *word2);
%}

extern int damerau_levenshtein(char *word1, char *word2);