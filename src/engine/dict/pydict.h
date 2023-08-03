#ifndef PyC_PyDict_H

#define PyC_PyDict_H

#define PyC_PyHash_NUM1 1293046948912312987
#define PyC_PyHash_NUM2 1237198279687292368
#define PyC_PyHash_NUM3 4304983002139844950
#define PyC_PyHash_NUM4 7483629010250012344
#define PyC_PyHash_NUM5 5893992827527391873

#include "../object/pyobj.h"

extern PyC_Type dict_type_notptr;
extern PyC_Object dict_obj_notptr;

// size -> hashmap_num_entries

extern PyC_Object* dict_from_map(hashmap map);

extern unsigned long long pyhash(PyC_Object* obj);
extern void init_PyDict_H(void);
extern void quit_PyDict_H(void);

#endif