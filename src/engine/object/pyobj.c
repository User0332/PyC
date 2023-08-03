#include <stdlib.h>
#include "../pyargs.h"
#include "../PyC.h"
#include "pyobj.h"

PyCReturnType object_new(PyCArgs)
{
    int i;
    int len = arglen(args);

    if (len == 0) {
        return NULL; // raise exc, not enough args
    }

    if ((args[0]->type) != &type_type_notptr) {
        return NULL; // raise exc, wrong type for first arg (should be a class/type)
    }

    PyC_Type* class_type = (PyC_Type*) args[0]->innervalue;

    PyC_Object* obj = malloc(sizeof (PyC_Object)); // TODO: add this to some garbage collecting mechanism

	hashmap* symtab = malloc(sizeof(hashmap));

	hashmap_create(5, symtab);

    *obj = (PyC_Object) {
        class_type,
        NULL,
        *symtab
    };

    PyC_Object* init_args[len+1];

    init_args[0] = obj;

    for (i=1; i<len; i++) init_args[i] = args[i]; // pass on recieved args

    init_args[len] = NULL;

    class_type->__init__(init_args);

    return obj;
}

PyCReturnType object_init(PyCArgs)
{
    int len = arglen(args);

    if (len == 0) {
        return NULL; // raise exc, not enough args
    }

    if (len > 1) {
        return NULL; // raise exc, too many args
    }

    // TODO: RETURN NONETYPE NONE

    return NULL;
}

PyCReturnType type_init(PyCArgs)
{
    /* needs_impl */
}

PyCReturnType type_call(PyCArgs)
{
    int len = arglen(args);

    if (len == 0) {
        return NULL; // raise exc, not enough args
    }

    PyC_Object* class_obj = args[0];

    if (class_obj->type != &type_type_notptr) {
        return NULL; // raise exc, wrong type -- ALSO find out later how to check 4 subclasses of `type`
    }

    PyC_Type* init_type = class_obj->innervalue;

    return init_type->__new__(args);
}

void init_PyObject_H(void)
{

    type_type_notptr = (PyC_Type) {
        "type",
        object_new,
        type_init,
        .__call__=type_call
    };

    type_obj_notptr = (PyC_Object) {
        &type_type_notptr,
        &type_type_notptr,
        get_default_type_table(&type_type_notptr)
    };

    object_type_notptr = (PyC_Type) { // we need to impl all these methods later
        "object",
        object_new,
        object_init
    };

    object_notptr = (PyC_Object) {
        &type_type_notptr,
        &object_type_notptr,
        get_default_type_table(&object_type_notptr)
    };
}

void quit_PyObject_H(void)
{
    hashmap_destroy(&type_obj_notptr.symtab);
    hashmap_destroy(&object_notptr.symtab);
}

PyC_Object object_notptr = { NULL };
PyC_Type object_type_notptr = { NULL };
PyC_Object type_obj_notptr = { NULL };
PyC_Type type_type_notptr = { NULL };