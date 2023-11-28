# Nombre del Proyecto

Descripción breve del proyecto.

## Requisitos previos

- Python 3.x
- pip (gestor de paquetes de Python)
- [Opcional] Entorno virtual (recomendado)

## Clonar el Repositorio

```bash
git clone https://github.com/rinfasulasalle/django_api_backend.git
cd django_api_backend
```

## Configuración del Entorno Virtual [Opcional pero Recomendado]

```bash
# Instalar virtualenv si no está instalado
pip install virtualenv

# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Linux/Mac
source venv/bin/activate
# En Windows
venv\Scripts\activate
```

## Instalación de Dependencias

```bash
pip install -r requirements.txt
```

## Configuración de la Base de Datos

```bash
python manage.py migrate
```

## Crear un Superusuario [Opcional pero Recomendado]

```bash
python manage.py createsuperuser
```

## Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver localhost:3000
```

El servidor estará disponible en `http://localhost:3000/`. Puedes acceder al panel de administración en `http://localhost:3000/admin/` con las credenciales del superusuario.

## Contribuciones

Si quieres contribuir, sigue los pasos a continuación:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un Pull Request.
