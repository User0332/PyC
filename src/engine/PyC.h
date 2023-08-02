#include "../hashmap/hashmap.h"
#include "symtab.h"
#include "pyobj.h"
#include "pyexc.h"
#include "str.h"
#include "constants.h"
#include "builtins.h"

#ifndef PyC_H

#define PyC_H

extern void InitPythonC(void);
extern void QuitPythonC(void);

extern hashmap __main__mod_symtab;

#endif