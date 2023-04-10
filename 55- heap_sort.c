#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int a[10]={0,8,6,9,2,5,7,10};
int n=7;

void heapification(int a[],int n)
{
    int i,j=0,heap,v=0,k=0;
    for(i=(n/2);i>=1;i--)
    {
        k=i;
        v=a[k];
        heap=0;
        while(heap!=1 && 2*k<=n)
        {
            j=2*k;
            if(j<n)
            {
                if(a[j+1]>a[j])
                {
                    j=j+1;
                }
            }
            if(a[j]<v)
            {
                heap=1;
            }
            else
            {
                a[k]=a[j];
                k=j;
                a[k]=v;
            }
        }
    }
}

int main()
{
    int e=n;
    heapification(a,n);
    int d,m=0;
    for(d=1;d<=e;d++)
    {
        m=a[1];
        a[1]=a[n];
        printf("%d ",m);
        n=n-1;
        heapification(a,n);
    }
}
