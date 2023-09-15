#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float math_x1 (float a, float b, float delta) {
  return (-b + sqrt(delta)) / (2 * a);
}

float math_x2 (float a, float b, float delta) {
  return (-b - sqrt(delta)) / (2 * a);
}

int main () {

  float a, b, c, delta, x1, x2;

  printf("Digite o valor de A: ");
  scanf("%f", &a);

  printf("Digite o valor de B: ");
  scanf("%f", &b);

  printf("Digite o valor de C: ");
  scanf("%f", &c);

  printf("\n 1 - Calculado Delta\n");
  printf(" Δ = %.0f² - 4 * %.0f * %.0f\n", b, a, c);

  delta = (b * b) - (4 * a * c);
  printf(" Δ = %.0f\n", delta);

  if (delta < 0) {
    printf("\n Essa equação não possui raízes reais\n");
    return 0;
  };

  if (delta == 0) {
    printf("\nHá apenas uma raiz real\n");
    printf("X = %.2f \n", math_x1(a, b, delta));
    return 0;
  }

  printf("\nHá duas raízes reais\n");
  printf("X1 = %.2f \n", math_x1(a, b, delta));
  printf("X2 = %.2f \n", math_x2(a, b, delta));

  return 0;

}