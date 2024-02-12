#ifndef DATA_STRUCTURES_LIBRARY_H
#define DATA_STRUCTURES_LIBRARY_H

/**
 * Struct definition for a simple linked list (: sll)
 * data variable can be changed to whatever needed
 */
typedef struct sll{
    float data;
    struct sll *next;
}sll;

sll* sllAppend(sll** head, float data);

sll* sllPrepend(sll** head, float data);

void sllInsert(sll** head, float data, int range);

int** sllGetAddresses(sll* head);

void sllDeleteNode(sll **head, int range);

sll* sllModify(sll **head, int range, float data);

sll* sllReverse(sll **head);

void sllTraverse(sll **head);

#endif //DATA_STRUCTURES_LIBRARY_H
