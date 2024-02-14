#include "library.h"

#include <stdio.h>
#include <stdlib.h>

/*
Arrays:

    arrayInsert
    arrayDelete
    arrayTraversal
    arraySearch
    arraySort
    arrayMerge
    arraySplit
    arrayCopy
    arrayReverse
    Linked Lists:

Singly Linked List (SLL):

    sllAppend
    sllPrepend
    sllRemove
    sllDelete
    sllTraverse

Doubly Linked List (DLL):

    dllAppend
    dllPrepend
    dllRemove
    dllDelete
    dllTraverse

For Circular Singly Linked Lists (CSLL):

    csllAppend
    csllPrepend
    csllRemove
    csllDelete
    csllTraverse

For Circular Doubly Linked Lists (CDLL):

    cdllAppend
    cdllPrepend
    cdllRemove
    cdllDelete
    cdllTraverse

Stacks:

    stackPush
    stackPop
    stackPeek
    stackTraversal
    isStackEmpty
    isStackFull

Queues:

    queueEnqueue
    queueDequeue
    queueFront
    queueRear
    queueTraversal
    isQueueEmpty
    isQueueFull

Trees:

    binaryTreeNodeCreate
    binaryTreeInsert
    binaryTreeDelete
    binaryTreeTraverse
    bstInsert
    bstDelete
    bstSearch
    bstMinValue
    bstMaxValue
    avlRotateLeft
    avlRotateRight
    avlRotateLeftRight
    avlRotateRightLeft

Graphs:

    graphNodeCreate
    graphEdgeInsert
    graphEdgeDelete
    graphTraversal
    graphPathFind
    isGraphCyclic
    primMST
    kruskalMST
    dijkstraShortestPath
    bellmanFordShortestPath

Hash Tables:

    hashTableInit
    hashFunction
    hashTableInsert
    hashTableDelete
    hashTableSearch
    handleCollision
    hashTableResize
    hashTableTraversal

Heaps:

    heapInit
    heapify
    heapInsert
    heapDelete
    heapExtractMax
    heapSort

Tries:

    trieNodeCreate
    trieInsert
    trieDelete
    trieSearch
    triePrefixSearch

Priority Queues:

    priorityQueueInit
    priorityQueueInsert
    priorityQueueDelete
    priorityQueuePeek
    priorityQueueTraversal

*/


/* Simply linked list */

sll* sllAppend(sll** head, float data){
    sll* temp = (sll*)malloc(sizeof(sll));
    if ( temp == NULL ){
        printf("\nError, memory couldn't be allocated for <sll> temp variables");
        return NULL;
    }

    temp->data = data;
    temp->next = NULL;

    if ( *head == NULL) {
        *head = temp;
        return temp;
    }
    else {
        sll* ptr = *head;
        while(ptr->next != NULL){
            ptr = ptr->next;
        }
        ptr->next = temp;
        return temp;
    }
}

sll* sllPrepend(sll** head, float data){
    sll* temp = (sll*)malloc(sizeof(sll));
    if ( temp == NULL) {
        printf("\nMemory allocation for <sll> temp failed!");
        return NULL;
    }

    temp->next = NULL;
    temp->data = data;

    if ( *head == NULL) {
        *head = temp;
        return temp;
    }
    else {
        temp->next = *head;
        *head = temp;
        return temp;
    }

}

void sllInsert(sll** head, float data, int range){
    int counter = 0;
    sll* temp = (sll*)malloc(sizeof(sll));
    sll* ptr = *head;

    temp->next = NULL;
    temp->data = data;
    if ( temp == NULL ) {
        printf("\nMemory allocation for <sll> temp failed!");
        return;
    }

    while (ptr != NULL){
        counter++;
        ptr = ptr->next;
    }

    if ( range < 0 || range > counter ) {
        printf("\nInvalid range!");
        return;
    }
    else {
        if ( range == 0 ){
            temp->next = *head;
            *head = temp;
            return;
        }
        ptr = *head;
        for ( int i = 0 ; i < range-2 ; i++){
            ptr = ptr->next;
        }
        temp->next = ptr->next;
        ptr->next = temp;
    }
}

