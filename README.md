
# Tienda - Proyecto Integrador (Etapa 1)

## Descripción general
Este proyecto es una **tienda online básica** desarrollada con **Django** como parte de un proyecto integrador con fines educativos.  
En esta primera etapa, se construyó la **estructura base del sitio**, incluyendo la configuración del entorno, la creación de una app llamada `shop`, el sistema de templates, archivos estáticos y la conexión del servidor local.  

---

##  Objetivos de la Etapa 1
- Crear el entorno de desarrollo virtual.  
- Iniciar el proyecto Django y la aplicación `shop`.  
- Configurar la estructura de carpetas (`templates` y `static`).  
- Agregar un logo y las vistas `index` y `contacto`.  
- Verificar el funcionamiento en el servidor local.  
- Subir el proyecto correctamente a **GitHub**.  

---

##  Tecnologías utilizadas
- Python 3.10 o superior**
- pip (administrador de paquetes)
- Virtualenv (entorno virtual)
- Django 5.x

---

## ⚙️ Instalación y ejecución


### 1. Clonar el repositorio

git clone https://github.com/Valeria.py/tienda-project.git
cd tienda-project

### 2. Crear entorno virtual

python -m venv venv

### 3. Activar entorno virtual
En Windows (Git Bash) > source venv/Scripts/activate
En Linux/Mac > source venv/bin/activate

### 4. Instalar dependencias

pip install -r requirements.txt

### 5. Ejecutar el servidor

python manage.py runserver
Abrí en el navegador:

http://127.0.0.1:8000/shop/
http://127.0.0.1:8000/shop/contacto/

### Estructura de archivos (Etapa 1)

tienda_project/
│
├── manage.py
├── tienda/                 # Configuración principal del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── shop/                   # Aplicación principal
│   ├── templates/
│   │   └── shop/
│   │       ├── base.html
│   │       ├── index.html
│   │       └── contacto.html
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── static/
│   └── shop/
│       └── logo.png
│
├── .gitignore
├── requirements.txt
└── README.md

### Detalles técnicos de la Etapa 1

Se configuraron las rutas principales:

/shop/ → Página de inicio

/shop/contacto/ → Página de contacto

Se añadió un logo en la carpeta static/shop/logo.png, visible en el encabezado de todas las páginas.

Las plantillas usan herencia (base.html) y bloques de contenido ({% block content %}) para mantener consistencia entre páginas.

El logo redirige al inicio usando:

<a href="{% url 'index' %}">
    <img src="{% static 'shop/logo.png' %}" alt="Logo" style="height:80px;">
</a>

### Git y control de versiones

Repositorio remoto:
https://github.com/Valeria.py/tienda-project


### Estado actual

✅ Proyecto funcionando en servidor local
✅ Estructura de templates y estáticos creada
✅ Logo agregado correctamente
✅ Subido a GitHub
