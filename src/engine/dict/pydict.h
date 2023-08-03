#ifndef PyC_PyDict_H

#define PyC_PyDict_H

#include "../object/pyobj.h"

extern PyC_Type dict_type_notptr;
extern PyC_Object dict_obj_notptr;

// size -> hashmap_num_entries

extern PyC_Object* dict_from_map(hashmap map);

extern unsigned int pyhash(PyC_Object* obj);
extern void init_PyDict_H(void);
extern void quit_PyDict_H(void);

#endif