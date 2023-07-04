#include <stdio.h>
#include "engine/PyC.h"

int main(void)
{
    InitPythonC();

    // this is full of memory leaks currently
    PyC_Object* mystr = pystr_from_c_str("Hello, World!");


    PyBuiltins_print.type->__call__(
        (PyC_Object* []) { &PyBuiltins_print, mystr, 0 }
    );

    return 0;
}