#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main () {
  float altura, raio, m2, pi;
  int valor, latas;

  pi = 3.14159265359;

  printf("Informe a altura do cilindro: ");
  scanf("%f", &altura);

  printf("Informe o raio do cilindro: ");
  scanf("%f", &raio);

  m2 = pi * (raio * raio) + (2 * pi * raio * altura);

  printf("A área do cilindro é: %.2f\n", m2);

  latas = ceil(m2 / 15);
  valor = latas * 50;

  printf("A quantidade de latas necessárias é: %d\n", latas);
  printf("O valor total é: R$%d\n", valor);

  return 0;  
}