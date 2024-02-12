#include "lists.h"

/**
 * insert_node - inserts a number into a SORTED singly linked list
 * @head: double pointer to linked list; *head points to node to insert
 * @number: number to insert
 *
 * Return: node inserted or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *previous, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	current = *head;

	if (head == NULL || *head == NULL)
		return (new);

	while (current != NULL)
	{
		/* stops at node equal to or greater than number */
		if ((current)->n >= number)
			break;
		previous = current; /* captures node before number */
		current = (current)->next;  /*moves along linked list */
	}

	if (current == *head)  /*if number is first node */
	{
		new->next = (*head);
		*head = new;
	}
	else if ((previous)->next == NULL) /* if number is tail node */
		(previous)->next = new;
	else  /* if number is in the middle */
	{
		new->next = current;
		(previous)->next = new;
	}

	return (new);

}
