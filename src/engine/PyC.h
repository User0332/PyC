#include "../hashmap/hashmap.h"
#include "symtab/symtab.h"
#include "object/pyobj.h"
#include "exception/pyexc.h"
#include "str/str.h"
#include "builtins/builtins.h"
#include "constants.h"

#ifndef PyC_H

#define PyC_H

extern void InitPythonC(void);
extern void QuitPythonC(void);

extern hashmap __main__mod_symtab;

#endif