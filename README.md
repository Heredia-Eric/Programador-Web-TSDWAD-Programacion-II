# Backend - Django y DRF | Programación II

Este repositorio contiene el desarrollo práctico propuesto por el espacio curricular de **Programación II**, perteneciente al módulo **Programador Web** de la **Tecnicatura Superior en Desarrollo Web y Aplicaciones Digitales (TSDWAD)** del **ISPC**.

El objetivo del desafío es aproximarse a los fundamentos de **Django** y **Django REST Framework (DRF)** para la creación de una API robusta y escalable.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Framework Web:** Django
* **API Framework:** Django REST Framework (DRF)
* **Base de Datos:** SQLite (Configurada según requerimiento de clase para facilitar la portabilidad).
* **Entorno Virtual:** venv

## 🚀 Proceso de Desarrollo
El proyecto fue construido siguiendo la metodología propuesta en el material teórico de la cátedra, aplicando los siguientes pasos:

1.  **Configuración del Entorno:** Creación de entorno virtual e instalación de dependencias necesarias.
2.  **Arquitectura MTV:** Configuración del corazón del proyecto y creación de una aplicación modular.
3.  **Modelado de Datos:** Implementación de modelos para `Categoría` y `Producto` con relaciones de clave foránea.
4.  **Persistencia en SQLite:** A diferencia del material original enfocado en PostgreSQL, se optó por **SQLite** por pedido docente, garantizando que la base de datos sea un archivo local autogestionado.
5.  **Capa de Serialización:** Creación de traductores de datos (Serializers) para transformar objetos complejos en formato JSON.
6.  **Endpoints de API:** Implementación de `ViewSets` y `Routers` para habilitar las operaciones CRUD.
7.  **Lógica Especial:** Se añadió una funcionalidad extra para la **Actualización Global de Precios**, permitiendo aplicar aumentos porcentuales de forma masiva a todos los registros.


## ⚙️ Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Heredia-Eric/Programador-Web-TSDWAD-Programacion-II.git]
2. **Crear y activar el entorno virtual:**
    python -m venv env
    **En Windows:**
    env\Scripts\activate
    **En Mac/Linux:**
    source env/bin/activate
3. **Instalación de dependencias:**
    pip install -r requirements.txt
4. **Ejecutar migraciones:**
    python manage.py migrate
4. **Iniciar el servidor:**
    python manage.py runserver

Autor: **Eric Heredia**
