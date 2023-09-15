#include <stdio.h>
#include <stdlib.h>

int main () {

  int ddd;

  printf("Digite o DDD: ");
  scanf("%d", &ddd);

  struct ddd {
    int ddd;
    char cidade[30];
  };

  struct ddd ddds[] = {
    {61, "Brasilia"},
    {71, "Salvador"},
    {11, "Sao Paulo"},
    {21, "Rio de Janeiro"},
    {32, "Juiz de Fora"},
    {19, "Campinas"},
    {27, "Vitoria"},
    {31, "Belo Horizonte"}
  };

  int ddds_length = sizeof(ddds) / sizeof(ddds[0]);

  for (int i = 0; i < ddds_length; i++) {
    if (ddd == ddds[i].ddd) {
      printf("%s \n", ddds[i].cidade);
      return 0;
    }
  }

  printf("DDD nao cadastrado \n");
  return 0;
}