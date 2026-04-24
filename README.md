# 🍯 Plataforma de Telemetría para Honeypot

> Proyecto Final – Fuentes de Datos  
> Plataforma replicable y orientada a análisis de datos construida con **Cowrie**, **Docker Compose**, **FastAPI**, **PostgreSQL** y **Streamlit**.

---

## 📌 Descripción general

Este proyecto simula un entorno controlado de engaño defensivo (*deception defense*): despliega un honeypot SSH/Telnet, captura la telemetría generada por interacciones sospechosas, la almacena en una base de datos relacional, la expone mediante una API REST y la visualiza en un dashboard interactivo.

El enfoque es académico y seguro: en lugar de herramientas ofensivas, el proyecto demuestra cómo la telemetría de ciberseguridad puede tratarse como una **fuente de datos** para extracción, transformación, almacenamiento y análisis.

---

## 🏗️ Arquitectura

```
Atacante / Bot
      │
      ▼
  [COWRIE]          Honeypot SSH/Telnet — genera logs JSON
      │
      ▼
  [FastAPI]         API REST — recibe, valida y persiste eventos
      │
      ▼
 [PostgreSQL]       Base de datos relacional — almacenamiento estructurado
      │
      ▼
  [Streamlit]       Dashboard — visualización de métricas y eventos
```

### Quantas de arquitectura

| Quantum | Servicios | Responsabilidad |
|---|---|---|
| **Captura** | Cowrie | Simular servicios vulnerables y generar telemetría raw |
| **Procesamiento** | FastAPI + PostgreSQL | Ingesta, validación y persistencia de eventos |
| **Visualización** | Streamlit | Consulta y presentación de métricas agregadas |

---

## 🧰 Stack tecnológico

