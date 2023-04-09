#include <stdio.h>
#include <stdlib.h>

/*
    Adjacent sum greater than k:

    You are given two integers N and K. Find a permutation P of length N
    such that Pi +Pi+1 >=K. If there are multiple permutations find the lexicographically
    smallest one. Print -1 if no such permutation exists.

    Input : 6 5
    Output : 1 4 2 3 5 6

    Input : 4 6
    Output : -1


*/
int main()
{

	int num,i,N,K,j,arr[300],b[300],index=0,iter=0,var1,m1,flag=0,m,f;
	printf("enter n\n");
	scanf("%d", &num);
	for(i=0;i<num;i++)
	{

		scanf("%d%d",&N,&K);

		if(1+N<K)
		{
			printf("-1\n");
			continue;
		}
		iter=0;
		f=K;
		arr[0]=-1;
		  for(m1=0;m1<=K;m1=m1+2)
		  {
			b[m1]=iter+1;
			iter++;

		  }

		  for(m1=1;m1<K;m1=m1+2)
		  {
			b[m1]=f-1;
			f=f-1;
		  }

		 for(j=0;j<K-1;j++)
		 printf("%d ",b[j]);
		 for(j=K;j<=N;j++)
		 printf("%d ",j);
		  printf("\n");
		}
	return 0;

}
