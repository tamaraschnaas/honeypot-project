# Plataforma de Telemetría para Honeypot  
### Proyecto Final – Fuentes de Datos

Plataforma replicable y orientada a análisis de datos construida con **Cowrie, Docker Compose, FastAPI, PostgreSQL y Streamlit**.  
El objetivo del proyecto es simular un entorno controlado de engaño defensivo, capturar telemetría generada por un honeypot, almacenarla en una base de datos, exponerla mediante una API y visualizarla en un dashboard interactivo.

---

## Descripción general del proyecto

Este proyecto fue desarrollado como proyecto final de la materia **Fuentes de Datos**.  
Se enfoca en el diseño de una **arquitectura defensiva, reproducible y basada en datos**, capaz de capturar trazas de comportamiento a partir de un honeypot y transformarlas en información estructurada, consultable y visualizable.

En lugar de construir herramientas ofensivas, el proyecto adopta un enfoque **seguro y académico**: utiliza un honeypot para observar y registrar interacciones sospechosas o simuladas dentro de un entorno controlado. A partir de ello, se construye un pipeline que demuestra cómo la telemetría de ciberseguridad puede tratarse como una fuente de datos para extracción, transformación, almacenamiento y análisis.

---

## Objetivo principal

Construir un **sistema containerizado y replicable** que:

- despliegue un honeypot en un entorno controlado,
- capture eventos de interacción,
- almacene los datos estructurados en una base de datos relacional,
- exponga esa información a través de una API,
- y muestre métricas clave mediante un dashboard interactivo.

---

## Arquitectura

La plataforma está compuesta por cuatro servicios principales:

### 1. Cowrie
Honeypot de interacción media que emula servicios SSH/Telnet y registra intentos de conexión, credenciales probadas, comandos ejecutados y comportamiento de sesión.

### 2. FastAPI
Capa de API utilizada para:
- verificar la salud del sistema,
- exponer los eventos almacenados,
- recibir registros estructurados de eventos.

### 3. PostgreSQL
Base de datos relacional utilizada para almacenar la telemetría del honeypot en formato estructurado.

### 4. Streamlit
Dashboard para visualizar eventos recientes e indicadores agregados como IPs más frecuentes y tipos de evento.

---

## Stack tecnológico

- **Docker Compose** – orquestación de servicios
- **Cowrie** – honeypot
- **FastAPI** – capa de API
- **PostgreSQL** – almacenamiento estructurado
- **Streamlit** – dashboard y visualización
- **Python** – lógica de backend y aplicación

---

## Estructura del repositorio

```text
honeypot-project/
├── api/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── dashboard/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── db/
│   └── init.sql
├── compose.yaml
├── .env.example
├── .gitignore
└── README.md
