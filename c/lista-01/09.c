#include <stdio.h>
#include <stdlib.h>

int main () {

  float nota1, nota2, freq, media;

  printf("Digite a primeira nota: ");
  scanf(" %f", &nota1);

  printf("Digite a segunda nota: ");
  scanf(" %f", &nota2);

  printf("Digite a frequência: (0 a 100)");
  scanf(" %f", &freq);

  media = nota1 + nota2 / 2;

  if (media >= 7 && freq >= 75) {
    printf("Aprovado");
  } else {
    printf("Reprovado");
  }
  
  return 0;
}