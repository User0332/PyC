#include "pyobj.h"

#ifndef PyC_STR_H

#define PyC_STR_H

PyC_Type str_type_notptr;
PyC_Object str_notptr;

PyC_Object* pystr_from_c_str(char* str);
void init_PyStr_H(void);

#endif