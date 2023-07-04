import os
import ast
from compiler import Compiler
from utils import ArgParser

def main():
	argparser = ArgParser("pyc" , description="PyC Compiler")
	argparser.add_argument("file", type=str)

	args = argparser.parse_args()

	file: str = args.file

	if not os.path.exists(file):
		print(f"error: file {file!r} doesn't exist!")
		exit(1)

	try:
		with open(file, 'r') as f:
			code = f.read()
	except OSError as e:
		print(f"error: {e}")

	tree = ast.parse(code, type_comments=True)

if __name__ == "__main__":
	try: main()
	except KeyboardInterrupt: pass
	exit(0)