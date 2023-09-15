#include <stdio.h>
#include <stdlib.h>

int main () {

  int num;

  printf("Digite um número: ");
  scanf("%d", &num);

  if (num % 3 == 0) {
    printf("O número %d é múltiplo de 3\n", num);
  } else {
    printf("O número %d não é múltiplo de 3\n", num);
  }

  return 0;
}