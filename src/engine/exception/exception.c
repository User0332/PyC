#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "pyexc.h"
#include "../pyargs.h"

// TODO: Add checks for calloc and realloc fails

static void** handlerbuf;
static size_t bufsize;

PyC_Object* caught = NULL;

void raise(PyC_Object* exc)
{
    raise_cstr(
        exc->type->__str__(
            (PyC_Object* []) { exc, 0 }
        )->innervalue
    );
}

void raise_cstr(char *msg)
{
    int len = arglen(handlerbuf);

    if (len) goto *handlerbuf[len];
    
    fprintf(stderr, "Exception thrown: <stack-trace-not-impled> %s", msg);
    abort();
}

void add_except_handler(void* addr)
{
    int len = arglen(handlerbuf);

    if (len == bufsize-1)
    {
        bufsize+=5;
        handlerbuf = realloc(handlerbuf, bufsize*sizeof (void**));
        memset(handlerbuf+(bufsize-5), 0, 5);
    }

    handlerbuf[len] = addr;
}

void init_PyException_H(size_t handlerbufsize)
{
    handlerbuf = calloc(handlerbufsize, sizeof (void**));
    bufsize = handlerbufsize;
}

void quit_PyException_H(void)
{
    free(handlerbuf);
}