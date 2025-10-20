# Tienda - Proyecto Integrador

## Etapa 1

### Descripción general
Este proyecto es una tienda online básica desarrollada con Django como parte de un proyecto integrador con fines educativos.  
En esta primera etapa se construyó la estructura base del sitio, incluyendo la configuración del entorno, la creación de una app llamada `shop`, el sistema de templates, archivos estáticos y la conexión del servidor local.

### Objetivos de la Etapa 1
- Crear el entorno de desarrollo virtual.
- Iniciar el proyecto Django y la aplicación `shop`.
- Configurar la estructura de carpetas (`templates` y `static`).
- Agregar un logo y las vistas `index` y `contacto`.
- Verificar el funcionamiento en el servidor local.
- Subir el proyecto correctamente a GitHub.

### Tecnologías utilizadas
- Python 3.13.2
- pip (administrador de paquetes)
- Virtualenv (entorno virtual)
- Django 5.2.7

### Instalación y ejecución
1. Clonar el repositorio:
git clone https://github.com/Valeria.py/tienda_project.git
cd tienda_project
2. Crear entorno virtual:
python -m venv venv

3. Activar entorno virtual:
Windows (Git Bash):
source venv/Scripts/activate

Linux/Mac:
source venv/bin/activate

4. Instalar dependencias:
pip install -r requirements.txt

5. Ejecutar el servidor:
python manage.py runserver

6. Abrir en el navegador:

Página de inicio: http://127.0.0.1:8000/shop/

Página de contacto: http://127.0.0.1:8000/shop/contacto/

Estructura de archivos (Etapa 1)

tienda_project/
├── manage.py
├── tienda/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── shop/
│   ├── templates/shop/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── contacto.html
│   ├── views.py
│   ├── urls.py
│   └── ...
├── static/shop/logo.png
├── .gitignore
├── requirements.txt
└── README.md

### Detalles técnicos de la Etapa 1:

Rutas principales configuradas:

/shop/ → Página de inicio

/shop/contacto/ → Página de contacto

Logo agregado en static/shop/logo.png, visible en el encabezado de todas las páginas.

Templates usan herencia (base.html) y bloques de contenido ({% block content %}) para mantener consistencia.

El logo redirige al inicio con <a href="{% url 'index' %}">.

Git y control de versiones
Repositorio remoto: https://github.com/Valeria.py/tienda_project

### Estado actual
Proyecto funcionando en servidor local.

Estructura de templates y estáticos creada.

Logo agregado correctamente.

Subido a GitHub.

## Etapa 2
Descripción general
En esta etapa se agregaron formularios y modelos para administrar un catálogo (sólo de remeras para facilitar la tarea), permitiendo que los administradores carguen nuevas remeras y que se muestren en la página de inicio.

### Objetivos de la Etapa 2
Crear modelo Remera con campos:

marca (Texto)

talle (Opciones: XS, S, M, L, XL, XXL)

color (Texto)

lisa (Boolean)

genero (Opciones: Hombre, Mujer, Unisex)

Aplicar migraciones correspondientes.

Crear formulario RemeraForm usando ModelForm.

Crear vistas:

index: mostrar catálogo completo de remeras.

nueva_remera: formulario GET/POST para ingresar nuevas remeras.

Agregar template nueva_remera.html con formulario.

Actualizar template index.html para mostrar tabla de catálogo y enlaces al final.

Configurar URL /shop/nueva-remera/.

### Tecnologías utilizadas
Django ORM para modelos

Django Forms para formularios

Plantillas Django ({% extends %} y {% block %})

### Instalación y ejecución
1. Abrir servidor local como en Etapa 1.

2. Navegar a /shop/nueva-remera/ para agregar nuevas remeras.

3. Verificar que la tabla de catálogo se actualice automáticamente en la página de inicio.

### Flujo de Git
1. Creación de rama para no comprometer la rama main:

git checkout -b etapa2-remeras

Pruebas en shell de Django

Merge a main:

git checkout main
git merge etapa2-remeras
git push origin main
Commit vacío opcional para documentación:

git commit --allow-empty -m "Merge completado desde rama etapa2-remeras (práctica de trabajo con ramas y commits)"
git push origin main

Pruebas realizadas
Creación de objetos Remera en shell:

python

from shop.models import Remera
r = Remera(marca="Nike", talle=3, color="Negro", lisa=True, genero=3)
r.save()
Remera.objects.all()
Verificación de formulario RemeraForm y guardado de datos.

Visualización de tabla de catálogo en index.html.

### Estado actual
Proyecto funcionando en servidor local.

Formularios y modelo de remeras funcionando.

Tabla de catálogo visible en index.html.

Todas las etapas subidas a GitHub y documentadas.

Licencia
MIT License

Copyright (c) 2025 Valeria Echeveste

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.