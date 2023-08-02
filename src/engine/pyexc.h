#include "pyobj.h"

#ifndef PyC_PyException_H

#define PyC_PyException_H

extern void raise(PyC_Object* obj);
extern void raise_cstr(char *msg);

extern void add_except_hander(void* addr);

extern void init_PyException_H(size_t handlerbufsize);
extern void quit_PyException_H(void);

#endif