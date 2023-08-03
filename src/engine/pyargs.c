#include <stdlib.h>
#include <string.h>
#include "pyargs.h"
#include "constants.h"

int arglen(PyCPositionalArgs)
{
    int i = 0;

    while (args[i] != NULL) i++;

    return i;
}

int in_seen_kw(const char* seenkw[], const char* test, int len)
{
	int i;

	for (i=0; i<len; i++)
	{
		if (strcmp(seenkw[i], test) == 0) return 1;
	}

	return 0;
}