@echo off
echo tailwind_theme > input.txt
echo 2 >> input.txt
python manage.py tailwind init < input.txt
del input.txt 