#include <stdio.h>

//function prototypes
//int prime(int);
int max_value(int [], int);
int min_value(int [], int);

int max_value(int array[], int elem)
{
	int i = 0;
	int max;

	max = array[i];
	for(i = 0;i < elem;i++)
	{
		if(array[i] > max)
		{
			max = array[i];
		}
	}
	return max;
}

int min_value(int array[], int elem)
{
	int i = 0;
	int min;
	min = array[i];
	for (i = 0; i < elem; i++)
	{
		if(array[i] < min)
		{
			min = array[i];
		}
	}
	return min;
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

	return 1 == 1;
}

int main(){
	int readPrime;

	/*printf("Enter number to find if its prime\n");
	scanf("%d", &readPrime);
	printf("is %d a prime??[1 for Yes, 0 for No] \n",readPrime );
	printf("%d\n", prime(readPrime));*/
	int elements, i = 0, j = 0, k = 0;
	start:
	printf("How many elements do you want to insert in array?\n");
	scanf("%d", &elements);

	if(sizeof(elements) == sizeof(int))
	{
		printf("Please input %d elements\n", elements);
		int numberArray[elements];

		for(i = 0;i < elements;i++)
		{
			scanf("%d", &numberArray[i]);
		}

		printf("\n[");
		for(j = 0; j < elements; j++)
		{
			printf("%d, ", numberArray[j]);
		}
		printf("]\nMax Value ->> %d\n", max_value(numberArray, elements));
		printf("Min value ->> %d\n", min_value(numberArray, elements));
	}
	else
	{
		printf("Please input an integer\n");
		goto start;
	}
	
}
