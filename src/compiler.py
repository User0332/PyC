from json import dumps
from _ast import AST, Add, And, AnnAssign, Assert, Assign, AsyncFor, AsyncFunctionDef, AsyncWith, Attribute, AugAssign, Await, BinOp, BitAnd, BitOr, BitXor, BoolOp, Break, Call, ClassDef, Compare, Constant, Continue, Del, Delete, Dict, DictComp, Div, Eq, ExceptHandler, Expr, Expression, FloorDiv, For, FormattedValue, FunctionDef, GeneratorExp, Global, Gt, GtE, If, IfExp, Import, ImportFrom, In, Interactive, Invert, Is, IsNot, JoinedStr, LShift, Lambda, List, ListComp, Load, Lt, LtE, MatMult, Match, MatchAs, MatchClass, MatchMapping, MatchOr, MatchSequence, MatchStar, MatchValue, Mod, Module, Mult, Name, NamedExpr, Nonlocal, Not, NotEq, NotIn, Or, Pass, Pow, RShift, Raise, Return, Set, SetComp, Slice, Starred, Store, Sub, Subscript, Try, Tuple, TypeIgnore, UAdd, USub, UnaryOp, While, With, Yield, YieldFrom, alias, arg, arguments, comprehension, keyword, withitem
from ast import AugLoad, AugStore, Bytes, Ellipsis, ExtSlice, Index, NameConstant, NodeVisitor, AST, Num, Param, Str, Suite, stmt
from typing import Any

def string_to_c(s, max_length = 140, unicode=False):
    ret = []

    # Try to split on whitespace, not in the middle of a word.
    split_at_space_pos = max_length - 10
    if split_at_space_pos < 10:
        split_at_space_pos = None

    position = 0
    if unicode:
        position += 1
        ret.append('L')

    ret.append('"')
    position += 1
    for c in s:
        newline = False
        if c == "\n":
            to_add = "\\\n"
            newline = True
        elif ord(c) < 32 or 0x80 <= ord(c) <= 0xff:
            to_add = "\\x%02x" % ord(c)
        elif ord(c) > 0xff:
            if not unicode:
                raise ValueError("string contains unicode character but unicode=False")
            to_add = "\\u%04x" % ord(c)
        elif "\\\"".find(c) != -1:
            to_add = "\\%c" % c
        else:
            to_add = c

        ret.append(to_add)
        position += len(to_add)
        if newline:
            position = 0

        if split_at_space_pos is not None and position >= split_at_space_pos and " \t".find(c) != -1:
            ret.append("\\\n")
            position = 0
        elif position >= max_length:
            ret.append("\\\n")
            position = 0

    ret.append('"')

    return "".join(ret)

