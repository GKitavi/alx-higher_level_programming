#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: linked lis to check
 *
 * Return: 1 if the list has a cycle, 0 if none
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = list;
	second = list;
	while (first != NULL && second != NULL)
	{
		first = first->next;
		if (second->next)
			second = second->next->next;

		if (first == second)
			return (1);
	}
	return (0);
}
