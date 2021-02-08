#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
/**
 * infinite_while - Infinite loop
 *
 *
 * Return: always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Function that creates 5 zombies process
 *
 *
 * Return: number of nodes in the list.
 */
int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 1; i <= 5; i++)
	{
		/* Fork that gets process id*/
		child_pid = fork();
		/*Parent process*/
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
		}
		/* Child process*/
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
