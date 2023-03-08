    /*

    * C program to read two integers M and N and to swap their values.

    * Use a user-defined function for swapping by accepting the addresses of the two variables.

    * Output the values of M and N before and after swapping.

    */

     

    #include <stdio.h>

     

    /*  Function swap - to interchanges the contents of two items */

     

    void swap(float *ptr1, float *ptr2)

    {

        // Step 4. Create a temporary variable for storing the values

        float temp;

        temp = *ptr1;

        *ptr1 = *ptr2;

        *ptr2 = temp;

    }

     

    int main(void)

    {

        float m, n;

        // Step 1. Take user input

        printf("Enter the value of M (accepted decimal values): ");

        scanf("%f", &m);

        printf("Enter the value of N (accepted decimal values): ");

        scanf("%f", &n);

        // Step 2. Show the values before passing their addresses to the function

        printf("Before swapping : M = %5.2f\tN = %5.2f\n", m, n);

        // Step 3. Pass the addresses to the function

        swap(&m, &n);

        // Step 5. Print the values after the swap function has executed

        printf("After swapping : M  = %5.2f\tN = %5.2f\n", m, n);

    }