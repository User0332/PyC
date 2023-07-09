if [ $2 == "py" ]
then
    python pyc.py $1.py
fi

gcc -o $1 $1.c engine/* -Wall