# Dataton-2023

Aquí tienes el texto en formato Markdown:

```markdown
## Desplegar un Proyecto Django con React

### 1. Instalar las Dependencias

Asegúrate de tener instalados Python, Django, Node.js y npm (o yarn) en tu sistema.

### 2. Configurar el Proyecto Django

#### a. Configurar el Entorno Virtual (Recomendado)

```bash
# Crear un entorno virtual
python -m venv myenv

# Activar el entorno virtual
source myenv/bin/activate  # Linux/macOS
myenv\Scripts\activate  # Windows

# Instalar Django
pip install django
```

#### b. Crear y Configurar el Proyecto Django

```bash
# Crear el proyecto Django
django-admin startproject myproject

# Entrar al directorio del proyecto
cd myproject

# Crear la aplicación Django
python manage.py startapp myapp
```

### 3. Configurar la Aplicación React

#### a. Crear la Aplicación React

```bash
# Crear la aplicación React en el directorio de la aplicación Django
npx create-react-app frontend
```

#### b. Configurar CORS (Cross-Origin Resource Sharing)

Para permitir que el servidor Django acepte solicitudes desde el servidor de desarrollo de React, instala y configura la aplicación django-cors-headers.

```bash
pip install django-cors-headers
```

Añade `'corsheaders.middleware.CorsMiddleware',` a `MIDDLEWARE` en `settings.py` y configura `CORS_ALLOWED_ORIGINS`.

### 4. Configurar la Integración de React y Django

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

### 5. Ejecutar Ambos Servidores

#### a. Iniciar el Servidor de Desarrollo de Django

```bash
python manage.py runserver
```

#### b. Iniciar el Servidor de Desarrollo de React

```bash
# En el directorio de la aplicación React
cd frontend

# Ejecutar el servidor de desarrollo de React
npm run start  # o yarn start
```

### 6. Acceder al Proyecto

Abre tu navegador y ve a http://localhost:8000 para acceder al proyecto Django. La aplicación React estará integrada y disponible en las rutas configuradas.

Ten en cuenta que este enfoque utiliza el servidor de desarrollo de React para el entorno de desarrollo. Para producción, deberías construir los archivos estáticos de React y configurar Django para servirlos estáticamente.
```
