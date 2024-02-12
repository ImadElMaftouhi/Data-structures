#include <stdio.h>
#include <stdlib.h>
#include "library.h"


int main() {
    //initialising our list's head
    sll* head = NULL;

    //adding node to our linked list
    for ( int i = 0 ; i  <10 ; i++) {
        sllAppend(&head, i * 123);
    }   


    //getting the addresses of nodes in the list
    int** list = sllGetAddresses(head);

    //printing the addressese 
    for ( int i = 0 ; i < 10 ; i++) {
        printf("\nAddress : %x \t Value : %", list[i]);
    }

    return 0;
}