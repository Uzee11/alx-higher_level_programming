#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/* Structure for a singly linked list node */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/**
 * check_cycle - Check if a singly linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list) {
    listint_t *slow_ptr = list, *fast_ptr = list;

    /* Traverse the linked list with two pointers, one moving twice as fast */
    while (slow_ptr && fast_ptr && fast_ptr->next) {
        slow_ptr = slow_ptr->next;         /* Move slow pointer by one step */
        fast_ptr = fast_ptr->next->next;   /* Move fast pointer by two steps */

        /* If there is a cycle, slow and fast pointers will meet at some point */
        if (slow_ptr == fast_ptr)
            return 1;  /* Cycle detected */
    }

    return 0;  /* No cycle detected */
}

/* Example of usage */
int main(void) {
    listint_t *head, *node1, *node2, *node3;

    /* Creating a linked list with a cycle */
    head = malloc(sizeof(listint_t));
    node1 = malloc(sizeof(listint_t));
    node2 = malloc(sizeof(listint_t));
    node3 = malloc(sizeof(listint_t));

    head->n = 1;
    head->next = node1;
    node1->n = 2;
    node1->next = node2;
    node2->n = 3;
    node2->next = node3;
    node3->n = 4;
    node3->next = head;  /* Creating a cycle */

    /* Check if there is a cycle in the linked list */
    if (check_cycle(head))
        printf("There is a cycle in the linked list.\n");
    else
        printf("There is no cycle in the linked list.\n");

    /* Freeing the allocated memory */
    free(head);
    free(node1);
    free(node2);
    free(node3);

    return 0;
}
