#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
    char str1[10],str2[10];
    int a[15][15],len1,len2,i,j;
    printf("Enter string1\n");
    scanf("%s",str1);
    printf("Enter string2\n");
    scanf("%s",str2);
    len1=strlen(str1);
    len2=strlen(str2);
    for(i=0;i<len1;i++)
    {
        a[i][0]=0;
    }
    for(i=0;i<len2;i++)
    {
        a[0][i]=0;
    }
    for(i=1;i<=len1;i++)
    {
        for(j=1;j<=len2;j++)
        {
            if(str1[i-1]==str2[j-1])
                a[i][j]=a[i-1][j-1]+1;
            else
            {
                if(a[i-1][j]>a[i][j-1])
                    a[i][j]=a[i-1][j];
                else
                    a[i][j]=a[i][j-1];
            }
        }
    }
    printf("%d",a[len1][len2]);
    return 0;
}
