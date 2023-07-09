#include "pyobj.h"

#ifndef PyC_PyException_H

#define PyC_PyException_H

void raise(PyC_Object* obj);
void raise_cstr(char *msg);

void add_except_hander(void* addr);

void init_PyException_H(size_t handlerbufsize);
void quit_PyException_H(void);

#endif