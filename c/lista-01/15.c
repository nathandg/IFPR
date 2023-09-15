#include <stdio.h>
#include <stdlib.h>

#define NOT_FOUND_MESSAGE "Animal não identificado ! \n"

int getResponse () {
  char resposta;
  scanf(" %c", &resposta);

  if (resposta == '1'){
    printf("respondeu Sim\n");
    return 1;
  }
  
  if (resposta == '0'){
    printf("respondeu Não\n");
    return 0;
  }

  printf("Resposta inválida! digite (0 ou 1) \n");
  return getResponse();
}

int main () {
  printf("Pense em um animal: \n");
  printf("Esse animal é mamífero? (0 - não; 1 - sim) \n");

  if (getResponse()) {
    printf("Esse animal é quadrúpede? (0 - não; 1 - sim) \n");
    if (getResponse()){

      printf("Esse animal é carnívoro? (0 - não; 1 - sim) \n");
      if (getResponse()){
        printf("O animal pensado é o leão! \n");
        return 0;
      }

      printf("Esse animal é herbívoro? (0 - não; 1 - sim) \n");
      if (getResponse()){
        printf("O animal pensado é o cavalo! \n");
        return 0;
      }

      printf(NOT_FOUND_MESSAGE);
      return 0;
    }

    printf("Esse animal é bípede? (0 - não; 1 - sim) \n");
    if (getResponse()){

      printf("Esse animal é onívoro? (0 - não; 1 - sim) \n");
      if (getResponse()) {
        printf("O animal pensado é o homem! \n");
        return 0;
      } 
      
      printf("Esse animal é frutífero? (0 - não; 1 - sim) \n");
      if (getResponse()) {
        printf("O animal pensado é o macaco! \n");
        return 0;
      }

      printf(NOT_FOUND_MESSAGE);
      return 0;
    }

    printf("Esse animal é voador ?");
    if(getResponse()) {
      printf("O Animal é Morcego \n");
      return 0;
    }

    printf("Esse animal é aquático ?");
    if(getResponse()) {
      printf("O Animal é Baleia \n");
      return 0;
    }

    printf(NOT_FOUND_MESSAGE);
    return 0;
  }

  printf("Esse animal é uma ave? (0 - não; 1 - sim) \n");
  if (getResponse()) {
    printf("Esse animal é não-voador? (0 - não; 1 - sim) \n");
    if (getResponse()){

      printf("Esse animal é tropical? (0 - não; 1 - sim) \n");
      if (getResponse()) {
        printf("O animal pensado é o avestruz! \n");
        return 0;
      }

      printf("Esse animal é polar? (0 - não; 1 - sim) \n");
      if (getResponse()) {
        printf("O animal pensado é o pinguim! \n");
        return 0;
      }

      printf(NOT_FOUND_MESSAGE);
      return 0;
    }

    printf("Esse animal é nadador? (0 - não; 1 - sim) \n");
    if (getResponse()){ 
      printf("O animal pensado é o pato! \n");
      return 0;
    }

    printf("Esse animal é de rapina? (0 - não; 1 - sim) \n");
    if (getResponse()){ 
      printf("O animal pensado é a águia! \n");
      return 0;
    }

    printf(NOT_FOUND_MESSAGE);
    return 0;
  }

  printf("Esse animal é um réptil? (0 - não; 1 - sim) \n");
  if (getResponse()){
    printf("Esse animal é com casco? (0 - não; 1 - sim) \n");
    if (getResponse()) {
      printf("O animal pensado é a tartaruga! \n");
      return 0;
    }

    printf("Esse animal é carnívoro? (0 - não; 1 - sim) \n");
    if (getResponse()) {
      printf("O animal pensado é o crocodilo! \n");
      return 0;
    }

    printf("Esse animal é sem patas? (0 - não; 1 - sim) \n");
    if (getResponse()) {
      printf("O animal pensado é a cobra! \n");
      return 0;
    }

    printf(NOT_FOUND_MESSAGE);
    return 0;
  }

  printf(NOT_FOUND_MESSAGE);
  return 0;
}