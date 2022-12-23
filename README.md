# proyecto-informatorio

### Desarrollo de un blog para los bomberos de la localidad de San Martin.

#### Descripcion del proyecto:

Este proyecto fue propuesto como trabajo final de la segunda etapa del Informatorio. 
Tuvo como objetivo aplicar todo lo aprendido en la segunda etapa del informatorio sobre Python, bases de datos y django.

#### Tecnologias utilizadas:

- Base de datos: Mysql
- Lenguaje: Python
- Framework: django

#### Video demo del Blog:

https://user-images.githubusercontent.com/110850490/209404047-67a9c0f5-e7eb-4e8b-a318-8c438464148b.mp4

#### Link del Blog:

https://info2022.pythonanywhere.com/

***para ejecutar el proyecto:***

1. clonar el repositorio (ubicarse en la carpeta que se desee y desde el cmd ejecutar ```git clone https://github.com/RamaAlves/proyecto-informatorio.git``` )
2. ubicarse en la carpeta del proyecto y mediante el cmd ejecutar ```virtualenv env```
3. activar el entorno virtual creado ```env/Scripts/activate```
4. instalar los requeriments ```pip install -r requeriments.txt```
5. modificar el archivo manage.py para que utilice los settings/local en vez de los settings/produccion y poder correrlo en local
6. dirigirse a la carpeta del proyecto y una ves en ella desde el cmd ejecutar  ```python manage.py makemigrations``` 
7. Luego ```python manage.py migrate```
8. Ahora ya puede ejecutar el proyecto en local con el siguiente comando ```python manage.py runserver```
