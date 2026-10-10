# Документация проекта

## Общая информация

Этот проект содержит библиотеку, реализованную на Python - Geometric Lib
Каждый модуль содержит по 2 функции: area(...) — для вычисления площади и perimeter(...) — для вычисления периметра. Функции принимают определенные параметры фигуры и возвращают числовое значение.

## Описание функций

### triangle.py

area(a, h)
Принимает длину стороны a и длину высоты h, проведённой к этой стороне, возвращает площадь треугольника.
Формула: S = a * h / 2
```python
from triangle import area
# Пример вызовов функций:
area(6, 12) # 36
```

perimeter(a, b, c)
Принимает длины сторон треугольника, возвращает его периметр
Формула: P = a + b + c
```python
from triangle import perimeter
# Пример вызовов функций:
perimeter(6, 4, 8) # 18
```

### square.py

area(a)
Принимает сторону квадрата, возвращает его площадь
Формула: S = a * a
```python
from square import area
# Пример вызовов функций:
area(6) # 36
```

perimeter(a)
Принимает сторону квадарата, возвращает его периметр
Формула: P = a * 4
```python
from square import perimeter
# Пример вызовов функций:
perimeter(6) # 24
```

### rectangle.py

area(a, b)
Принимает длины сторон прямоугольника, возвращает его площадь
Формула: P = a * b
```python
from rectangle import area
# Пример вызовов функций:
area(6, 4) # 24
```

perimeter(a, b)
По полученным длинам сторон прямоугольника вычисляет его периметр
Формула: P = 2 * (a + b)
```python
from rectangle import perimeter
# Пример вызовов функций:
perimeter(6, 5) # 22
```

### circle.py

area(r)
Принимает радиус круга, возвращает его площадь
Формула: P = πR²
```python
from circle import area
# Пример вызовов функций:
area(14) # 615.5721601035994
```

perimeter(r)
Принимает радиус окружности, возвращает ее периметр
Формула: P = 2πR
```python
from circle import perimeter
# Пример вызовов функций:
perimeter(7) # 43.982297150257104
```

## История изменений

e505aa9 (HEAD -> new_features_558282) Added descriptions in every python file. Added docs/projectnotation.md which contains description of functions, formulas  behind them and examples of usage

369d5a7 (origin/new_features_558282) Added triangle.py

1cc1374 Fixed perimeter calculation in rectangle.py

9a27bc5 Added new file rectangle.py

d078c8d (origin/main, origin/HEAD, main) L-03: Docs added

8ba9aeb L-03: Circle and square added