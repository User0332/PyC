#include <string.h>
#include "engine/PyC.h"

int main()
{
	InitPythonC();

	PyC_Object* sv0;
	
	PyC_Object* working_expr = NULL;
	PyC_Object* pushed_expr = NULL; // fix, this, may be bad design (follow same pattern as used in UntypedScript, use __asm__ if needed)

	sv0 = hashmap_get(&__main__mod_symtab, "print", strlen("print"));
	working_expr = sv0->type->__call__((PyC_Object* []) { sv0, pystr_from_c_str("Hello, World!"), 0 });
	
	QuitPythonC();
	return 0;
}