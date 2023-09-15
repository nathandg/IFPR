#include <stdio.h>
#include <stdlib.h>

int main () {

  float num;

  printf("Informe um número inteiro: ");
  scanf("%f", &num);

  (num > 50)
  ? printf("A metade de %.0f é %.0f \n", num, num / 2)
  : printf("O dobro de %.0f é %.0f \n", num, num * 2);

  return 0;
}