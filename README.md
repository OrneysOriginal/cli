### Запуск через консоль
```
python main.py <ваши файлы> --report <отчёт>
```
Пример:
```
python main.py app1.log app2.log --report handlers
```
Любое название отчёта кроме handlers будет, восприниматься как неверное название.
Программа создаст в своей директории отчёт, с названием handlers

### Тестирование
```
pytest --cov=src test
```
Выведет в консоль покрытие тестами файла src


Константа PROCESS_COUNT указывает сколько процессов будет включено в задачу