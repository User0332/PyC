#include <stdlib.h>
#include <stdio.h>
#include "builtins.h"
#include "pyobj.h"
#include "pyargs.h"
#include "str.h"
#include "constants.h"

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

    return func(callargs);
}

PyCReturnType PyC_print_impl(PyCArgs) // don't worry about kwargs for now
{
    int len = arglen(args);
    int i;

    for (i=0; i<len; i++)
    {
        PyC_Object* strobj = args[i]->type->__str__(
            (PyC_Object* []) { args[i], 0 }
        );

        char* str = strobj->innervalue;

        fputs(str, stdout);
    }

    putc('\n', stdout); // behavior may be modified by kwargs later
    fflush(stdout);


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