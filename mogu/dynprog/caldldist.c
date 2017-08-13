
#include <stdio.h>
#include "dldist.h"

int main(int numargs, char **words) {
  char *word1 = words[1];
  char *word2 = words[2];
  printf("%s %s %i %i\n", word1, word2, damerau_levenshtein(word1, word2), longest_common_prefix(word1, word2));
  return(0);
}
