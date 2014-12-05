#include <stdio.h>

//function prototypes
int prime(int);
int maxValue(int [], int);

int maxValue(int array[], int elem)
{
	int i = 0;
	int max;

	for(i = 0;i < elem;i++)
	{
		max = array[i];
		if(array[i] > max)
		{
			array[i] = max;
		}
	}
	return max;
}

int prime(int number)
{
	if(number < 2)
	{
		return 0;
	}
	if(number % 2 == 0)
	{
		return (number == 2);
	} 

	int division = 3;

	while(division*division <= number)
	{
		if(number % division == 0)
		{
			return 0;
		}
		division += 2;
	}

	return 1;
}

int main(){
	/*int readPrime;

	printf("Enter number to find if its prime\n");
	scanf("%d", &readPrime);
	printf("is %d a prime?? \n",readPrime );
	printf("%d\n", prime(readPrime));
	
	int elements, i = 0, j = 0, k = 0;
	printf("How many elemnnts do you want to insert in array?\n");
	scanf("%d", &elements);
	printf("Please input %d elements\n", elements);

	int numberArray[elements];

	for(i = 0;i < elements;i++)
	{
		scanf("%d", &numberArray[i]);
	}*/
	int target = 13195, k = 0;
	int output[100];

	while(k <= target)
	{
		if(prime(k) == 1)
		{
			if(target % k == 0)
			{
				output[k] = k;
			}
		}
		k++;
	}
	int size = (sizeof(output) / sizeof(int));
	printf("Size of array : %d\n",size );
	printf("Largest prime factor of %d is %d\n", target, maxValue(output, size));

	return 0;
}
