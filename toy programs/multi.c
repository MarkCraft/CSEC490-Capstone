#include <stdio.h>

int main(){
    int first;
    int second;
    printf("Enter an integer: ");
    scanf("%d", &first);
    printf("Enter another integer: ");
    scanf("%d", &second);
    int multiply = first * second;
    printf("Sum = %d", multiply)

    return 0;
}