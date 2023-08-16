#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: A pointer to a pointer to the head node of the list.
 *
 * Return: A pointer to the new head node of the reversed list.
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *currentNode = *head;
	listint_t *prevNode = NULL;
	listint_t *nextNode = NULL;

	/*Reverse the list*/
	while (currentNode)
	{
		nextNode = currentNode->next;
		currentNode->next = prevNode;
		prevNode = currentNode;
		currentNode = nextNode;
	}

	return (prevNode);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: A pointer to a pointer to the head node of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	/*Check for empty or single-node list*/
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	listint_t *slow, *fast;

	slow = fast = *head;
	listint_t *tracker = NULL; /*Separates first half and second half*/

	/*Find the middle of the list*/
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		tracker = slow;
		slow = slow->next;
	}

	/* Reverse the second half and compare the lists*/
	listint_t *secondHalf = reverse_list(&slow);

	tracker->next = NULL; /*Disconnect into two halves*/

	/*Compare the two halves*/
	listint_t *firstHalf = *head;

	while (firstHalf != NULL && secondHalf != NULL)
	{
		if (firstHalf->n != secondHalf->n)
		{
			return (0);
		}
		firstHalf = firstHalf->next;
		secondHalf = secondHalf->next;
	}
	return (1);
}

