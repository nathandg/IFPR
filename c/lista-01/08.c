#include <stdio.h>
#include <stdlib.h>

int main () {
  int jogador1, jogador2;

  printf("Jogador 1, digite um número: ");
  scanf("%d", &jogador1);

  printf("Jogador 2, digite um número: ");
  scanf("%d", &jogador2);

  if ((jogador1 + jogador2) % 2 == 0) {
    printf("------ PAR GANHOU ------\n");
  } else {
    printf("------ ÍMPAR GANHOU ------\n");
  }

  return 0;
}