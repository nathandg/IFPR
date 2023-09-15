#include <stdio.h>

int main(void) {
  // Learning C
  printf("Hello, World!\n");
  
  // Types
  int a = 1; // 4 bytes
  float b = 1.0; // 4 bytes
  double c = 1.0; // 8 bytes
  long double d = 1.0; // 16 bytes
  char e = 'a'; // 1 byte
  char f[] = "Hello"; // 6 bytes

  // Print real size of types
  printf("Size of int: %d --> %ld\n", a, sizeof(a));
  printf("Size of float: %f --> %ld\n", b, sizeof(b));
  printf("Size of double: %f --> %ld\n", c, sizeof(c));
  printf("Size of long double: %Lf --> %ld\n", d, sizeof(d));
  printf("Size of char: %c --> %ld\n", e, sizeof(e));
  printf("Size of char[]: %s --> %ld\n", f, sizeof(f));

  return 0;
}