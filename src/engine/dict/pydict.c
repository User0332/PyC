#include <stdlib.h>
#include "pydict.h"
#include "../object/pyobj.h"
#include "../symtab/symtab.h"
#include "../constants.h"
#include "../pyargs.h"
#include "../../hashmap/hashmap.h"

unsigned int pyhash(PyC_Object* obj)
{
	return 0;
}

PyCReturnType dict_init(PyCArgs)
{
	int len = arglen(args);

	if (len == 0) return NULL; // exc

	if (len > 1) return NULL; // exc

	PyC_Object* self = args[0];

    if ((self->type) != &dict_type_notptr) return NULL; // raise exc, wrong type for self

	const hashmap* map = malloc(sizeof(hashmap));

	hashmap_create(10, map);

	self->innervalue = map;

	return NULL; // return None
}

PyCReturnType dict_getitem(PyCArgs)
{
	int len = arglen(args);

	if (len == 0) return NULL; // exc

	if (len > 2) return NULL; // exc

	PyC_Object* self = args[0];

    if ((self->type) != &dict_type_notptr) return NULL; // raise exc, wrong type for self

	PyC_Object* key = args[1];

	unsigned int hash = pyhash(key);

	PyC_Object* val = hashmap_get(self->innervalue, hash, sizeof(hash));

	if (val == NULL) return NULL; // raise exc, check if NULL is actually what is returned on err

	return val;
}

PyCReturnType dict_setitem(PyCArgs)
{
	int len = arglen(args);

	if (len == 0) return NULL; // exc

	if (len > 3) return NULL; // exc

	PyC_Object* self = args[0];

    if ((self->type) != &dict_type_notptr) return NULL; // raise exc, wrong type for self

	PyC_Object* key = args[1];

	unsigned int hash = pyhash(key);

	PyC_Object* val = args[2];

	if (hashmap_put(self->innervalue, hash, sizeof(hash), val) != 0) return NULL; // if not 0, hashmap_put failed, raise exc

	return NULL; // return None
}

PyC_Type dict_type_notptr = {
	"dict",
	object_new,
	dict_init,
	.__getitem__=dict_getitem,
	.__setitem__=dict_setitem
};