---

````markdown
# 🚀 API Gestor de Usuarios y Comentarios de Blog

Una API REST construida con **FastAPI** para gestionar usuarios y comentarios de un blog. Permite crear usuarios, asociar comentarios a publicaciones y manejar el estado de los mismos.

---

## 🎯 Objetivo

Crear una API funcional para:

- 📌 Registrar y consultar **usuarios** del blog
- 💬 Gestionar los **comentarios** que esos usuarios dejan en artículos

---

## 🧱 Modelos

### 👤 Usuario

| Campo         | Tipo     | Descripción                          |
|---------------|----------|--------------------------------------|
| `id`          | int      | Identificador único del usuario      |
| `nombre`      | str      | Nombre del usuario                   |
| `email`       | EmailStr | Correo electrónico                   |
| `direccion`   | objeto   | Ciudad, país y código postal         |
| `preferencias`| dict (opcional) | Preferencias vía cookies      |

### 💬 Comentario

| Campo        | Tipo     | Descripción                          |
|--------------|----------|--------------------------------------|
| `id`         | int      | Identificador del comentario         |
| `usuario_id` | int      | ID del usuario que comenta           |
| `post_id`    | int      | ID del post al que se comenta        |
| `contenido`  | str      | Texto del comentario                 |
| `fecha`      | datetime | Fecha de creación (auto-generado)    |
| `estado`     | str      | `"visible"`, `"oculto"`, `"eliminado"` |

---

## 🔗 Endpoints Principales

### Usuarios

| Método | Ruta             | Descripción                |
|--------|------------------|----------------------------|
| GET    | `/usuarios`      | Obtener todos los usuarios |
| GET    | `/usuarios/{id}` | Obtener un usuario por ID  |
| POST   | `/usuarios`      | Crear un nuevo usuario     |

### Comentarios

| Método | Ruta                            | Descripción                         |
|--------|----------------------------------|-------------------------------------|
| GET    | `/comentarios`                  | Listar todos los comentarios        |
| GET    | `/comentarios/por-post/{post}`  | Listar comentarios por `post_id`    |
| POST   | `/comentarios`                  | Crear un nuevo comentario           |
| PUT    | `/comentarios/{id}`             | Actualizar contenido o estado       |
| DELETE | `/comentarios/{id}`             | Eliminar comentario (soft delete)   |

---

## 🌲 Estructura del Proyecto

```bash
blog_api/
├── app/
│   ├── main.py                  # Punto de entrada FastAPI
│   ├── models/                  # Modelos SQLAlchemy
│   │   ├── user.py
│   │   └── comment.py
│   ├── schemas/                 # Modelos Pydantic (I/O)
│   │   ├── user.py
│   │   └── comment.py
│   ├── crud/                    # Funciones CRUD
│   │   ├── user.py
│   │   └── comment.py
│   ├── routes/                  # Rutas (routers)
│   │   ├── user.py
│   │   └── comment.py
│   ├── database.py              # Conexión a DB
│   └── config.py                # Config global (URI, CORS, etc)
├── requirements.txt             # Dependencias
└── README.md                    # Documentación
````

---

## ⚙️ Tecnologías Usadas

* ⚡ **FastAPI** – Framework para APIs modernas
* 🐘 **SQLAlchemy** – ORM para base de datos
* 📄 **Pydantic** – Validación y serialización
* 🐍 **Python 3.11+**
* 🛢️ **SQLite / MySQL**
* 🧪 **Swagger UI / ReDoc** – Documentación automática

---

## 🧪 Pruebas

Puedes probar la API desde:

* Swagger: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`
* Postman: (próximamente incluir colección .json en el repositorio)

---

## 🛠️ Instalación y Ejecución Local

1. Clona el proyecto:

   ```bash
   git clone https://github.com/GabrielEGonzalez/API_Gestor_Usuarios_Comentarios.git
   cd API_Gestor_Usuarios_Comentarios
   ```

2. Crea un entorno virtual (opcional):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta el servidor:

   ```bash
   uvicorn app.main:app --reload
   ```

5. Abre en navegador:

   * Swagger: `http://127.0.0.1:8000/docs`
   * ReDoc: `http://127.0.0.1:8000/redoc`

---
## 🚀 Despliegue (próximo paso)
---

## 📬 Autor

**Gabriel E. González**
📂 GitHub: [@GabrielEGonzalez](https://github.com/GabrielEGonzalez)
📫 Contacto: [gabriel.ejemplo@email.com](mailto:enriquegonzalez123467@gmail.com)

---

## 📝 Estado del Proyecto

> 🟢 Fase actual: API funcional completa
> 🔵 Próximos pasos: pruebas, documentación externa y despliegue

---

## ❤️ Contribuciones

¿Quieres contribuir o dejar sugerencias?
¡Crea un `issue` o `pull request` en este repositorio!

---
