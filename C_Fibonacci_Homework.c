#include <math.h>
#include <stdio.h>
int main()
{
   int f1=0, f2=1, age, f3, sum=0;

   printf("Enter your age: ");
   scanf("%d",&age);

   for(int f3=0; f3<age; f3++)
   {
      sum += f1;
      f3 = f1 + f2; //next element
      f1 = f2;
      f2 = f3;
   }

   printf("Sum = %d", sum);

   return 0;

long long convert(int sum)
      {
        long long bin = 0;
        int rem, i = 1, step = 1;
        while (sum != 0) {
                rem = sum % 2;
                printf("Step %d: %d/2, Remainder = %d, Quotient = %d\sum", step++, sum, rem, sum / 2);
                sum /= 2;
                bin += rem * i;
                i *= 10;
        }
        return bin;
}

