#include "pyobj.h"

#ifndef PyC_SYMTAB_H

#define PyC_SYMTAB_H

typedef struct symbol_node {
    char* name;
    PyC_Object* obj;
    struct symbol_node* next;
} symtab_node;

symtab_node* get_default_table(void);
symtab_node* get_default_type_table(void);

#endif