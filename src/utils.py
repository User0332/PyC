from argparse import ArgumentParser
from typing import NoReturn

class ArgParser(ArgumentParser):
	def error(self, message: str) -> NoReturn:
		print(f"error: {message}")
		exit(1)