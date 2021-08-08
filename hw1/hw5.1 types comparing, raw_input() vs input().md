#### 1. Составить таблицу соответствия между различными объектами основных классов: int, str и объектами класса bool.
| Value | Type |bool("Value") | Value | Type |bool("Value") |
| ------ | ------ | ------| ------| ------| ------| 
| Never | str |True| 1 |int| true|
| Gonna | str |True| 10 | int | true|
| Give  | str |True| 100 | int | true|
| You | str |True| 1337 | int | true|
| Up | str |True|65536| int | true|
| Never | str|True|0| int | **false**|
| Gonna | str |True|25632420| int | true|
| Let | str |True|-1| int | true|
| You | str |True|-12312| int | true|
| Down | str |True|-65536| int | true|
| "" (empty str) | str |**False**|-324234242| int | true|
Все строки, кроме пустых - True.
Пустые строки - False.
Все целочисленные значения, кроме 0 - True.
Ноль - False.
#### 2. Разобраться с различиями между input() и raw_input(). Также в контексте разных версий python: 2 и 3.
|  | Python 2 |Python 3| 
| ------ | ------ | ------| 
| input() | Пытается запустить значение аргумента input, как код Python. |Соответствует raw_input() из Python 2. Функция читает строку из ввода и преобразует ее в строку (str).| 
| raw_input() | Функция читает строку из ввода и преобразует ее в строку (str). | Отсутствует, можно симулировать с помощью ```eval(input())```. Пытается запустить значение аргумента input, как код Python| 
#### 3. Найти и прочитать PEP про изменение print между python2 и python3.
print стал функцией, хотя был оператором.
Старый синтаксис, Python 2.6: ```print "The answer is", 2*2```
Новый синтаксис, Python 3: ```print("The answer is", 2*2)```
В Python 3 стало возможно изменить разделитель с помощью атрибута "sep": ```print("There are <", 2**32, "> possibilities!", sep="")``` 
Функция print() не поддерживает особенность "программный пробел" старого оператора print. Например, в Python 2, ```print "A\n", "B"``` напечатает "A\nB\n"; но в Python 3, ```print("A\n", "B")``` напечатает "A\n B\n".
