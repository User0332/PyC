#include "PyC.h"

void InitPythonC(void)
{
    init_PyObject_H();
    init_PyStr_H();
    init_PyBuiltins_H();
}