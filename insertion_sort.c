#include<stdio.h>
#include<stdlib.h>


int insertion_sort(int n, int a[20])
{
    int i,temp,j,v;
    for(i=1;i<=n-1;i++)
    {
        v=a[i];
        j=i-1;
        while(j>=0 && a[j]>v)
        {
            a[j+1]=a[j];
            j=j-1;
        }
         a[j+1]=v;

    }
}

int display(int n, int a[20])
{
    int i;
    printf("numbers in ascending order:\n");
    for(i=0;i<n;i++)
    {
        printf("%d\t",a[i]);
    }
}

int main()
{
    int n=5;
    int a[20]={12,5,9,23,4};
    insertion_sort(n,a);
    display(n,a);
    return 0;
}
