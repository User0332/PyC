#include <stdlib.h>
#include "pyargs.h"
#include "constants.h"

int arglen(PyCArgs)
{
    int i = 0;

    while (args[i] != NULL) i++;

    return i;
}