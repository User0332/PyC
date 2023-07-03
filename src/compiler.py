from _ast import AST, Add, And, AnnAssign, Assert, Assign, AsyncFor, AsyncFunctionDef, AsyncWith, Attribute, AugAssign, Await, BinOp, BitAnd, BitOr, BitXor, BoolOp, Break, Call, ClassDef, Compare, Constant, Continue, Del, Delete, Dict, DictComp, Div, Eq, ExceptHandler, Expr, Expression, FloorDiv, For, FormattedValue, FunctionDef, GeneratorExp, Global, Gt, GtE, If, IfExp, Import, ImportFrom, In, Interactive, Invert, Is, IsNot, JoinedStr, LShift, Lambda, List, ListComp, Load, Lt, LtE, MatMult, Match, MatchAs, MatchClass, MatchMapping, MatchOr, MatchSequence, MatchStar, MatchValue, Mod, Module, Mult, Name, NamedExpr, Nonlocal, Not, NotEq, NotIn, Or, Pass, Pow, RShift, Raise, Return, Set, SetComp, Slice, Starred, Store, Sub, Subscript, Try, Tuple, TypeIgnore, UAdd, USub, UnaryOp, While, With, Yield, YieldFrom, alias, arg, arguments, comprehension, keyword, withitem
from ast import AugLoad, AugStore, Bytes, Ellipsis, ExtSlice, Index, NameConstant, NodeVisitor, AST, Num, Param, Str, Suite
from typing import Any

