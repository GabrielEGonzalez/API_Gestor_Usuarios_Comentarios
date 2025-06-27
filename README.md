## 🚀 Proyecto Práctico: **Gestor de Usuarios y Comentarios de un Blog**

### 🎯 Objetivo:

Construir una API REST donde se puedan gestionar:

1. Usuarios registrados del blog
2. Comentarios que esos usuarios dejan en los artículos

---

### 🧱 Modelos:

#### 📌 Usuario

* `id`: int
* `nombre`: str
* `email`: EmailStr
* `direccion`: modelo anidado con ciudad, país, y zip
* `preferencias`: cookies opcionales

#### 📌 Comentario

* `id`: int
* `usuario_id`: int
* `post_id`: int
* `contenido`: str
* `fecha`: datetime (auto-generado)
* `estado`: "visible", "oculto", "eliminado"

---

### 📌 Endpoints:

#### Usuarios

| Método | Ruta             | Descripción                |
| ------ | ---------------- | -------------------------- |
| GET    | `/usuarios`      | Obtener todos los usuarios |
| GET    | `/usuarios/{id}` | Obtener usuario por ID     |
| POST   | `/usuarios`      | Crear usuario              |

#### Comentarios

| Método | Ruta                           | Descripción                      |
| ------ | ------------------------------ | -------------------------------- |
| GET    | `/comentarios`                 | Listar todos los comentarios     |
| GET    | `/comentarios/por-post/{post}` | Listar comentarios por post\_id  |
| POST   | `/comentarios`                 | Crear un nuevo comentario        |
| PUT    | `/comentarios/{id}`            | Actualizar el contenido o estado |
| DELETE | `/comentarios/{id}`            | Eliminar comentario              |


**árbol de carpetas recomendado** para tu **API de usuarios y comentarios** usando FastAPI + SQLAlchemy

---

## 🌲 Estructura de Carpetas

```
blog_api/
├── app/
│   ├── __init__.py
│   ├── main.py                  # Punto de entrada (crea el FastAPI app)
│   ├── models/                  # Modelos de SQLAlchemy
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── comment.py
│   ├── schemas/                 # Modelos Pydantic (entrada/salida)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── comment.py
│   ├── crud/                    # Lógica de base de datos (funciones)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── comment.py
│   ├── routes/                  # Rutas o endpoints (routers)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── comment.py
│   ├── database.py              # Conexión a la base de datos
│   └── config.py                # Configuración general (URI, settings, etc)
├── requirements.txt             # Dependencias
└── README.md                    # Explicación del proyecto
```

---

## 🔧 Archivos clave

### `main.py`

Registra todos los routers y ejecuta la app.

### `models/*.py`

Contiene tus clases de SQLAlchemy (`User`, `Comment`).

### `schemas/*.py`

Contiene tus clases de entrada/salida (`UserCreate`, `UserResponse`, `CommentCreate`, etc.)

### `crud/*.py`

Funciones como `create_user`, `get_user_by_id`, `add_comment`, etc.

### `routes/*.py`

Define las rutas (`/usuarios`, `/comentarios`, etc.)

### `database.py`

Inicializa SQLAlchemy (`engine`, `SessionLocal`, `Base`)

### `config.py`

Puedes definir aquí la `DATABASE_URL` y otras configuraciones como CORS, etc.

---