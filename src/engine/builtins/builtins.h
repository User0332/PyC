#include "../object/pyobj.h"
#include "../str/str.h"
#include "../None/NoneType.h"

#ifndef PYASM_BUILTINS_H

#define PYASM_BUILTINS_H

extern PyC_Object PyBuiltins_object;

extern PyC_Object PyBuiltins_print;
extern PyC_Object PyBuiltins_None;
extern PyC_Object PyBuiltins_NotImplemented;

void init_PyBuiltins_H(void);

#endif