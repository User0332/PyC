#include "constants.h"

#ifndef PyC_ARGS_H

#define PyC_ARGS_H

typedef struct PyC_Object_s PyC_Object;

extern int arglen(PyCPositionalArgs);

extern int in_seen_kw(const char* seenkw[], const char* test, int len);

#endif