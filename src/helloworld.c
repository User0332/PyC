#include <string.h>
#include "engine/PyC.h"

int main()
{
	InitPythonC();

	PyC_Object* sv0;
	PyC_Object* sv1[4];
	hashmap hmap0;
	
	PyC_Object* working_expr = NULL;
	PyC_Object* pushed_expr = NULL; // fix, this, may be bad design (follow same pattern as used in UntypedScript, use __asm__ if needed)

	hashmap_create(5, &hmap0);
	sv0 = hashmap_get(&__main__mod_symtab, "print", strlen("print"));
	sv1[0] = sv0;
	working_expr = pystr_from_c_str("Hel\x00lo", 6);
	sv1[1] = working_expr;
	working_expr = pystr_from_c_str("World", 5);
	sv1[2] = working_expr;
	sv1[3] = 0;
	working_expr = pystr_from_c_str(", (sep)", 7);
	hashmap_put(&hmap0, "sep", 3, working_expr);
	working_expr = pystr_from_c_str("! (end)\
", 8);
	hashmap_put(&hmap0, "end", 3, working_expr);
	working_expr = sv0->type->__call__(sv1, &hmap0);
	hashmap_destroy(&hmap0);
	
	QuitPythonC();
	return 0;
}