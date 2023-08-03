#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "builtins.h"
#include "../object/pyobj.h"
#include "../pyargs.h"
#include "../str/str.h"
#include "../constants.h"

PyCReturnType PyC_print_impl(PyCArgs);
PyC_Type func_obj_notptr;
PyC_Type NotImplementedType; // this is literally not implemented

void init_PyBuiltins_H(void)
{
    PyBuiltins_print = (PyC_Object) {
        &func_obj_notptr,
        PyC_print_impl,
        NULL
    };

    PyBuiltins_object = object_notptr;
}

PyCReturnType func_obj_init(PyCArgs)
{
    int len = arglen(args);

    if (len == 0) {
        return NULL; // raise exc, not enough args
    }

    if (len > 2) {
        return NULL; // raise exc, too many args
    }

    if ((args[0]->type) != &func_obj_notptr) {
        return NULL; // raise exc, wrong type for first arg (should be a func_obj)
    }

    args[0]->innervalue = args[1]->innervalue; // add function over to innervalue
}

PyCReturnType func_obj_call(PyCArgs)
{
    int len = arglen(args);
    int i;

    if (len == 0) {
        return NULL; // raise exc, not enough args
    }

    if (args[0]->type != &func_obj_notptr) {
        return NULL; // raise exc, wrong type -- ALSO find out later how to check 4 subclasses of `type`
    }

    PyC_Object* callargs[len];

    for (i=1; i<len; i++)
    {
        callargs[i-1] = args[i];
    }

    callargs[len-1] = NULL;

    PyCReturnType (*func)(PyCArgs) = args[0]->innervalue;

    return func(callargs, kwargs);
}

int print_iter_kwargs(void** ctx[], struct hashmap_element_s* elem)
{
	char** seenkw = (char**) ctx[0];
	PyC_Object** kwvals = (PyC_Object**) ctx[1];

	int len = arglen(seenkw);

	if (in_seen_kw(seenkw, elem->key, len)) { return 1; } // raise exc

	if (strcmp(elem->key, "sep") == 0) kwvals[0] = elem->data;
	else if (strcmp(elem->key, "end") == 0) kwvals[1] = elem->data;
	else if (strcmp(elem->key, "file") == 0) kwvals[2] = elem->data;
	else if (strcmp(elem->key, "flush") == 0) kwvals[3] = elem->data;
	else
	{
		return 1; // raise exc
	}
	
	seenkw[len] = elem->key;
	
	return 0;
}

PyCReturnType PyC_print_impl(PyCArgs)
{
    int len = arglen(args);
    int i;

	char* seenkw[4] = { NULL, NULL, NULL, NULL };
	PyC_Object* kwvals[4] = { pystr_from_c_str(" ", 1), pystr_from_c_str("\n", 1), NULL, NULL }; // last two are file and flush (using two unimpled types)

	void** context[] = { &seenkw, &kwvals };

	hashmap_iterate_pairs(kwargs, print_iter_kwargs, context);

	char* sep = kwvals[0]->innervalue;
	size_t seplen = hashmap_get(&(kwvals[0]->symtab), length_key, key_length);

	char* end = kwvals[1]->innervalue;
	size_t endlen = hashmap_get(&(kwvals[1]->symtab), length_key, key_length);

	// PyIO file = kwvals[2]

	int flush = 0; // kwvals[3]->innervalue;

    for (i=0; i<len; i++)
    {
        PyC_Object* strobj = args[i]->type->__str__(
            (PyC_Object* []) { args[i], 0 }, NULL
        );

        char* str = strobj->innervalue;
		int length = hashmap_get(&(strobj->symtab), length_key, key_length);

		fwrite(str, sizeof(char), length, stdout);

		if (i != (len-1)) fwrite(sep, sizeof(char), seplen, stdout); // this char will be 'sep'
    }

	fwrite(end, sizeof(char), endlen, stdout);
   
	if (flush) fflush(stdout);

    return NULL; // this should actually be `None` once impl.ed
}

PyC_Type func_obj_notptr = {
    "PyC internal class [builtin func obj]",
    object_new,
    func_obj_init,
    .__call__=func_obj_call
};

PyC_Object PyBuiltins_NotImplemented = {
    &NotImplementedType,
    NULL,
    NULL
};

PyC_Object PyBuiltins_object = { NULL };
PyC_Object PyBuiltins_print = { NULL };