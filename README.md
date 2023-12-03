# Dataton
---
## Desplegar un Proyecto Django con React

### 1. Instalar las Dependencias

Asegúrate de tener instalados Python, Django y Node.js en tu sistema.

### 2. Configurar la Aplicación React

#### a. Instalar las Dependencias de React

```bash
# En el directorio de la aplicación React
cd frontend

# Instalar las dependencias de React
npm install
```

#### b. Configurar CORS (Cross-Origin Resource Sharing)

Para permitir que el servidor Django acepte solicitudes desde el servidor de desarrollo de React, instala y configura la aplicación `django-cors-headers`.

```bash
pip install django-cors-headers
```

Añade `'corsheaders.middleware.CorsMiddleware',` a `MIDDLEWARE` en `settings.py` y configura `CORS_ALLOWED_ORIGINS`.

### 3. Configurar la Integración de React y Django

#### a. Configurar las Rutas en Django

Actualiza las rutas en `urls.py` para manejar las vistas de React:

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
```

#### b. Configurar la Ruta de Construcción de React

Crea un archivo `index.html` en la carpeta de plantillas de Django (por ejemplo, `templates`) que se usará como plantilla principal. Este archivo debe incluir la referencia al archivo JavaScript generado por React.

### 4. Ejecutar Ambos Servidores

#### a. Iniciar el Servidor de Desarrollo de Django

```bash
python manage.py runserver
```

#### b. Iniciar el Servidor de Desarrollo de React

```bash
# En el directorio de la aplicación React
cd frontend

# Ejecutar el servidor de desarrollo de React
npm run dev
```

### 5. Acceder al Proyecto

Abre tu navegador y ve a http://localhost:8000 para acceder al proyecto Django. La aplicación React estará integrada y disponible en las rutas configuradas.

Ten en cuenta que este enfoque utiliza el servidor de desarrollo de React para el entorno de desarrollo. Para producción, deberías construir los archivos estáticos de React y configurar Django para servirlos estáticamente.
```
