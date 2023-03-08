#include<stdio.h>
#include<stdlib.h>

void add(int one [][3], int two [][3], int sum[][3]){
    for (int i = 0; i<3; i++)
        for(int j = 0; j<3; j++)
            sum[i][j] = one[i][j] + two[i][j];
}

void matPrinter(int mat [][3]){
    for (int i = 0; i<3; i++)
        for(int j = 0; j<3; j++)
            printf("%d\t",mat[i][j]);

    printf("\n");
}

int main() {
    int a [][3] = {{1,4,7}, {4,5,6}, {0,0,0}};
    int b [][3] = {{7,7,7}, {9,3,6}, {9,0,1}};
    int c [3][3];
    add(a,b,c);
    printf("SUM");
    printf("------------------");
    matPrinter(c);
    return 0;
}