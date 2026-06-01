#include <stdio.h>
void pattern1(int N)
{
    for(int i = 1; i < N; i++)
    {
        for(int j = 1; j <= N-i+1; j++)
        {
            printf("%d ", j);
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