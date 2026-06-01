#include <stdio.h>
void pattern1(int N)
{
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j <= i; j++)
        {
            printf("* ");
        }
        printf("\n");
    }
}
int main()
{
    int N = 5;
    pattern1(N);
    return 0;
}