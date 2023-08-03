#include <stdlib.h>
#include <string.h>
#include "../object/pyobj.h"
#include "../builtins/builtins.h"
#include "../symtab/symtab.h"
#include "../../hashmap/hashmap.h"

hashmap get_default_table(void)
{
    hashmap map;
    int res = 0;

    if (hashmap_create(PyC_DEFAULT_SYMTAB_SIZE, &map) != 0)
    {
        return map; // throw exc, failed to create map
    }

    res &= hashmap_put(&map, "print", strlen("print"), &PyBuiltins_print);

    if (res != 0)
    {
        return map; // throw exc, failed to add something to map
    }

    return map;
}

hashmap get_default_type_table(PyC_Type* type)
{
    hashmap map;
    int res = 0;

    if (hashmap_create(PyC_DEFAULT_SYMTAB_SIZE, &map) != 0)
    {
        return map; // throw exc, failed to create map
    }

    res &= hashmap_put(&map, "__new__", strlen("__new__"), type->__new__);
    res &= hashmap_put(&map, "__init__", strlen("__init__"), type->__init__);
    res &= hashmap_put(&map, "__del__", strlen("__del__"), type->__del__);
    res &= hashmap_put(&map, "__repr__", strlen("__repr__"), type->__repr__);
    res &= hashmap_put(&map, "__str__", strlen("__str__"), type->__str__);
    res &= hashmap_put(&map, "__bytes__", strlen("__bytes__"), type->__bytes__);
    res &= hashmap_put(&map, "__format__", strlen("__format__"), type->__format__);
    res &= hashmap_put(&map, "__lt__", strlen("__lt__"), type->__lt__);
    res &= hashmap_put(&map, "__le__", strlen("__le__"), type->__le__);
    res &= hashmap_put(&map, "__eq__", strlen("__eq__"), type->__eq__);
    res &= hashmap_put(&map, "__ne__", strlen("__ne__"), type->__ne__);
    res &= hashmap_put(&map, "__gt__", strlen("__gt__"), type->__gt__);
    res &= hashmap_put(&map, "__ge__", strlen("__ge__"), type->__ge__);
    res &= hashmap_put(&map, "__hash__", strlen("__hash__"), type->__hash__);
    res &= hashmap_put(&map, "__bool__", strlen("__bool__"), type->__bool__);
    res &= hashmap_put(&map, "__getattr__", strlen("__getattr__"), type->__getattr__);
    res &= hashmap_put(&map, "__getattribute__", strlen("__getattribute__"), type->__getattribute__);
    res &= hashmap_put(&map, "__setattr__", strlen("__setattr__"), type->__setattr__);
    res &= hashmap_put(&map, "__delattr__", strlen("__delattr__"), type->__delattr__);
    res &= hashmap_put(&map, "__dir__", strlen("__dir__"), type->__dir__);
    res &= hashmap_put(&map, "__get__", strlen("__get__"), type->__get__);
    res &= hashmap_put(&map, "__set__", strlen("__set__"), type->__set__);
    res &= hashmap_put(&map, "__delete__", strlen("__delete__"), type->__delete__);
    res &= hashmap_put(&map, "__init_subclass__", strlen("__init_subclass__"), type->__init_subclass__);
    res &= hashmap_put(&map, "__set_name__", strlen("__set_name__"), type->__set_name__);
    res &= hashmap_put(&map, "__instancecheck__", strlen("__instancecheck__"), type->__instancecheck__);
    res &= hashmap_put(&map, "__subclasscheck__", strlen("__subclasscheck__"), type->__subclasscheck__);
    res &= hashmap_put(&map, "__class_getitem__", strlen("__class_getitem__"), type->__class_getitem__);
    res &= hashmap_put(&map, "__call__", strlen("__call__"), type->__call__);
    res &= hashmap_put(&map, "__len__", strlen("__len__"), type->__len__);
    res &= hashmap_put(&map, "__length_hint__", strlen("__length_hint__"), type->__length_hint__);
    res &= hashmap_put(&map, "__getitem__", strlen("__getitem__"), type->__getitem__);
    res &= hashmap_put(&map, "__setitem__", strlen("__setitem__"), type->__setitem__);
    res &= hashmap_put(&map, "__delitem__", strlen("__delitem__"), type->__delitem__);
    res &= hashmap_put(&map, "__missing__", strlen("__missing__"), type->__missing__);
    res &= hashmap_put(&map, "__iter__", strlen("__iter__"), type->__iter__);
    res &= hashmap_put(&map, "__reversed__", strlen("__reversed__"), type->__reversed__);
    res &= hashmap_put(&map, "__contains__", strlen("__contains__"), type->__contains__);
    res &= hashmap_put(&map, "__add__", strlen("__add__"), type->__add__);
    res &= hashmap_put(&map, "__radd__", strlen("__radd__"), type->__radd__);
    res &= hashmap_put(&map, "__iadd__", strlen("__iadd__"), type->__iadd__);
    res &= hashmap_put(&map, "__sub__", strlen("__sub__"), type->__sub__);
    res &= hashmap_put(&map, "__mul__", strlen("__mul__"), type->__mul__);
    res &= hashmap_put(&map, "__matmul__", strlen("__matmul__"), type->__matmul__);
    res &= hashmap_put(&map, "__truediv__", strlen("__truediv__"), type->__truediv__);
    res &= hashmap_put(&map, "__floordiv__", strlen("__floordiv__"), type->__floordiv__);
    res &= hashmap_put(&map, "__mod__", strlen("__mod__"), type->__mod__);
    res &= hashmap_put(&map, "__divmod__", strlen("__divmod__"), type->__divmod__);
    res &= hashmap_put(&map, "__pow__", strlen("__pow__"), type->__pow__);
    res &= hashmap_put(&map, "__lshift__", strlen("__lshift__"), type->__lshift__);
    res &= hashmap_put(&map, "__rshift__", strlen("__rshift__"), type->__rshift__);
    res &= hashmap_put(&map, "__and__", strlen("__and__"), type->__and__);
    res &= hashmap_put(&map, "__xor__", strlen("__xor__"), type->__xor__);
    res &= hashmap_put(&map, "__or__", strlen("__or__"), type->__or__);
    res &= hashmap_put(&map, "__neg__", strlen("__neg__"), type->__neg__);
    res &= hashmap_put(&map, "__pos__", strlen("__pos__"), type->__pos__);
    res &= hashmap_put(&map, "__abs__", strlen("__abs__"), type->__abs__);
    res &= hashmap_put(&map, "__invert__", strlen("__invert__"), type->__invert__);
    res &= hashmap_put(&map, "__dunder_complex__", strlen("__dunder_complex__"), type->__dunder_complex__);
    res &= hashmap_put(&map, "__int__", strlen("__int__"), type->__int__);
    res &= hashmap_put(&map, "__float__", strlen("__float__"), type->__float__);
    res &= hashmap_put(&map, "__index__", strlen("__index__"), type->__index__);
    res &= hashmap_put(&map, "__round__", strlen("__round__"), type->__round__);
    res &= hashmap_put(&map, "__trunc__", strlen("__trunc__"), type->__trunc__);
    res &= hashmap_put(&map, "__floor__", strlen("__floor__"), type->__floor__);
    res &= hashmap_put(&map, "__ceil__", strlen("__ceil__"), type->__ceil__);
    res &= hashmap_put(&map, "__enter__", strlen("__enter__"), type->__enter__);
    res &= hashmap_put(&map, "__exit__", strlen("__exit__"), type->__exit__);
    res &= hashmap_put(&map, "__await__", strlen("__await__"), type->__await__);
    res &= hashmap_put(&map, "__aiter__", strlen("__aiter__"), type->__aiter__);
    res &= hashmap_put(&map, "__anext__", strlen("__anext__"), type->__anext__);
    res &= hashmap_put(&map, "__aenter__", strlen("__aenter__"), type->__aenter__);
    res &= hashmap_put(&map, "__aexit__", strlen("__aexit__"), type->__aexit__);

    if (res != 0)
    {
        return map; // throw exc, failed to add something to map
    }

    return map;
}