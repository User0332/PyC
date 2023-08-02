#include "pyobj.h"

#ifndef PyC_STR_H

#define PyC_STR_H

extern PyC_Type str_type_notptr;
extern PyC_Object str_notptr;

extern const char* length_key;
extern size_t key_length;

extern PyC_Object* pystr_from_c_str(char* str, size_t len);
extern void init_PyStr_H(void);
extern void quit_PyStr_H(void);

#endif