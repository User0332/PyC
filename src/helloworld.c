#include <string.h>
#include "engine/PyC.h"

int main()
{
	InitPythonC();

	PyC_Object* sv1[3];
	PyC_Object* sv0;
	PyC_Object* sv3;
	PyC_Object* sv2;
	
	PyC_Object* working_expr = NULL;
	PyC_Object* pushed_expr = NULL; // fix, this, may be bad design (follow same pattern as used in UntypedScript, use __asm__ if needed)

	sv0 = hashmap_get(&__main__mod_symtab, "print", strlen("print"));
	sv1[0] = sv0;
	sv2 = pystr_from_c_str("Hel\x00lo, ", 8);
	sv3 = pystr_from_c_str("World!", 6);
	if ((working_expr = sv2->type->__add__((PyC_Object* []) { sv2, sv3, 0 })) == &PyBuiltins_NotImplemented) {
		if ((working_expr = sv3->type->__radd__((PyC_Object* []) { sv3, sv2, 0 })) == &PyBuiltins_NotImplemented) {
			raise_cstr("TypeError: cannot perform addition between objects of type %s and %s");
		}
	}
	sv1[1] = working_expr;
	sv1[2] = 0;
	working_expr = sv0->type->__call__(sv1);
	
	QuitPythonC();
	return 0;
}