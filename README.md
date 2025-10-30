
---

# Tienda - Proyecto Integrador

## Etapa 1 - Configuración inicial

**Descripción:**
Este proyecto es una tienda online básica desarrollada con Django como parte de un proyecto integrador educativo. En esta etapa se construyó la estructura base del sitio.

**Objetivos:**

* Crear entorno virtual de desarrollo.
* Iniciar proyecto Django y app `shop`.
* Configurar estructura de carpetas (`templates`, `static`).
* Agregar logo y vistas `index` y `contacto`.
* Verificar funcionamiento en servidor local.
* Subir proyecto a GitHub.

**Tecnologías:**

* Python 3.13.2
* pip
* Virtualenv
* Django 5.2.7

**Instalación y ejecución:**

```bash
git clone https://github.com/Valeriapy/tienda_project.git
cd tienda_project
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate    # Linux/Mac
pip install -r requirements.txt
python manage.py runserver
```

**URLs principales:**

* Inicio: [http://127.0.0.1:8000/shop/](http://127.0.0.1:8000/shop/)
* Contacto: [http://127.0.0.1:8000/shop/contacto/](http://127.0.0.1:8000/shop/contacto/)

**Estructura de archivos:**

```
tienda_project/
├── manage.py
├── tienda/
│   ├── settings.py
│   └── urls.py
├── shop/
│   ├── templates/shop/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── contacto.html
│   ├── views.py
│   └── urls.py
├── static/shop/logo.png
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Etapa 2 - Modelo y formulario de remeras

**Descripción:**
Se agregan modelos y formularios para administrar un catálogo de remeras.

**Objetivos:**

* Crear modelo `Remera` con campos:

  * `marca` (Texto)
  * `talle` (Opciones: XS, S, M, L, XL, XXL)
  * `color` (Texto)
  * `lisa` (Boolean)
  * `genero` (Opciones: Hombre, Mujer, Unisex)
* Aplicar migraciones correspondientes.
* Crear formulario `RemeraForm` usando `ModelForm`.
* Crear vistas:

  * `index`: mostrar catálogo completo de remeras.
  * `nueva_remera`: formulario GET/POST para ingresar nuevas remeras.
* Agregar template `nueva_remera.html`.
* Actualizar `index.html` para mostrar tabla de catálogo.
* Configurar URL `/shop/nueva-remera/`.

**Pruebas:**

* Crear objetos `Remera` desde shell.
* Verificar guardado mediante `RemeraForm`.
* Visualización correcta de la tabla en `index.html`.

---

## Etapa 3.1 - Optimización con ModelForm

**Descripción:**
Se mejora el formulario de remeras usando `ModelForm` y tipos de datos adecuados.

**Objetivos:**

* Reemplazar campos `talle` y `genero` por `PositiveSmallIntegerField`.
* Crear `FormularioRemera` basado en `ModelForm`.
* Ajustar vista que procesa datos del formulario.
* Eliminar `required=False` en modelo para `lisa`.
* Aplicar migraciones correspondientes.

**Resultado:**
Formulario más limpio, código más compacto y tipos de datos optimizados.

---

## Etapa 3.2 - Uso exclusivo del Administrador de Django

**Descripción:**
Se centraliza la gestión de remeras usando el **admin de Django**, eliminando formularios y vistas personalizadas.

**Cambios principales:**

* Eliminación de la vista `nueva_remera()` y plantilla `nueva_remera.html`.
* Registro del modelo `Remera` en el administrador:

```python
from django.contrib import admin
from .models import Remera

@admin.register(Remera)
class RemeraAdmin(admin.ModelAdmin):
    list_display = ('marca', 'get_talle_display', 'color', 'lisa', 'get_genero_display')
    list_filter = ('talle', 'genero', 'lisa')
    search_fields = ('marca', 'color')
```

* Uso de `get_talle_display()` y `get_genero_display()` para mostrar valores legibles.
* Configuración de idioma español (`LANGUAGE_CODE = 'es'` en `settings.py`).

**Resultado:**

* La creación, edición y eliminación de remeras se realiza únicamente desde el **administrador de Django**.
* La página principal muestra el catálogo correctamente.

---

## Estado actual

* Proyecto funcionando en servidor local.
* Todas las etapas documentadas y subidas a GitHub.
* Licencia MIT incluida.

---