class Compiler(NodeVisitor):
	def __init__(self, tree: AST):
		self.ast = tree
		self.data = "section .data\n\n"
		self.bss = "section .bss\n\n"
		self.text = "section .text\n\n"

	def compile(self):
		self.visit(self.ast)

		return '\n\n'.join((self.text, self.data, self.bss))

		
	def generic_visit(self, node: AST):
		pass # raise exc

	def visit_Add(self, node: Add) -> Any:
		return super().visit_Add(node)
	
	def visit_alias(self, node: alias) -> Any:
		return super().visit_alias(node)
	
	def visit_And(self, node: And) -> Any:
		return super().visit_And(node)
	
	def visit_Set(self, node: Set) -> Any:
		return super().visit_Set(node)
	
	def visit_YieldFrom(self, node: YieldFrom) -> Any:
		return super().visit_YieldFrom(node)
	
	def visit_AnnAssign(self, node: AnnAssign) -> Any:
		return super().visit_AnnAssign(node)
	
	def visit_arg(self, node: arg) -> Any:
		return super().visit_arg(node)
	
	def visit_Assert(self, node: Assert) -> Any:
		return super().visit_Assert(node)
	
	def visit_arguments(self, node: arguments) -> Any:
		return super().visit_arguments(node)
	
	def visit_Assign(self, node: Assign) -> Any:
		return super().visit_Assign(node)
	
	def visit_AsyncFor(self, node: AsyncFor) -> Any:
		return super().visit_AsyncFor(node)
	
	def visit_AsyncFunctionDef(self, node: AsyncFunctionDef) -> Any:
		return super().visit_AsyncFunctionDef(node)
	
	def visit_AsyncWith(self, node: AsyncWith) -> Any:
		return super().visit_AsyncWith(node)
	
	def visit_Attribute(self, node: Attribute) -> Any:
		return super().visit_Attribute(node)
	
	def visit_AugAssign(self, node: AugAssign) -> Any:
		return super().visit_AugAssign(node)
	
	def visit_AugLoad(self, node: AugLoad) -> Any:
		return super().visit_AugLoad(node)
	
	def visit_AugStore(self, node: AugStore) -> Any:
		return super().visit_AugStore(node)
	
	def visit_Await(self, node: Await) -> Any:
		return super().visit_Await(node)
	
	def visit_BinOp(self, node: BinOp) -> Any:
		return super().visit_BinOp(node)
	
	def visit_BitAnd(self, node: BitAnd) -> Any:
		return super().visit_BitAnd(node)

	def visit_BitOr(self, node: BitOr) -> Any:
		return super().visit_BitOr(node)
	
	def visit_BitXor(self, node: BitXor) -> Any:
		return super().visit_BitXor(node)

	def visit_BoolOp(self, node: BoolOp) -> Any:
		return super().visit_BoolOp(node)
	
	def visit_Break(self, node: Break) -> Any:
		return super().visit_Break(node)
	
	def visit_Bytes(self, node: Bytes) -> Any:
		return super().visit_Bytes(node)

	def visit_Call(self, node: Call) -> Any:
		return super().visit_Call(node)

	def visit_ClassDef(self, node: ClassDef) -> Any:
		return super().visit_ClassDef(node)

	def visit_Compare(self, node: Compare) -> Any:
		return super().visit_Compare(node)
	
	def visit_comprehension(self, node: comprehension) -> Any:
		return super().visit_comprehension(node)
	
	def visit_Constant(self, node: Constant) -> Any:
		return super().visit_Constant(node)
	
	def visit_Continue(self, node: Continue) -> Any:
		return super().visit_Continue(node)
	
	def visit_Del(self, node: Del) -> Any:
		return super().visit_Del(node)
	
	def visit_Delete(self, node: Delete) -> Any:
		return super().visit_Delete(node)
	
	def visit_Dict(self, node: Dict) -> Any:
		return super().visit_Dict(node)
	
	def visit_DictComp(self, node: DictComp) -> Any:
		return super().visit_DictComp(node)
	
	def visit_Div(self, node: Div) -> Any:
		return super().visit_Div(node)
	
	def visit_MatchValue(self, node: MatchValue) -> Any:
		return super().visit_MatchValue(node)
	
	def visit_Ellipsis(self, node: Ellipsis) -> Any:
		return super().visit_Ellipsis(node)
	
	def visit_Eq(self, node: Eq) -> Any:
		return super().visit_Eq(node)
	
	def visit_ExceptHandler(self, node: ExceptHandler) -> Any:
		return super().visit_ExceptHandler(node)
	
	def visit_Expr(self, node: Expr) -> Any:
		return super().visit_Expr(node)
	
	def visit_Expression(self, node: Expression) -> Any:
		return super().visit_Expression(node)
	
	def visit_ExtSlice(self, node: ExtSlice) -> Any:
		return super().visit_ExtSlice(node)
	
	def visit_FloorDiv(self, node: FloorDiv) -> Any:
		return super().visit_FloorDiv(node)
	
	def visit_For(self, node: For) -> Any:
		return super().visit_For(node)
	
	def visit_FormattedValue(self, node: FormattedValue) -> Any:
		return super().visit_FormattedValue(node)
	
	def visit_FunctionDef(self, node: FunctionDef) -> Any:
		return super().visit_FunctionDef(node)
	
	def visit_Invert(self, node: Invert) -> Any:
		return super().visit_Invert(node)
	
	def visit_GeneratorExp(self, node: GeneratorExp) -> Any:
		return super().visit_GeneratorExp(node)
	
	def visit_Global(self, node: Global) -> Any:
		return super().visit_Global(node)
	
	def visit_Gt(self, node: Gt) -> Any:
		return super().visit_Gt(node)
	
	def visit_GtE(self, node: GtE) -> Any:
		return super().visit_GtE(node)
	
	def visit_If(self, node: If) -> Any:
		return super().visit_If(node)
	
	def visit_IfExp(self, node: IfExp) -> Any:
		return super().visit_IfExp(node)
	
	def visit_Import(self, node: Import) -> Any:
		return super().visit_Import(node)
	
	def visit_ImportFrom(self, node: ImportFrom) -> Any:
		return super().visit_ImportFrom(node)
	
	def visit_In(self, node: In) -> Any:
		return super().visit_In(node)
	
	def visit_Index(self, node: Index) -> Any:
		return super().visit_Index(node)
	
	def visit_Interactive(self, node: Interactive) -> Any:
		return super().visit_Interactive(node)
	
	def visit_Is(self, node: Is) -> Any:
		return super().visit_Is(node)
	
	def visit_IsNot(self, node: IsNot) -> Any:
		return super().visit_IsNot(node)
	
	def visit_JoinedStr(self, node: JoinedStr) -> Any:
		return super().visit_JoinedStr(node)
	
	def visit_keyword(self, node: keyword) -> Any:
		return super().visit_keyword(node)
	
	def visit_Lambda(self, node: Lambda) -> Any:
		return super().visit_Lambda(node)
	
	def visit_List(self, node: List) -> Any:
		return super().visit_List(node)
	
	def visit_ListComp(self, node: ListComp) -> Any:
		return super().visit_ListComp(node)
	
	def visit_Load(self, node: Load) -> Any:
		return super().visit_Load(node)
	
	def visit_LShift(self, node: LShift) -> Any:
		return super().visit_LShift(node)
	
	def visit_Lt(self, node: Lt) -> Any:
		return super().visit_Lt(node)
	
	def visit_LtE(self, node: LtE) -> Any:
		return super().visit_LtE(node)
	
	def visit_Match(self, node: Match) -> Any:
		return super().visit_Match(node)
	
	def visit_MatchAs(self, node: MatchAs) -> Any:
		return super().visit_MatchAs(node)
	
	def visit_MatchClass(self, node: MatchClass) -> Any:
		return super().visit_MatchClass(node)
	
	def visit_MatchMapping(self, node: MatchMapping) -> Any:
		return super().visit_MatchMapping(node)

	def visit_MatchOr(self, node: MatchOr) -> Any:
		return super().visit_MatchOr(node)

	def visit_MatchSequence(self, node: MatchSequence) -> Any:
		return super().visit_MatchSequence(node)

	def visit_MatchStar(self, node: MatchStar) -> Any:
		return super().visit_MatchStar(node)
	
	def visit_MatMult(self, node: MatMult) -> Any:
		return super().visit_MatMult(node)
	
	def visit_Mod(self, node: Mod) -> Any:
		return super().visit_Mod(node)

	def visit_Module(self, node: Module) -> Any:
		return super().visit_Module(node)

	def visit_Mult(self, node: Mult) -> Any:
		return super().visit_Mult(node)

	def visit_Name(self, node: Name) -> Any:
		return super().visit_Name(node)

	def visit_NameConstant(self, node: NameConstant) -> Any:
		return super().visit_NameConstant(node)
	
	def visit_NamedExpr(self, node: NamedExpr) -> Any:
		return super().visit_NamedExpr(node)

	def visit_Nonlocal(self, node: Nonlocal) -> Any:
		return super().visit_Nonlocal(node)

	def visit_Not(self, node: Not) -> Any:
		return super().visit_Not(node)

	def visit_NotEq(self, node: NotEq) -> Any:
		return super().visit_NotEq(node)
	
	def visit_NotIn(self, node: NotIn) -> Any:
		return super().visit_NotIn(node)

	def visit_Num(self, node: Num) -> Any:
		return super().visit_Num(node)

	def visit_Or(self, node: Or) -> Any:
		return super().visit_Or(node)
	
	def visit_Param(self, node: Param) -> Any:
		return super().visit_Param(node)
	
	def visit_Pass(self, node: Pass) -> Any:
		return super().visit_Pass(node)
	
	def visit_Pow(self, node: Pow) -> Any:
		return super().visit_Pow(node)
	
	def visit_Raise(self, node: Raise) -> Any:
		return super().visit_Raise(node)
	
	def visit_Return(self, node: Return) -> Any:
		return super().visit_Return(node)
	
	def visit_RShift(self, node: RShift) -> Any:
		return super().visit_RShift(node)
	
	def visit_SetComp(self, node: SetComp) -> Any:
		return super().visit_SetComp(node)
	
	def visit_Slice(self, node: Slice) -> Any:
		return super().visit_Slice(node)
	
	def visit_Starred(self, node: Starred) -> Any:
		return super().visit_Starred(node)
	
	def visit_Store(self, node: Store) -> Any:
		return super().visit_Store(node)
	
	def visit_Str(self, node: Str) -> Any:
		return super().visit_Str(node)
	
	def visit_Sub(self, node: Sub) -> Any:
		return super().visit_Sub(node)
	
	def visit_Subscript(self, node: Subscript) -> Any:
		return super().visit_Subscript(node)
	
	def visit_Suite(self, node: Suite) -> Any:
		return super().visit_Suite(node)
	
	def visit_Try(self, node: Try) -> Any:
		return super().visit_Try(node)
	
	def visit_Tuple(self, node: Tuple) -> Any:
		return super().visit_Tuple(node)
	
	def visit_TypeIgnore(self, node: TypeIgnore) -> Any:
		return super().visit_TypeIgnore(node)
	
	def visit_UAdd(self, node: UAdd) -> Any:
		return super().visit_UAdd(node)
	
	def visit_UnaryOp(self, node: UnaryOp) -> Any:
		return super().visit_UnaryOp(node)
	
	def visit_USub(self, node: USub) -> Any:
		return super().visit_USub(node)
	
	def visit_While(self, node: While) -> Any:
		return super().visit_While(node)
	
	def visit_With(self, node: With) -> Any:
		return super().visit_With(node)
	
	def visit_withitem(self, node: withitem) -> Any:
		return super().visit_withitem(node)
	
	def visit_Yield(self, node: Yield) -> Any:
		return super().visit_Yield(node)