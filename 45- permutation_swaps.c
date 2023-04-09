#include <stdio.h>
#include<stdlib.h>

/*
    Permutation Swaps:

    You are given an array A having N integers. You can apply the following operation on the array
    any number of times:

    Choose two indices i, j such that 1<=i<j<=N, then decrease 1 from Ai and add to 1 to Aj

    Find if it is possible to convert the array A  into a permutation of length N.

    Input- N=4  arr=3 3 2 2
    Output- Yes

    Input- N=3  arr=2 1 2
    Output- No

*/
int main(){
	//int n,i,j,num,x1,x2,flag,count;
	int arr[300],n,i,j,num,flag;
	long long sum,y;     // Writing output to STDOUT
	scanf("%lu",&n);
	for(i=0;i<n;i++)
	{
		y=0;
		sum=0;
		flag=0;
		scanf("%lu",&num);
		for(j=0;j<num;j++)
		{
			scanf("%lu",&arr[j]);
			sum=sum+arr[j];
			y=y+(j+1);
			if(sum<y)
			{
				flag=1;
			}
		}


		if(sum==y && flag==0)
		{
			printf("YES\n");
		}

		else
		{
			printf("NO\n");
		}


	}
	return 0;

}
