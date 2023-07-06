from json import dumps
from _ast import AST, Add, And, AnnAssign, Assert, Assign, AsyncFor, AsyncFunctionDef, AsyncWith, Attribute, AugAssign, Await, BinOp, BitAnd, BitOr, BitXor, BoolOp, Break, Call, ClassDef, Compare, Constant, Continue, Del, Delete, Dict, DictComp, Div, Eq, ExceptHandler, Expr, Expression, FloorDiv, For, FormattedValue, FunctionDef, GeneratorExp, Global, Gt, GtE, If, IfExp, Import, ImportFrom, In, Interactive, Invert, Is, IsNot, JoinedStr, LShift, Lambda, List, ListComp, Load, Lt, LtE, MatMult, Match, MatchAs, MatchClass, MatchMapping, MatchOr, MatchSequence, MatchStar, MatchValue, Mod, Module, Mult, Name, NamedExpr, Nonlocal, Not, NotEq, NotIn, Or, Pass, Pow, RShift, Raise, Return, Set, SetComp, Slice, Starred, Store, Sub, Subscript, Try, Tuple, TypeIgnore, UAdd, USub, UnaryOp, While, With, Yield, YieldFrom, alias, arg, arguments, comprehension, keyword, withitem
from ast import AugLoad, AugStore, Bytes, Ellipsis, ExtSlice, Index, NameConstant, NodeVisitor, AST, Num, Param, Str, Suite, stmt
from typing import Any

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

	def gen_stackvar(self) -> str:
		var = f"sv{len(self.stackvars)}"

		self.stackvars.append(var)

		return var

	def build_stackvars(self) -> str:
		stackvar_code = "\n\t"

		for var in self.saved_stackvars:
			stackvar_code+=f"PyC_Object* {var};\n\t"

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
			self.code+=f"if (working_expr = {left}->type->__call__((PyC_Object* []) {{ {left}, right }}"

			for arg in node.args:
				self.visit(arg)
				self.code+=", "

			self.code+="0 })"		
			return # unimpled
		else: # switch dict for a sym lookup (with some NotImplemented checks for two-way ops (such as ==))
	
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

		self.code+=f"{stackvar} = "

		self.visit(node.func)
		self.code+=";\n\t"

		self.code+=f"working_expr = {stackvar}->type->__call__((PyC_Object* []) {{ {stackvar}, "

		for arg in node.args:
			self.visit(arg)
			self.code+=", "

		self.code+="0 })"

	def visit_ClassDef(self, node: ClassDef) -> Any:
		return # unimpled

	def visit_Compare(self, node: Compare) -> Any:
		return # unimpled
	
	def visit_comprehension(self, node: comprehension) -> Any:
		return # unimpled
	
	def visit_Constant(self, node: Constant) -> Any:
		if type(node.value) is str:
			self.code+=f"pystr_from_c_str({dumps(node.value)})"
	
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