class Compiler(NodeVisitor):
	def __init__(self, tree: AST):
		self.ast = tree

		# keep this code setup for now, but change it later based on whether this should be compiled as an importable module

		self.main_start = """#include <string.h>
#include "engine/PyC.h"

int main()
{
	InitPythonC();
"""

		self.code = """
	PyC_Object* working_expr = NULL;
	PyC_Object* pushed_expr = NULL; // fix, this, may be bad design (follow same pattern as used in UntypedScript, use __asm__ if needed)

	"""
		self.saved_stackvars: set[str] = set()
		self.stackvars: list[str] = []
		self.saved_hmaps: set[str] = set()
		self.hmaps: list[str] = []

	def gen_hmap(self):
		var = f"hmap{len(self.hmaps)}"

		self.hmaps.append(var)

		self.code+=f"hashmap_create(5, &{var});\n\t"

		return var

	def gen_stackvar(self, args: int=0) -> str:
		var = f"sv{len(self.stackvars)}"

		self.stackvars.append(var if not args else var+f"[{args}]")

		return var

	def build_stackvars(self) -> str:
		stackvar_code = "\n\t"

		for var in self.saved_stackvars:
			stackvar_code+=f"PyC_Object* {var};\n\t"

		for var in self.saved_hmaps:
			stackvar_code+=f"hashmap {var};\n\t"

		return stackvar_code

	def compile(self):
		self.visit(self.ast)

		return self.main_start+self.build_stackvars()+self.code+"\n\tQuitPythonC();\n\treturn 0;\n}"

	def visit(self, node: AST, modchild: bool=False):
		if type(node) is Module:
			for child in node.body:
				self.visit(child, modchild=True)

			return

		super().visit(node)

		if modchild:
			self.code+=";\n\t"
			
			for var in self.stackvars: self.saved_stackvars.add(var)
			for var in self.hmaps:
				self.saved_hmaps.add(var)
				self.code+=f"hashmap_destroy(&{var});\n\t"

			self.hmaps.clear()
			self.stackvars.clear() # add this to function-level stmts once impled
		
	def generic_visit(self, node: AST):
		pass # raise exc

	def visit_Add(self, node: Add) -> Any:
		return # unimpled
	
	def visit_alias(self, node: alias) -> Any:
		return # unimpled
	
	def visit_And(self, node: And) -> Any:
		return # unimpled
	
	def visit_Set(self, node: Set) -> Any:
		return # unimpled
	
	def visit_YieldFrom(self, node: YieldFrom) -> Any:
		return # unimpled
	
	def visit_AnnAssign(self, node: AnnAssign) -> Any:
		return # unimpled
	
	def visit_arg(self, node: arg) -> Any:
		return # unimpled
	
	def visit_Assert(self, node: Assert) -> Any:
		return # unimpled
	
	def visit_arguments(self, node: arguments) -> Any:
		return # unimpled
	
	def visit_Assign(self, node: Assign) -> Any:
		return # unimpled
	
	def visit_AsyncFor(self, node: AsyncFor) -> Any:
		return # unimpled
	
	def visit_AsyncFunctionDef(self, node: AsyncFunctionDef) -> Any:
		return # unimpled
	
	def visit_AsyncWith(self, node: AsyncWith) -> Any:
		return # unimpled
	
	def visit_Attribute(self, node: Attribute) -> Any:
		return # unimpled
	
	def visit_AugAssign(self, node: AugAssign) -> Any:
		return # unimpled
	
	def visit_AugLoad(self, node: AugLoad) -> Any:
		return # unimpled
	
	def visit_AugStore(self, node: AugStore) -> Any:
		return # unimpled
	
	def visit_Await(self, node: Await) -> Any:
		return # unimpled
	
	def visit_BinOp(self, node: BinOp) -> Any:
		left = self.gen_stackvar()
		right = self.gen_stackvar()

		self.code+=f"{left} = "

		self.visit(node.left)
		self.code+=";\n\t"

		self.code+=f"{right} = "

		self.visit(node.right)
		self.code+=";\n\t"

		if type(node.op) is Add:
			self.code+=f"""if ((working_expr = {left}->type->__add__((PyC_Object* []) {{ {left}, {right}, 0 }})) == &PyBuiltins_NotImplemented) {{
		if ((working_expr = {right}->type->__radd__((PyC_Object* []) {{ {right}, {left}, 0 }})) == &PyBuiltins_NotImplemented) {{
			raise_cstr("TypeError: cannot perform addition between objects of type %s and %s");
		}}
	}}\n\t"""
		else: pass# switch dict for a sym lookup (with some NotImplemented checks for two-way ops (such as ==))
	
	def visit_BitAnd(self, node: BitAnd) -> Any:
		return # unimpled

	def visit_BitOr(self, node: BitOr) -> Any:
		return # unimpled
	
	def visit_BitXor(self, node: BitXor) -> Any:
		return # unimpled

	def visit_BoolOp(self, node: BoolOp) -> Any:
		return # unimpled
	
	def visit_Break(self, node: Break) -> Any:
		return # unimpled
	
	def visit_Bytes(self, node: Bytes) -> Any:
		return # unimpled

	def visit_Call(self, node: Call) -> Any:
		stackvar = self.gen_stackvar()
		kwargsmap = self.gen_hmap()
		argsarr = self.gen_stackvar(args=len(node.args)+2) # find more reliable usage later, (ex. we won't know the arg length for unpacked iterables)

		self.code+=f"{stackvar} = "

		self.visit(node.func)
		self.code+=";\n\t"

		self.code+=f"{argsarr}[0] = {stackvar};\n\t"

		for i, arg in enumerate(node.args, start=1):
			self.visit(arg)
			self.code+=f"{argsarr}[{i}] = working_expr;\n\t"

		self.code+=f"{argsarr}[{len(node.args)+1}] = 0;\n\t" # ^^^^^^ see above comment -- this line also uses len(node.args)

		for kwarg in node.keywords:
			name = kwarg.arg
			val = kwarg.value

			self.visit(val)

			self.code+=f"hashmap_put(&{kwargsmap}, {string_to_c(name)}, {len(name)}, working_expr);\n\t"

		self.code+=f"working_expr = {stackvar}->type->__call__({argsarr}, &{kwargsmap})"

	def visit_ClassDef(self, node: ClassDef) -> Any:
		return # unimpled

	def visit_Compare(self, node: Compare) -> Any:
		return # unimpled
	
	def visit_comprehension(self, node: comprehension) -> Any:
		return # unimpled
	
	def visit_Constant(self, node: Constant) -> Any:
		if type(node.value) is str:
			length = len(node.value)
			self.code+=f"working_expr = pystr_from_c_str({string_to_c(node.value)}, {length});\n\t"
	
	def visit_Continue(self, node: Continue) -> Any:
		return # unimpled
	
	def visit_Del(self, node: Del) -> Any:
		return # unimpled
	
	def visit_Delete(self, node: Delete) -> Any:
		return # unimpled
	
	def visit_Dict(self, node: Dict) -> Any:
		return # unimpled
	
	def visit_DictComp(self, node: DictComp) -> Any:
		return # unimpled
	
	def visit_Div(self, node: Div) -> Any:
		return # unimpled
	
	def visit_MatchValue(self, node: MatchValue) -> Any:
		return # unimpled
	
	def visit_Ellipsis(self, node: Ellipsis) -> Any:
		return # unimpled
	
	def visit_Eq(self, node: Eq) -> Any:
		return # unimpled
	
	def visit_ExceptHandler(self, node: ExceptHandler) -> Any:
		return # unimpled
	
	def visit_Expr(self, node: Expr) -> Any:
		return self.visit(node.value)
	
	def visit_Expression(self, node: Expression) -> Any:
		return # unimpled
	
	def visit_ExtSlice(self, node: ExtSlice) -> Any:
		return # unimpled
	
	def visit_FloorDiv(self, node: FloorDiv) -> Any:
		return # unimpled
	
	def visit_For(self, node: For) -> Any:
		return # unimpled
	
	def visit_FormattedValue(self, node: FormattedValue) -> Any:
		return # unimpled
	
	def visit_FunctionDef(self, node: FunctionDef) -> Any:
		return # unimpled
	
	def visit_Invert(self, node: Invert) -> Any:
		return # unimpled
	
	def visit_GeneratorExp(self, node: GeneratorExp) -> Any:
		return # unimpled
	
	def visit_Global(self, node: Global) -> Any:
		return # unimpled
	
	def visit_Gt(self, node: Gt) -> Any:
		return # unimpled
	
	def visit_GtE(self, node: GtE) -> Any:
		return # unimpled
	
	def visit_If(self, node: If) -> Any:
		return # unimpled
	
	def visit_IfExp(self, node: IfExp) -> Any:
		return # unimpled
	
	def visit_Import(self, node: Import) -> Any:
		return # unimpled
	
	def visit_ImportFrom(self, node: ImportFrom) -> Any:
		return # unimpled
	
	def visit_In(self, node: In) -> Any:
		return # unimpled
	
	def visit_Index(self, node: Index) -> Any:
		return # unimpled
	
	def visit_Interactive(self, node: Interactive) -> Any:
		return # unimpled
	
	def visit_Is(self, node: Is) -> Any:
		return # unimpled
	
	def visit_IsNot(self, node: IsNot) -> Any:
		return # unimpled
	
	def visit_JoinedStr(self, node: JoinedStr) -> Any:
		return # unimpled
	
	def visit_keyword(self, node: keyword) -> Any:
		return # unimpled
	
	def visit_Lambda(self, node: Lambda) -> Any:
		return # unimpled
	
	def visit_List(self, node: List) -> Any:
		return # unimpled
	
	def visit_ListComp(self, node: ListComp) -> Any:
		return # unimpled
	
	def visit_Load(self, node: Load) -> Any:
		return # unimpled
	
	def visit_LShift(self, node: LShift) -> Any:
		return # unimpled
	
	def visit_Lt(self, node: Lt) -> Any:
		return # unimpled
	
	def visit_LtE(self, node: LtE) -> Any:
		return # unimpled
	
	def visit_Match(self, node: Match) -> Any:
		return # unimpled
	
	def visit_MatchAs(self, node: MatchAs) -> Any:
		return # unimpled
	
	def visit_MatchClass(self, node: MatchClass) -> Any:
		return # unimpled
	
	def visit_MatchMapping(self, node: MatchMapping) -> Any:
		return # unimpled

	def visit_MatchOr(self, node: MatchOr) -> Any:
		return # unimpled

	def visit_MatchSequence(self, node: MatchSequence) -> Any:
		return # unimpled

	def visit_MatchStar(self, node: MatchStar) -> Any:
		return # unimpled
	
	def visit_MatMult(self, node: MatMult) -> Any:
		return # unimpled
	
	def visit_Mod(self, node: Mod) -> Any:
		return # unimpled

	def visit_Module(self, node: Module) -> Any:
		return # unimpled

	def visit_Mult(self, node: Mult) -> Any:
		return # unimpled

	def visit_Name(self, node: Name) -> Any:
		strname = dumps(node.id)
		self.code+=f"hashmap_get(&__main__mod_symtab, {strname}, strlen({strname}))" # change this to use getattr later

	def visit_NameConstant(self, node: NameConstant) -> Any:
		return # unimpled
	
	def visit_NamedExpr(self, node: NamedExpr) -> Any:
		return # unimpled

	def visit_Nonlocal(self, node: Nonlocal) -> Any:
		return # unimpled

	def visit_Not(self, node: Not) -> Any:
		return # unimpled

	def visit_NotEq(self, node: NotEq) -> Any:
		return # unimpled
	
	def visit_NotIn(self, node: NotIn) -> Any:
		return # unimpled

	def visit_Num(self, node: Num) -> Any:
		return # unimpled

	def visit_Or(self, node: Or) -> Any:
		return # unimpled
	
	def visit_Param(self, node: Param) -> Any:
		return # unimpled
	
	def visit_Pass(self, node: Pass) -> Any:
		return # unimpled
	
	def visit_Pow(self, node: Pow) -> Any:
		return # unimpled
	
	def visit_Raise(self, node: Raise) -> Any:
		return # unimpled
	
	def visit_Return(self, node: Return) -> Any:
		return # unimpled
	
	def visit_RShift(self, node: RShift) -> Any:
		return # unimpled
	
	def visit_SetComp(self, node: SetComp) -> Any:
		return # unimpled
	
	def visit_Slice(self, node: Slice) -> Any:
		return # unimpled
	
	def visit_Starred(self, node: Starred) -> Any:
		return # unimpled
	
	def visit_Store(self, node: Store) -> Any:
		return # unimpled
	
	def visit_Str(self, node: Str) -> Any:
		return # unimpled
	
	def visit_Sub(self, node: Sub) -> Any:
		return # unimpled
	
	def visit_Subscript(self, node: Subscript) -> Any:
		return # unimpled
	
	def visit_Suite(self, node: Suite) -> Any:
		return # unimpled
	
	def visit_Try(self, node: Try) -> Any:
		return # unimpled
	
	def visit_Tuple(self, node: Tuple) -> Any:
		return # unimpled
	
	def visit_TypeIgnore(self, node: TypeIgnore) -> Any:
		return # unimpled
	
	def visit_UAdd(self, node: UAdd) -> Any:
		return # unimpled
	
	def visit_UnaryOp(self, node: UnaryOp) -> Any:
		return # unimpled
	
	def visit_USub(self, node: USub) -> Any:
		return # unimpled
	
	def visit_While(self, node: While) -> Any:
		return # unimpled
	
	def visit_With(self, node: With) -> Any:
		return # unimpled
	
	def visit_withitem(self, node: withitem) -> Any:
		return # unimpled
	
	def visit_Yield(self, node: Yield) -> Any:
		return # unimpled