| Tecnología | Rol |
|---|---|
| [Cowrie](https://github.com/cowrie/cowrie) | Honeypot de interacción media (SSH/Telnet) |
| [FastAPI](https://fastapi.tiangolo.com/) | Capa de API REST con documentación OpenAPI automática |
| [PostgreSQL 15](https://www.postgresql.org/) | Almacenamiento relacional de eventos |
| [Streamlit](https://streamlit.io/) | Dashboard de visualización interactiva |
| [Docker Compose](https://docs.docker.com/compose/) | Orquestación de todos los servicios |
| [Python 3.10+](https://www.python.org/) | Lenguaje base del backend y dashboard |

---

## 📁 Estructura del repositorio

```
honeypot-project/
├── api/
│   ├── Dockerfile
│   ├── main.py               # Endpoints FastAPI
│   ├── requirements.txt
│   └── tests/
│       └── test_main.py      # Pruebas con pytest
├── dashboard/
│   ├── Dockerfile
│   ├── app.py                # Dashboard Streamlit
│   └── requirements.txt
├── db/
│   └── init.sql              # Esquema inicial de la base de datos
├── docs/
│   ├── adr/
│   │   ├── ADR-001-eleccion-honeypot-cowrie.md
│   │   ├── ADR-002-postgres-almacenamiento.md
│   │   ├── ADR-003-fastapi-capa-api.md
│   │   └── ADR-004-streamlit-dashboard.md
│   ├── openapi.json          # Especificación OpenAPI exportada
│   └── quantas.md            # Documento de architecture quantas
├── .github/
│   └── workflows/
│       └── ci.yml            # Pipeline de CI/CD con GitHub Actions
├── compose.yaml
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Requisitos previos

- [Docker](https://docs.docker.com/get-docker/) >= 24.x
- [Docker Compose](https://docs.docker.com/compose/install/) >= 2.x
- Git

> No se requiere Python ni ninguna otra dependencia instalada localmente. Todo corre dentro de los contenedores.

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/victormbr-creator/honeypot-project.git
cd honeypot-project
```

### 2. Configurar variables de entorno

```bash
cp .env.example .env
```

Editar `.env` con los valores deseados:

```env
POSTGRES_USER=honeypot_user
POSTGRES_PASSWORD=honeypot_pass
POSTGRES_DB=honeypot_db
POSTGRES_HOST=db
POSTGRES_PORT=5432

API_HOST=0.0.0.0
API_PORT=8000
```

### 3. Levantar todos los servicios

```bash
docker compose up -d
```

Esto levanta los cuatro servicios: Cowrie, FastAPI, PostgreSQL y Streamlit.

### 4. Verificar que todo esté corriendo

```bash
docker compose ps
```

Deberías ver los cuatro contenedores con estado `running`.

---

## 🌐 Acceso a los servicios

| Servicio | URL | Descripción |
|---|---|---|
| **FastAPI** | http://localhost:8000 | API REST |
| **Swagger UI** | http://localhost:8000/docs | Documentación interactiva OpenAPI |
| **ReDoc** | http://localhost:8000/redoc | Documentación alternativa |
| **Streamlit** | http://localhost:8501 | Dashboard de telemetría |
| **Cowrie SSH** | `localhost:2222` | Puerto honeypot (¡no es un servidor real!) |
| **PostgreSQL** | `localhost:5432` | Base de datos (TablePlus, psql, etc.) |

---

## 🔌 Conexión a PostgreSQL (TablePlus / DBeaver)

```
Host:     localhost
Port:     5432
User:     honeypot_user      (según tu .env)
Password: honeypot_pass      (según tu .env)
Database: honeypot_db        (según tu .env)
```

---

## 📡 Endpoints de la API

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/health` | Healthcheck del sistema |
| `GET` | `/events` | Listar todos los eventos capturados |
| `GET` | `/events/{id}` | Obtener un evento por ID |
| `POST` | `/events` | Ingresar un nuevo evento (usado por el log shipper) |
| `GET` | `/stats` | Métricas agregadas (top IPs, tipos de evento) |

> La especificación completa está en [`docs/openapi.json`](docs/openapi.json) y también disponible en vivo en `/docs`.

---

## 🧪 Pruebas

Las pruebas se ubican en `api/tests/` y se ejecutan con `pytest`:

```bash
# Ejecutar pruebas localmente
cd api
pip install -r requirements.txt pytest httpx
pytest tests/ -v
```

Las pruebas también se corren automáticamente en cada `push` a `main` mediante GitHub Actions (ver `.github/workflows/ci.yml`).

---

## 🔄 CI/CD

El proyecto incluye un pipeline de integración continua configurado con **GitHub Actions**.

**Se ejecuta automáticamente cuando:**
- Se hace `push` a la rama `main`
- Se abre un Pull Request hacia `main`

**Qué hace el pipeline:**
1. Hace checkout del código
2. Configura Python 3.10
3. Instala dependencias
4. Ejecuta las pruebas con `pytest`

Ver configuración completa en [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

---

## 🎬 Demo rápida (simulación de ataque)

Para ver el sistema en acción, puedes simular un atacante intentando conectarse al honeypot:

```bash
# Intento de conexión SSH al honeypot (contraseña incorrecta a propósito)
ssh root@localhost -p 2222
# Prueba contraseñas débiles: 123456, password, admin, root
```

Cowrie registrará la sesión, el log shipper enviará el evento a FastAPI, y en segundos aparecerá reflejado en el dashboard de Streamlit en `http://localhost:8501`.

---

## 📄 Documentación adicional

- [`docs/quantas.md`](docs/quantas.md) — Architecture Quantas del sistema
- [`docs/adr/`](docs/adr/) — Architecture Decision Records (ADRs)
- [`docs/openapi.json`](docs/openapi.json) — Especificación OpenAPI de la API

---

## 🛑 Detener los servicios

```bash
docker compose down
```

Para eliminar también los volúmenes de datos (borra la base de datos):

```bash
docker compose down -v
```

---

## 👥 Equipo

Victor Benitez

Tamara Schnaas

Tania Hernández 

---

## 📚 Referencias

- [Cowrie Documentation](https://cowrie.readthedocs.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Architecture Decision Records (ADRs)](https://adr.github.io/)
