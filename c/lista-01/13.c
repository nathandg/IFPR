#include <stdio.h>
#include <stdlib.h>

int main () {
  float salario, novoSalario;
  int reajuste;

  printf("Digite o salário: ");
  scanf("%f", &salario);

  if (salario <= 400){
    reajuste = 15;
  } else if (salario <= 800) {
    reajuste = 12;
  } else if (salario <= 1200) {
    reajuste = 10;
  } else if (salario <= 2000) {
    reajuste = 7;
  } else {
    reajuste = 4;
  }

  novoSalario = salario + (salario * reajuste / 100);

  printf("\n \t Salário atual: R$ %.2f\n", salario);
  printf("\t Novo salário: R$ %.2f\n", novoSalario);
  printf("\t Reajuste ganho: R$ %.2f\n", novoSalario - salario);
  printf("\t Percentual de reajuste: %d%%\n", reajuste);
  return 0;
}