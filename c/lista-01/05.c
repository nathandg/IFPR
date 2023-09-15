#include <stdio.h>
#include <stdlib.h>

int main () {
  int valor;

  printf("Informe o valor: ");
  scanf("%d", &valor);

  int notas[] = {100, 50, 20, 10, 5, 2, 1};
  int qtd = sizeof(notas) / sizeof(int);

  for (int i = 0; i < qtd; i++) {
    int qtd = valor / notas[i];
    valor = valor % notas[i]; 
    printf("%d nota(s) de R$ %d,00\n", qtd, notas[i]);
  }

  return 0;
}