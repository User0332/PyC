#include <stdlib.h>
#include "pyobj.h"
#include "builtins.h"
#include "symtab.h"

symtab_node* get_default_table(void)
{
    symtab_node* head = malloc(sizeof (symtab_node));
    *head = (symtab_node) { "print", &PyBuiltins_print, NULL };

    return head;
}

symtab_node* get_default_type_table(void)
{
    return NULL;
}