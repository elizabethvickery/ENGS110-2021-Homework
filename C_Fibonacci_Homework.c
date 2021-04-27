#include<stdio.h>
int main()
{
   int a=0, b=1, age, c, sum=0;

   printf("Enter your age: ");
   scanf("%d",&age);

   for(int c=0; c<age; c++)
   {
      sum += a;
      c = a + b; //next element
      a = b;
      b = c;

   }

   printf("Sum = %d", sum);

   return 0;
}
