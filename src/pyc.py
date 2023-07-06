import os
import ast
from compiler import Compiler
from utils import ArgParser

def main():
	argparser = ArgParser("pyc" , description="PyC Compiler")
	argparser.add_argument("file", type=str)
	argparser.add_argument("-o", "--out", help="output c file", type=str)

	args = argparser.parse_args()

	file: str = args.file
	out = args.out

	if not os.path.exists(file):
		print(f"error: file {file!r} doesn't exist!")
		exit(1)

	try:
		with open(file, 'r') as f:
			code = f.read()
	except OSError as e:
		print(f"error: {e}")

	if out is None:
		out = '.'.join(file.split('.')[:-1])+".c"
		if out == ".c": out = f"{file}.c" # in case the input did not have any dots in it

	tree = ast.parse(code, type_comments=True)

	compiler = Compiler(tree)

	c_code = compiler.compile()

	try:
		with open(out, 'w') as f:
			f.write(c_code)

		print(f"Successfully written C output to {out!r}")
	except OSError as e:
		print(f"error: {e}")

if __name__ == "__main__":
	try: main()
	except KeyboardInterrupt: pass
	exit(0)