# Script for Electronic School Journal

This script is created to correct grades, remove remarks, and add commendations to the school's electronic school journal.
## Running

- Download the website archive from [Github](https://github.com/dvmn-tasks/e-diary), copy the database file to the root folder, and deploy the website.
- Put the `script.py` file next to `manage.py` in the root of the website.
- Run the Shell console `python manage.py shell`.
- Install the script in the terminal with the command `import script`.
- Run the script with the command `script.main()`.
- After the prompt `Введите фамилию и имя`, enter the full name of the student.
- In the empty field after `Введите название предмета`, add the lesson name for adding a commendation.

## Additional Usage Options

To run specific tasks, after installing the script, enter the following commands in the terminal window:

`fix_marks('Фамилия Имя')` - a function to fix grades to fives, where you need to substitute the real student's data (without errors) instead of Last Name and First Name. In case of an error, the terminal will show `"Имя ученика введено с ошибкой"`, which means you need to use the command again.

`remove_chastisements('Фамилия Имя')` - a function to remove remarks from the teacher, where Last Name and First Name are substituted similarly to the function above.

`create_commendation('Фамилия Имя', 'Предмет')` - a function to add a commendation from the teacher. Here, enter the Last Name and First Name in quotes first, and then, separated by a comma, in quotes as well, enter the name of the desired subject on which the commendation will be given to the selected student. In case of an error in the subject name, `"Ошибка: введено несколько учеников"` will be displayed.

## Usage Examples

```python manage.py shell

>>> import script

>>> script.main()

Ввведите фамилию и имя
>Иванов Иван

Введите название предмета
>Музыка
>>>
```
