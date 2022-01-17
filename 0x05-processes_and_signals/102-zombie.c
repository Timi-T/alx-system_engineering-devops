#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int infinite_while(void);
/**
 * main - Entry point
 *
 * Return: nothing
 */
int main(void)
{
	int i = 0;
	int ret_val;

	ret_val = fork();
	if (ret_val == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
	while (i < 4 && ret_val != 0)
	{
		ret_val = fork();
		if (ret_val == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		i++;
	}
	infinite_while();
}

/**
 * infinite_while - function to display infinitely
 *
 * Return: nothing
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
