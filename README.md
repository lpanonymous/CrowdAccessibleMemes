# CrowdsourcingMemes

Sistema web Django para la descripción de plantillas de memes.

## Comenzando 🚀

Estas instrucciones te permitiran probar el proyecto localmente.


### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
1.-Visual Studio Code.
2.-Una base de datos en Xampp llamada memesaccesibles
3.-Una cuenta en Google Cloud habilitando el api de GoogleDrive
```

### Instalación 🔧

```
1.- Descargar el codigo.
2.- En Google Cloud Platform generar un archivo token.json donde contenga las credenciales de acceso a las apis habilitadas de google.
3.- Guardar el archivo token en la carpeta settings del proyecto.
4.- En el archivo models.py del proyecto modificar el correo electronico que viene por defecto para ver las imagenes guardadas.
5.- Abrir el proyecto con Visual Studio Code.
6.- En el directorio del proyecto ubicar el archivo requeriments.txt y en terminal ejecutar: pip install -r requirements.txt
7.- Habilitar apache y mysql en xampp
8.- En terminal ejecutar el comando: python manage.py makemigrations
9.- En terminal ejecutar el comando: python manage.py migrate
10.- Para crear la cuenta de administrador en terminal ejecutar el comando: python manage.py createsuperuser e ingresar los datos que se piden
11.- En terminal ejecutar el comando: python manage.py runserver 0.0.0.0:8000
```

## Ejecutando las pruebas ⚙️
<h3>1.- Acceso al sistema web</h3>
<img src="https://http2.mlstatic.com/D_NQ_NP_845361-MLM42753973203_072020-O.jpg" alt="Página principal" width=800px height=500px/>

   
## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Visual Studio Code](https://code.visualstudio.com/download) - El editor de codigo.
* [Xampp](https://www.apachefriends.org/download.html) - Para la base de datos mysql.
* [Google Drive Api](https://developers.google.com/drive) - Api para almacenar las imagenes.
* [Django](https://www.djangoproject.com/) - Framework de desarrollo de aplicaciones web con python.

## Versionado 📌

Usamos [GitHub](https://github.com/lpanonymous/CrowdAccessibleMemes.git) para el versionado.

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **LUIS PABLO REYES FERNÁNDEZ**- *Trabajo Inicial* - [lpanonymous](https://github.com/lpanonymous/MemesToText.git)
* **ROJANO CÁCERES JOSE RAFAEL**[tareasR](https://github.com/tareasR)

