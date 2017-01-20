## Instrucciones de uso

Para montar un entorno de desarrollo utilizar virtualenv
```
virtualenv /venv
source /venv/bin/activate
```

Instalar las dependencias
```
pip install -r requirements.txt
```
Configurar las BBDD y archivos estáticos
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_data
python manage.py collectstatic
```

Para utilizar docker se necesita docker-compose
Compilar el proyecto y arrancar.
```
docker-compose build
docker-compose up -d
```

Instalar la BBDD y los datos iniciales (solo si se usa una BBDD como MySQL) si
no se han realizado anteriormente
```
docker exec -ti restapi_webapp_1 python manage.py makemigrations
docker exec -ti restapi_webapp_1 python manage.py migrate
docker exec -ti restapi_webapp_1 python manage.py loaddata initial_data
```

Ya podemos acceder desde la url de acceso al puerto 80.

Las URL son: 
/students/
/courses/
/courses/email_view/
/registrations/

# Notas sobre la calidad de código

Podemos lanzar los test unitarios y funcionales con el siguiente comando.
Así mismo podemos ver la cobertura de los tests y la calidad del código
```
docker exec -ti restapi_webapp_1 python manage.py test
docker exec -ti restapi_webapp_1 coverage run --source='.' manage.py test
docker exec -ti restapi_webapp_1 coverage report
docker exec -ti restapi_webapp_1 flake8 .
docker exec -ti restapi_webapp_1 pylint --load-plugins="pylint_django" learning_cooking
```

Notas sobre los modelos:

He agregado el campo e-mail en alumno para que haya una clave única que
identifique a dicho alumno.

He creado el modelo "Inscripción" como una tabla con claves foráneas, podría
haberlo realizado como un campo many2many de cursos, pero de esta forma se crea
igual en la BBDD y ayuda a la hora de desarrollar la inscripción en la API.
Tambien he creido conveniente crear la fecha de matriculación a dicho curso.