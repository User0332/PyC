#include "constants.h"
#include "../hashmap/hashmap.h"

#ifndef PYOBJ_H

#define PYOBJ_H

typedef struct hashmap_s hashmap;

typedef struct PyC_Type_s {
    char* name;
    PyCReturnType (*__new__)(PyCArgs);
    PyCReturnType (*__init__)(PyCArgs);
    PyCReturnType (*__del__)(PyCArgs);
    PyCReturnType (*__repr__)(PyCArgs);
    PyCReturnType (*__str__)(PyCArgs);
    PyCReturnType (*__bytes__)(PyCArgs);
    PyCReturnType (*__format__)(PyCArgs);
    PyCReturnType (*__lt__)(PyCArgs);
    PyCReturnType (*__le__)(PyCArgs);
    PyCReturnType (*__eq__)(PyCArgs);
    PyCReturnType (*__ne__)(PyCArgs);
    PyCReturnType (*__gt__)(PyCArgs);
    PyCReturnType (*__ge__)(PyCArgs);
    PyCReturnType (*__hash__)(PyCArgs);
    PyCReturnType (*__bool__)(PyCArgs);
    PyCReturnType (*__getattr__)(PyCArgs);
    PyCReturnType (*__getattribute__)(PyCArgs);
    PyCReturnType (*__setattr__)(PyCArgs);
    PyCReturnType (*__delattr__)(PyCArgs);
    PyCReturnType (*__dir__)(PyCArgs);
    PyCReturnType (*__get__)(PyCArgs);
    PyCReturnType (*__set__)(PyCArgs);
    PyCReturnType (*__delete__)(PyCArgs);
    PyCReturnType (*__init_subclass__)(PyCArgs);
    PyCReturnType (*__set_name__)(PyCArgs);
    PyCReturnType (*__instancecheck__)(PyCArgs);
    PyCReturnType (*__subclasscheck__)(PyCArgs);
    PyCReturnType (*__class_getitem__)(PyCArgs);
    PyCReturnType (*__call__)(PyCArgs);
    PyCReturnType (*__len__)(PyCArgs);
    PyCReturnType (*__length_hint__)(PyCArgs);
    PyCReturnType (*__getitem__)(PyCArgs);
    PyCReturnType (*__setitem__)(PyCArgs);
    PyCReturnType (*__delitem__)(PyCArgs);
    PyCReturnType (*__missing__)(PyCArgs);
    PyCReturnType (*__iter__)(PyCArgs);
    PyCReturnType (*__reversed__)(PyCArgs);
    PyCReturnType (*__contains__)(PyCArgs);
    PyCReturnType (*__add__)(PyCArgs);
    PyCReturnType (*__radd__)(PyCArgs);
    PyCReturnType (*__iadd__)(PyCArgs);
    PyCReturnType (*__sub__)(PyCArgs);
    PyCReturnType (*__mul__)(PyCArgs);
    PyCReturnType (*__matmul__)(PyCArgs);
    PyCReturnType (*__truediv__)(PyCArgs);
    PyCReturnType (*__floordiv__)(PyCArgs);
    PyCReturnType (*__mod__)(PyCArgs);
    PyCReturnType (*__divmod__)(PyCArgs);
    PyCReturnType (*__pow__)(PyCArgs);
    PyCReturnType (*__lshift__)(PyCArgs);
    PyCReturnType (*__rshift__)(PyCArgs);
    PyCReturnType (*__and__)(PyCArgs);
    PyCReturnType (*__xor__)(PyCArgs);
    PyCReturnType (*__or__)(PyCArgs);
    PyCReturnType (*__neg__)(PyCArgs);
    PyCReturnType (*__pos__)(PyCArgs);
    PyCReturnType (*__abs__)(PyCArgs);
    PyCReturnType (*__invert__)(PyCArgs);
    PyCReturnType (*__dunder_complex__)(PyCArgs);
    PyCReturnType (*__int__)(PyCArgs);
    PyCReturnType (*__float__)(PyCArgs);
    PyCReturnType (*__index__)(PyCArgs);
    PyCReturnType (*__round__)(PyCArgs);
    PyCReturnType (*__trunc__)(PyCArgs);
    PyCReturnType (*__floor__)(PyCArgs);
    PyCReturnType (*__ceil__)(PyCArgs);
    PyCReturnType (*__enter__)(PyCArgs);
    PyCReturnType (*__exit__)(PyCArgs);
    PyCReturnType (*__await__)(PyCArgs);
    PyCReturnType (*__aiter__)(PyCArgs);
    PyCReturnType (*__anext__)(PyCArgs);
    PyCReturnType (*__aenter__)(PyCArgs);
    PyCReturnType (*__aexit__)(PyCArgs);
} PyC_Type;

typedef struct PyC_Object_s {
    PyC_Type* type;
    void* innervalue;
    hashmap symtab;
} PyC_Object;

PyC_Object object_notptr;
PyC_Type object_type_notptr;

PyC_Object type_obj_notptr;
PyC_Type type_type_notptr;


void init_PyObject_H(void);
void quit_PyObject_H(void);
PyCReturnType object_init(PyCArgs);
PyCReturnType object_new(PyCArgs);

#endif