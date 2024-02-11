    #include "library.h"

    #include <stdio.h>
    #include <stdlib.h>

/*
sllAppendNode (for a singly linked list)
sllInsertNode
sllRemoveNode
sllDeleteNode
sllTraverseList
dllAppendNode (for a doubly linked list)
dllInsertNode
dllRemoveNode
dllDeleteNode
dllTraverseList
 */


/**
 * Struct definition for a simple linked list (: sll)
 * data variable can be changed to whatever needed
 */
typedef struct sll{
    float data;
    struct sll *next;
}sll;



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

int* sllGetAddresses(sll* head) {
    if (head == NULL) {
        printf("\nNull list!");
        return NULL;
    }

    // Count the number of nodes
    int counter = 0;
    sll* ptr = head;
    while (ptr != NULL) {
        counter++;
        ptr = ptr->next;
    }

    // Allocate memory for array of pointers
    int* list = (int*)malloc(counter * sizeof(int));
    if (list == NULL) {
        printf("Memory allocation failed");
        return NULL;
    }

    // Populate the array with addresses of nodes
    ptr = head;
    counter = 0;
    while (ptr != NULL) {
        list[counter] = (int)ptr; // Store the address of the current node
        ptr = ptr->next; // Move to the next node
        counter++;
    }

    return list;
}


void sllDeleteNode(sll **head, int range){
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

// testing
int main (){

    sll *head = NULL, *ptr = NULL;
    int i;

    for ( i = 1 ; i <= 10 ; i++){
        sllAppend(&head, (float)i );
    }

    ptr = head;
    while (ptr != NULL){
        printf("\naddress : %p , value : %f", ptr, ptr->data);
        ptr = ptr->next;
    }



    return 0;
}