#include <stdio.h>
#include <stdlib.h>

int main() {

  // Even or odd
  int number = 0;

  printf("Enter a number: ");
  scanf("%d", &number);

  if (number % 2 == 0) {
    printf("Even\n");
  } else {
    printf("Odd\n");
  }

}