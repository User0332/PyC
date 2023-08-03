#ifndef PyC_CONSTANTS_H

#define PyC_CONSTANTS_H

#define PyCReturnType struct PyC_Object_s*
#define PyCPositionalArgs PyCReturnType args[]
#define PyCKwargs hashmap* kwargs
#define PyCArgs PyCPositionalArgs, PyCKwargs

#endif