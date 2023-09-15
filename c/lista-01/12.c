#include <stdio.h>
#include <stdlib.h>

int main () {

  int cod, qtd;

  struct produto {
    int cod;
    char nome[50];
    float valor;
  };

  struct produto produtos[] = {
    {100, "Cachorro quente", 7.50},
    {101, "Bauru simples", 5.50},
    {103, "X-Burguer", 10.50},
    {104, "X-Salada", 11},
    {105, "X-Bacon", 13.50},
    {106, "Refrigerante", 3.50}
  };

  int qtdProdutos = sizeof(produtos) / sizeof(produtos[0]);

  printf("Digite o código do produto: ");
  scanf("%d", &cod);

  printf("Digite a quantidade comprada: ");
  scanf("%d", &qtd);

  for(int i = 0; i < qtdProdutos; i++) {
    if (produtos[i].cod == cod) {
      printf("Total: R$ %.2f\n", produtos[i].valor * qtd);
      return 0;
    }
  }

  printf("Produto não encontrado. \n");
  return 0;
}