# Клонирование проекта

```bash
git clone https://github.com/nezhdanchik/student-olymp.git
cd student-olymp
```
### Задача 2

```bash
docker build -t task2-app .
docker run --name my-task task2-app
```
После завершения работы контейнера
```bash
docker cp my-task:/app/success_ip.txt ./file.txt
```
Результирующий файл появится в текущей директории под названием file.txt