int** sllGetAddresses(sll* head) {
    if (head == NULL) {
        printf("\nNull list!");
        return NULL;
    }

    // Count the number of nodes
    int counter = 0;
    sll* ptr = head;
    
    //counting the number of node in the list
    while (ptr != NULL) {
        counter++;
        ptr = ptr->next;
    }

    // Allocate memory for array of pointers
    int** list = malloc(counter * sizeof(int*));
    if (list == NULL) {
        printf("Memory allocation failed");
        return NULL;
    }

    // Populate the array with addresses of nodes
    ptr = head;
    counter = 0;
    while (ptr != NULL) {
        list[counter] = (int*)ptr;  // Store the address of the current node
        ptr = ptr->next; // Move to the next node
        counter++;
    }

    return list;
}

void sllDeleteNode(sll **head, int range) {
    if ( *head == NULL){
        printf("\nNUll list!");
        return;
    }

    int counter = 0, i = 0;
    sll *ptr = *head;

    while( ptr != NULL ){
        counter++;
        ptr = ptr->next;
    }

    if ( range <= 0 || range > counter){
        printf("\n\nRange is not valid.");
        return;
    }

    ptr = *head;
    if ( range == 1 ){
        *head = (*head)->next;
        free(ptr);
        return;
    }

    while ( i < range - 2){
        ptr = ptr->next;
        i++;
    }

//    printf("\n\naddress : %p , value : %f", ptr, ptr->data);

    sll *temp = ptr->next;
    if ( range == counter){
        ptr->next = NULL;
    }
    else {
        ptr->next = ptr->next->next;
    }
    free(temp);
}

sll* sllModify(sll **head, int range, float data) {

    if ( *head == NULL ) {
        printf("\nNULL list!");
        return NULL;
    }

    sll* ptr = *head;
    int counter = 0, i = 0;

    while (ptr!=NULL) {
        ptr = ptr->next;
        counter++;
    }

    if ( range <= 0 || range > counter ) {
        printf("\nInvalid range!");
        return NULL;
    }

    ptr = *head;

    while ( i < range - 1) {
        ptr = ptr->next;
        i++;
    }

    ptr->data = data;
    return ptr;
}

sll* sllReverse(sll **head) {
    if ( *head == NULL ) {
        printf("\nNULL list");
        return NULL;
    }
    if ( (*head)->next == NULL){
        return *head;
    }

    sll *prev = NULL;
    sll *current = *head;
    sll *next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;

    return *head;
}

void sllTraverse(sll** head) {
    if ( *head == NULL){
        printf("\n\tNULL LIST!");
        return;
    }

    sll *ptr = *head;
    while( ptr != NULL ) {
        printf("\nAddress : %p |\t| data : %f", ptr, ptr->data);
        ptr = ptr->next;
    }
    return;
}

void sllFreeMemory(sll* head) {
    if (head == NULL) {
        return;
    }
    sll* ptr = head;
    sll* ptr2 = NULL;
    while (ptr != NULL) {
        ptr2 = ptr;
        ptr = ptr->next;
        free(ptr2);
    }
}



/*Doubly linked listed*/

dll* dllPrepend(dll** head,dll** tail, int data){
	dll* temp = (dll*)malloc(sizeof(dll));
	
    if ( temp == NULL) {
        printf("\nMemory allocation failed for <dll*>temp in function dllPrepend");
        return NULL; }

	temp->data= data;
	temp->next = NULL;
	temp->prev = NULL;

	if ( *head == NULL) {
        *head = temp; 
        *tail = temp;
    }
	else
	{
		(*head)->prev = temp;
		temp->next = *head;
		*head = temp;
	}

    return temp;
}

dll* dllAppend(dll** head,dll** tail, int valeur){
	dll* temp = (dll*)malloc(sizeof(dll));
	
    if ( temp == NULL){	
        printf("\nMemory allocation failed for dll* temp in funciton dllApend!");
        return NULL;
    }
	
    temp->data = valeur;
	temp->next = NULL;

	if ( *head == NULL)
	{
		temp->prev = NULL;
		*head = temp;
		*tail = temp;
	}
	else
	{
		(*tail)->next = temp;
		temp->prev = *tail;
		*tail = temp;
	}
	
    
    return temp;
}

void dllPrintList(dll* head){
	if ( head == NULL ) {
        printf("\n\tNULL LIST!");
    return;
    }

	dll* ptr = head;
	while ( ptr != NULL )
	{
		printf("\nAddress %x <=> %p \t Value :%d",ptr ,ptr ,ptr->data);
		ptr = ptr->next;
	}

}

