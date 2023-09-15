#include <stdio.h>
#include <stdlib.h>

int main () {

  int nota1, nota2, freq;

  printf("Digite a primeira nota: ");
  scanf("%d", &nota1);

  printf("Digite a segunda nota: ");
  scanf("%d", &nota2);

  printf("Digite a frequência: (0 a 100)");
  scanf("%d", &freq);

  media = nota1 + nota2 / 2;

  if (media >= 7 && freq >= 75) {
    printf('Aprovado')
  } else {
    printf('Reprovado')
  }
  
  return 0;
}