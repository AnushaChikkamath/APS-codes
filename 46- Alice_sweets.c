#include<stdio.h>
#include<stdbool.h>
#include<malloc.h>
#include<stdlib.h>


/*
    Alices sweeets:

    Input-  4 2 5
            3 2 1
            5 5 5

    Output- 4
    Explanation- There are 27 possible choices of sweets we can take.
    The minimum equation value is when we take the triplet with indices
    (3, 1, 1) or (3, 1, 2), or (1, 1, 1). In the first triplet, the equation
    value will be abs(A[3] - B[1]) + abs(B[1] - C[1]) + abs(C[1] - A[3]) =
    abs(5 - 3) + abs(3 - 5) + abs(5 - 5) = 4.

*/

// Quick sort in C

#include <stdio.h>

// function to swap elements
void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

// function to find the partition position
int partition(int array[], int low, int high) {

  // select the rightmost element as pivot
  int pivot = array[high];

  // pointer for greater element
  int i = (low - 1);

  // traverse each element of the array
  // compare them with the pivot
  for (int j = low; j < high; j++) {
    if (array[j] <= pivot) {

      // if element smaller than pivot is found
      // swap it with the greater element pointed by i
      i++;

      // swap element at i with element at j
      swap(&array[i], &array[j]);
    }
  }

  // swap the pivot element with the greater element at i
  swap(&array[i + 1], &array[high]);

  // return the partition point
  return (i + 1);
}

void quickSort(int array[], int low, int high) {
  if (low < high) {

    // find the pivot element such that
    // elements smaller than pivot are on left of pivot
    // elements greater than pivot are on right of pivot
    int pi = partition(array, low, high);

    // recursive call on the left of pivot
    quickSort(array, low, pi - 1);

    // recursive call on the right of pivot
    quickSort(array, pi + 1, high);
  }
}

// function to print array elements
void printArray(int array[], int size) {
  for (int i = 0; i < size; ++i) {
    printf("%d  ", array[i]);
  }
  printf("\n");
}

// main function



int mini=999999,x,y,z;
int main()
{
    int n,i,j,k,a[100000],b[100000],c[100000],sum=0;
    scanf("%d",&n);


        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        quickSort(a,0,n-1);
        for(i=0;i<n;i++)
        {
            scanf("%d",&b[i]);
        }
        quickSort(b,0,n-1);
        for(i=0;i<n;i++)
        {
            scanf("%d",&c[i]);
        }
        quickSort(c,0,n-1);

  i=0;
  j=0;
  k=0;
    while(i<n && j<n && k<n)
    {
      sum=abs(b[j]-a[i])+abs(c[k]-b[j])+abs(c[k]-a[i]);
      if(sum<mini)
      mini=sum;
      if(a[i]<=b[j]&& a[i]<=c[k])
      i++;
      else if(b[j]<=c[k])
      j++;
      else
      k++;
    }

    printf("%d\n",mini);
}
