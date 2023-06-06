#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list to perform check on
 * Return: 0 if no cycle; 1 if cycle present
 */

int check_cycle(listint_t *list)
{
	listint_t *past = list;
	listint_t *future = list;

	if (!list)
		return (0);

	while (past && future && future->next)
	{
		past = past->next;
		future = future->next->next;
		if (past == future)
			return (1);
	}
	return (0);
}