// Print the linked list in reverse.
void dllPrintListReverse(dll* tail){
	if ( tail == NULL ) {
        printf("\n\tNULL LIST!");
        return;
    }

	dll* ptr = tail;
	while ( ptr != NULL)
	{
		printf("\nAddress %x <=> %p \t Value :%d",ptr ,ptr ,ptr->data);
		ptr = ptr->prev;
	}
}

dll* dllFind(dll** head_dbl, dll** tail, int valeur){
	if ( *head_dbl == NULL ) {
        printf("\n\n\t\tNULL LIST!");
        return NULL;
    }

	dll* ptr = *head_dbl;
	dll* ptr2 = *tail;

    // traversing the linked list in two opposite direction to reduce search time
	while ( ptr != NULL && ptr2 != NULL)
	{
		if ( ptr->data == valeur) { return ptr; }
		if ( ptr2->data == valeur) { return ptr2; }
		ptr = ptr->next;
		ptr2 = ptr2->prev;
	}

	return NULL;
}

void dllFreeMemory(dll** head){
	dll* ptr = *head;
    dll* ptr2 = NULL;
	while ( ptr != NULL ){
        ptr2 = ptr;
		ptr = ptr->next;
		free(ptr2);
	}
}


/*Stack

A Stack data structure can be represented using both Simple and double linked list, the appropriate choice depends on the problem.

A Stack data structure respect one fundamental concept, which is that the first element insert into the list is the last item to leave/read/treated, it's FILO ; First In Last Out 

In this example, we'll be using a simple linked list.

*/

sll* StackPush(sll** head, float data){
    sll* temp = (sll*)malloc(sizeof(sll));

    if ( temp == NULL ) {
        printf("\nMemory allocation for <sll>temp in StackPush() failed!");
        return NULL;
    }

    temp->data = data;
    temp->next = NULL;


    if ( *head == NULL ) {
        *head = temp;
    }
    else {
        temp->next = *head;
        *head = temp;
    }

    return temp;
}


//function type may varie depending on the problem
sll* StackPop(sll** head) {
    
    if ( *head == NULL ) {
        printf("\nNULL LIST!");
        return NULL;
    }

    sll* temp = (sll*)malloc(sizeof(sll));
    if ( temp == NULL ) {
        printf("\nMemory allocation failed for <sll*> temp in Stackpop()!");
        return NULL;
    }

    temp->data = (*head)->data;
    temp->next = (*head)->next;

    sll* ptr = *head;
    if ( (*head)->next == NULL ) {
            free(ptr);
            *head = NULL;
    }
    else {
        *head = (*head)->next;
        free(ptr);
    }
    
    return temp;
}


 ///////////////////////////////// QUEUE /////////////////////////////////

/**
 * Function to add new node to the queue. A queue is a data structure that respect the principal of FIFO ( First In First Out) 
 * The implemantation in this library uses a simple linked list to link the nodes together
 *@return : <sll*> temp ; the new node created
*/
sll* QueuePush(sll** head, float data) {
    sll* temp = (sll*)malloc(sizeof(sll));

    if ( temp == NULL ) {
        printf("\nMemory allocation for <temp> in QueuePop() failed!");
        return NULL;
    }

    temp->data = data;
    temp->next = NULL;

    if ( *head == NULL ) {
        *head = temp;
    }
    else {
        sll* tail = *head;
        
        while ( tail->next != NULL ) {
            tail = tail->next;
        }

        tail->next = temp;
    }
    return temp;
}

/**
 * Function to pop/retrieve/remove the first node, the node it removed from the list. 
 * @return : <sll*>temp : the first node in the list
*/
sll* QueuePop(sll** head) {
    
    if ( *head == NULL ) {
        printf("\nNULL list!");
        return NULL;
    }
    
    sll* temp = (sll*)malloc(sizeof(sll));
    
    if ( temp == NULL ) {
        printf("\nMemory allocatiol failure in function QueuePop()!");
        return NULL;
    }
    
    if ( (*head)->next != NULL ){
        sll* ptr = *head;
        temp->data = (*head)->data;
        temp->next = (*head)->next;
        *head = (*head)->next;
        free(ptr);
    }

    return temp;
}


