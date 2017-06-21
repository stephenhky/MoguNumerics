
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

#include <string.h>
#include <stdio.h>

int damerau_levenshtein(char *word1, char *word2)
{
  int len1 = strlen(word1);
  int len2 = strlen(word2);

  int matrix[len1+1][len2+1];
  for (int i=0; i<=len1; i++) matrix[i][0] = i;
  for (int j=0; j<=len2; j++) matrix[0][j] = j;

  for (int i=1; i<=len1; i++) {
    for (int j=1; j<=len2; j++) {
      int cost = 0;
      if (word1[i]!=word2[j]) cost = 1;
      int delcost = matrix[i-1][j] + 1;
      int inscost = matrix[i][j-1] + 1;
      int subcost = matrix[i-1][j-1] + cost;
      int score = MIN(MIN(delcost, inscost), subcost);
      if ((i>1) & (j>1) & (word1[i]==word2[j-1]) & (word1[i-1]==word2[j])) {
	    score = MIN(score, matrix[i-2][j-2]+cost);
      }
      matrix[i][j] = score;
    }
  }
//  for (int i=0; i<=len1; i++) {
//    for (int j=0; j<=len2; j++) {
//      printf("%i ", matrix[i][j]);
//    }
//    printf("\n");
//  }
  return(matrix[len1][len2]);
}

int main(int numargs, char **words) {
  char *word1 = words[1];
  char *word2 = words[2];
  printf("%s %s %i\n", word1, word2, damerau_levenshtein(word1, word2));
  return(0);
}
