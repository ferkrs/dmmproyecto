# Sistema de gestion para la DMM (Direccion Municipal de la mujer)
Requerimientos de instalacion 
* Instalacion de [PYTHON](https://www.python.org/community-landing/) version 3.8.8 recomendada. 
* Instalacion de [MYSQL](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04) guia de instalacion para ubuntu. 
* Instalacion de [PIP](https://pip.pypa.io/en/stable/) en la version mas estable.
* Instalacion de [VIRTUALENVWRAPPER](https://pypi.org/project/virtualenvwrapper/), disponible para linux, windows o Mac Os.
* Instalacion de [GIT](https://git-scm.com/downloads) version estable.

# Instalacion del sistema
Paso 1: Clonar el repositorio

```
git clone https://github.com/ferkrs/dmmproyecto.git
cd dmmproyecto
```
Paso 2: Crear el entorno virtual

```
mkvirtualenv dmm // para crear el entorno 
workon // para listar los entornos
workon dmm // para iniciar el entorno
```
Paso 3: Instalar los requerimientos

```
pip install -r requirements.txt
pip3 install -r requirements.txt // en caso de tener la version 3 usar pip3 
```
Paso 4: Correr las migraciones

```
./manage.py makemigrations
./manage.py migrate
```
Paso 5: Crear SuperUsuario
```
./manage.py createsuperuser
```
Paso 6: Levantar el servidor
```
./manage.py runserver
```
