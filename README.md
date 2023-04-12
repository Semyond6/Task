1. Проект выполнен на docker-compose. Для запуска проекта необходимо скопировать проект и выполнить команду:

docker-compose up -d --build

Для проверки работоспособности можно воспользоваться SwaggerUI по адресу: 

http://localhost:8000/docs

2. Скрипт для выполнения задания о переносе данных статуса из таблицы short_names в таблицу full_names.
Поля name были созданы с указанием того, что они являются индексами.

UPDATE "full_names" as f SET status = s.status 
FROM "short_names" as s 
WHERE split_part(f.name, '.', 1) = s.name;