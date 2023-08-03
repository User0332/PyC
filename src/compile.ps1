if ($args[1] -eq "py")
{
	python pyc.py "$($args[0]).py"
}

gcc -o "$($args[0]).exe" "$($args[0]).c" engine/*.c engine/*.h engine/**/*.c engine/**/*.h -Wall