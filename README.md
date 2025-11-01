# Лабораторная работа номер 2 

## Мини оболочка с файловыми командами
Делалось на windows 10
Ввод бесконечный пока не введешь break
## Структура проекта
 <pre>
  ├── src/ # Исходный код
  │ ├── init.py # Инициализация 
  │ ├── logg.py # Логгирование
  │ ├── power.py # функции
  │ └── main.py # Основной класс 
  ├── tests/ # Тесты
  │ ├── init.py # Инициализация тестов
  │ └── test.py # Тесты калькулятора
  ├── requirements.txt
  ├── .gitignore
  ├── .pre-commit-config.yaml
  └── README.md
  </pre>
Алгоритм: программа считывает команду аргументы передает в функции они все выполняют
Реализованы команды 
Easy:
ls,cd,cat
сp,mv,rm
Логирование
Medium:
Архивы(zip/tar)
Поиск grep

Установка 
 ```bash
 $ python -m venv venv
 $ source venv/bin/activate
 
 $ pip install requirements.txt
 $ python -m src.main
```
