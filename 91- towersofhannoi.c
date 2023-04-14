#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

void towers(int n,char from, char to, char aux)
{
    if(n==1)
    {
        printf("move disc 1 from %c to %c\n",from, to);
        return;
    }
    towers(n-1,from,aux,to);
    printf("move disc %d from c to %c\n",from, to);
    towers(n-1,aux,to,from);
}

int main()
{
    int n=13;
    clock_t start,end;
    int j;
    start=clock();
    towers(n,'a','c','b');
    end=clock();

   double duration;
   duration=(end -start)/ CLOCKS_PER_SEC;
   printf("time taken is %g\n", duration);
    return 0;
}
