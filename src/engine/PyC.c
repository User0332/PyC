#include "PyC.h"

void InitPythonC(void)
{
    init_PyObject_H();
    init_PyStr_H();
    init_PyBuiltins_H();
    init_PyException_H(15);
    __main__mod_symtab = get_default_table();
}

void QuitPythonC(void)
{
    hashmap_destroy(&__main__mod_symtab);
    quit_PyObject_H();
    quit_PyStr_H();
    quit_PyException_H();
}