# Запуск задач через Docker

В репозитории три задачи: `task1`, `task2`, `task3`. Каждая запускается отдельно через Docker.

## Клонирование проекта

```bash
git clone https://github.com/nezhdanchik/student-olymp.git
cd student-olymp
```

## Запуск задач

### Задача 1

```bash
cd task1
docker build -t task1-app .
docker run task1-app
```

### Задача 2

```bash
cd task2
docker build -t task2-app .
docker run task2-app
```

### Задача 3

```bash
cd task3
docker build -t task3-app .
docker run task3-app
```