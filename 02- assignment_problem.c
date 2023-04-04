#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<conio.h>
#define infinity 9999
int main()
{
    int n,i,j,cost[15][15],power,dp[15],count,num,unit,mask[5],o,k,c1,c2;
    printf("Enter n\n");
    scanf("%d",&n);
    printf("Enter the cost matrix\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&cost[i][j]);
        }
    }
    power=pow(2,n);
    dp[0]=0;
    for(i=1;i<power;i++)
    {
        dp[i]=infinity;
    }
    for(i=0;i<power;i++)
    {
        count=0;
        k=0;
        num=i;
        while(num>0)
        {
            unit=num%2;
            mask[k]=unit;
            k++;
            if(unit==1)
                count++;
            num=num/2;
        }
        for(j=0;j<n;j++)
        {
            if(mask[j]!=1)
            {
                o=i|(1<<j);
                c1=dp[o];
                c2=dp[i]+cost[count][j];
                if(c2<c1)
                    dp[o]=c2;
            }
        }
    }
    printf("\n%d\n",dp[power-1]);
    return 0;
}
