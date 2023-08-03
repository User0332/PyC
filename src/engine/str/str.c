#include <stdlib.h>
#include "../constants.h"
#include "../object/pyobj.h"
#include "../symtab/symtab.h"
#include "../pyargs.h"
#include "str.h"

const char* length_key = "length";
size_t key_length = 0;

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

    return self; // self is the __str__ representation (maybe make a copy later?)
}

PyCReturnType str_repr(PyCArgs)
{

} // missing_impl

PyCReturnType str_add(PyCArgs)
{
    int len = arglen(args);

    if (len < 2) {
        return NULL; // raise exc, not enough args
    }

    if (len > 2) {
        return NULL; // raise exc, too many args
    }

    PyC_Object* self = args[0];
    PyC_Object* other = args[1];

    if ((self->type) != &str_type_notptr) {
        return NULL; // raise exc, wrong type for first arg (should be a str instance)
    }

    if ((other->type) != &str_type_notptr) {
        return NULL; // raise exc, wrong type for second arg (should be str)
    }

    size_t selflen = hashmap_get(&(self->symtab), length_key, key_length);
    size_t otherlen = hashmap_get(&(other->symtab), length_key, key_length);

    size_t newlen = selflen+otherlen;
    char* new = malloc((newlen+1)*sizeof (char*));

    memcpy(new, self->innervalue, selflen);
    memcpy(&new[selflen], other->innervalue, otherlen);

    new[newlen] = '\0';

    PyC_Object* newobj = pystr_from_c_str(new, newlen);

    return newobj;
}

void init_PyStr_H(void)
{
    str_notptr.symtab = get_default_type_table(&str_type_notptr);
	key_length = strlen(length_key);
}

void quit_PyStr_H(void)
{
    hashmap_destroy(&str_notptr.symtab);
}

PyC_Object* pystr_from_c_str(char* str, size_t len)
{

    PyC_Object* string = str_type_notptr.__new__(
        (PyC_Object* []) {&str_notptr, NULL}
    );

    string->innervalue = str;

	hashmap_put(&(string->symtab), length_key, key_length, len); // size 'length' is an internal property, the int does not need to be wrapped by a PyObject

    return string;
}

PyC_Type str_type_notptr = {
    "str",
    object_new,
    str_init,
    NULL,
    str_repr,
    str_str,
    .__add__=str_add
};

PyC_Object str_notptr = {
    &type_type_notptr,
    &str_type_notptr,
    NULL
};