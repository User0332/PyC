#include "pyobj.h"
#include "str.h"
#include "NoneType.h"

#ifndef PYASM_BUILTINS_H

#define PYASM_BUILTINS_H

PyC_Object PyBuiltins_object;

PyC_Object PyBuiltins_print;
PyC_Object PyBuiltins_None;
PyC_Object PyBuiltins_NotImplemented;

void init_PyBuiltins_H(void);


#endif