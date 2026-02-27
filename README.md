# WebSocket Rooms - Django Channels Project

## 📋 Descripción
WebSocket Rooms es una aplicación web en tiempo real construida con Django y Django Channels que permite la creación y gestión de salas de comunicación WebSocket. Los usuarios pueden crear salas, conectarse como master o slave, y enviar comandos en tiempo real.

## ✨ Características Principales
- **Autenticación de usuarios**: Sistema de login/logout integrado
- **Gestión de salas**: Crear y eliminar salas de comunicación
- **Dos roles de conexión**:
  - **Master**: Puede enviar comandos a la sala
  - **Slave**: Solo puede recibir comandos
- **Tokens únicos**: Cada sala genera tokens automáticos para master y slave
- **Comunicación en tiempo real**: Uso de WebSockets para comunicación bidireccional
- **Interfaz moderna**: UI responsive con animaciones CSS

## 🚀 Tecnologías Utilizadas
- **Backend**: Django 4.x
- **WebSockets**: Django Channels + Daphne
- **Base de datos**: SQLite (por defecto) / PostgreSQL (producción)
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Autenticación**: Sistema de auth de Django

## 📁 Estructura del Proyecto
```
websocket_project/
├── manage.py
├── websocket_project/
│   ├── __init__.py
│   ├── asgi.py          # Configuración ASGI para Channels
│   ├── settings.py      # Configuración del proyecto
│   └── urls.py          # URLs principales
├── rooms/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py        # Modelo Room
│   ├── urls.py          # URLs de la app rooms
│   ├── views.py         # Vistas de la app
│   └── templates/
│       └── rooms/
│           └── index.html
└── requirements.txt
```

## 🔧 Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- pip (gestor de paquetes de Python)
- virtualenv (recomendado)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone <url-del-repositorio>
cd websocket_project
```

2. **Crear y activar entorno virtual**
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
# o
env\Scripts\activate  # Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar la base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

6. **Ejecutar el servidor**
```bash
DJANGO_SETTINGS_MODULE=websocket_project.settings daphne -b 0.0.0.0 -p 8000 websocket_project.asgi:application
```

## 📦 Dependencias Principales
```
Django>=4.0.0
channels>=4.0.0
daphne>=4.0.0
```

## 🎮 Uso de la Aplicación

### 1. **Autenticación**
- Accede a `http://localhost:8000`
- Inicia sesión con tus credenciales
- Serás redirigido al dashboard principal

### 2. **Gestión de Salas**
- **Crear sala**: Ingresa un nombre y haz clic en "Create Room"
- **Eliminar sala**: Haz clic en el botón "Delete" de cualquier sala
- Las salas inactivas se ocultan automáticamente

### 3. **Conexión WebSocket**
- **Como Master**: Usa el botón "👑 Master" - Tendrás permisos para enviar comandos
- **Como Slave**: Usa el botón "🔧 Slave" - Solo podrás recibir comandos
- Una vez conectado, puedes:
  - Ver el estado de la conexión en tiempo real
  - Enviar comandos (solo master)
  - Visualizar mensajes y comandos en el panel
  - Desconectarte manualmente

## 🔌 API Endpoints

### Endpoints REST
- `GET /rooms/` - Lista de salas activas
- `POST /rooms/create/` - Crear nueva sala
- `DELETE /rooms/delete/<room_name>/` - Eliminar sala

### WebSocket Endpoint
- `ws://<server_url>/ws/room/<room_name>/<token>/`

## 🗄️ Modelo de Datos

### Room
| Campo | Tipo | Descripción |
|-------|------|-------------|
| name | CharField | Nombre único de la sala |
| master_token | CharField | Token para conexión master |
| slave_token | CharField | Token para conexión slave |
| created_at | DateTimeField | Fecha de creación |
| is_active | BooleanField | Estado de la sala |

## 🎨 Características de la Interfaz

### Panel Principal
- Header con información del usuario y botón de logout
- Sección para creación de nuevas salas
- Grid de salas activas con tarjetas interactivas
- Panel de conexión WebSocket con indicadores de estado

### Indicadores Visuales
- **Puntos de estado**: Muestran conexión activa y rol actual
- **Animaciones**: Transiciones suaves y efectos hover
- **Diseño responsive**: Adaptable a dispositivos móviles
- **Feedback visual**: Mensajes de sistema y timestamps

## 🔒 Seguridad
- Autenticación requerida para todas las operaciones
- Tokens únicos por sala y rol
- Protección CSRF en peticiones POST
- Las salas inactivas no son accesibles

## ⚡ Rendimiento
- Servidor ASGI con Daphne para manejo eficiente de WebSockets
- Conexiones persistentes y bidireccionales
- Escalable horizontalmente

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## ✒️ Autor
[Tu Nombre]

## 🎁 Características Planificadas
- [ ] Salas privadas con contraseña
- [ ] Historial de mensajes persistente
- [ ] Múltiples slaves por sala
- [ ] Comandos predefinidos
- [ ] Notificaciones en tiempo real
- [ ] Estadísticas de uso

---
**Nota**: Este proyecto demuestra la implementación de WebSockets con Django Channels para comunicación en tiempo real. Diseñado para ser educativo y fácilmente extensible.
