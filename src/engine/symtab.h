#include "pyobj.h"
#include "../hashmap/hashmap.h"

#ifndef PyC_SYMTAB_H

#define PyC_SYMTAB_H

#define PyC_DEFAULT_SYMTAB_SIZE 2 /* <- change this later */
#define PyC_DEFAULT_TYPE_SYMTAB_SIZE 73

typedef struct hashmap_s hashmap;

hashmap get_default_table(void);
hashmap get_default_type_table(PyC_Type* type);

#endif