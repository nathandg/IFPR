#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {

  float cateto1, cateto2, hipotenusa;
  
  printf("Informe o valor do primeiro cateto: ");
  scanf("%f", &cateto1);

  printf("Informe o valor do segundo cateto: ");
  scanf("%f", &cateto2);
  
  hipotenusa = sqrt(pow(cateto1, 2) + pow(cateto2, 2));
  printf("O valor da hipotenusa é: %.1f\n", hipotenusa);

  return 0;
}