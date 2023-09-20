#include <stdio.h>
#include <stdlib.h>

int main() {

  int distancia;
  float litros, consumo;

  printf("Digite a distância percorrida (km): ");
  scanf("%d", &distancia);

  printf("Digite a quantidade de litros consumidos: ");
  scanf("%f", &litros);

  consumo = distancia / litros;
  printf("O consumo médio é de %.2f km/l \n", consumo);

  return 0;
}