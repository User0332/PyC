#include <stdlib.h>
#include "constants.h"
#include "pyobj.h"
#include "symtab.h"
#include "pyargs.h"
#include "str.h"

PyCReturnType str_init(PyCArgs)
{
    int len = arglen(args);

    if (len == 0) {
        return NULL; // raise exc, not enough args
    }

    if (len > 2) {
        return NULL; // raise exc, too many args
    }

    PyC_Object* self = args[0];

    if ((self->type) != &str_type_notptr) {
        return NULL; // raise exc, wrong type for first arg (should be a str instance)
    }


    if (len == 1) {
        self->innervalue = "";
        return NULL/* PyC_None */;
    }

    PyC_Object* val = args[1];

    *self = *(val->type->__str__((PyC_Object* []) {val, NULL}));

    // TODO: RETURN NONETYPE NONE
}

PyCReturnType str_str(PyCArgs)
{
    int len = arglen(args);

    if (len == 0) {
        return NULL; // raise exc, not enough args
    }

    if (len > 1) {
        return NULL; // raise exc, too many args
    }

    PyC_Object* self = args[0];


    if ((self->type) != &str_type_notptr) {
        return NULL; // raise exc, wrong type for first arg (should be a str instance)
    }

    return self; // self is the __str__ represntation (maybe make a copy later?)
}

PyCReturnType str_repr(PyCArgs)
{

} // missing_impl

void init_PyStr_H(void)
{
    str_notptr.symtab = get_default_type_table(&str_type_notptr);
}

void quit_PyStr_H(void)
{
    hashmap_destroy(&str_notptr.symtab);
}

PyC_Object* pystr_from_c_str(char* str)
{
    PyC_Object* string = str_type_notptr.__new__(
        (PyC_Object* []) {&str_notptr, NULL}
    );

    string->innervalue = str;

    return string;
}

PyC_Type str_type_notptr = {
    "str",
    object_new,
    str_init,
    NULL,
    str_repr,
    str_str
};

PyC_Object str_notptr = {
    &type_type_notptr,
    &str_type_notptr,
    NULL
};