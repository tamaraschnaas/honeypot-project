# ADR-002: Elección de PostgreSQL como Base de Datos

## Estado
Aceptado

## Contexto
Necesitábamos un sistema de almacenamiento para persistir la telemetría capturada 
por el honeypot. Los eventos tienen una estructura bien definida (IP, timestamp, 
tipo de evento, credenciales probadas, comandos ejecutados), lo que hacía viable 
un esquema relacional. Evaluamos PostgreSQL y MongoDB como opciones principales.

## Decisión
Elegimos **PostgreSQL 15** como base de datos relacional.

## Consecuencias
* **Positivas:**
    * El esquema fijo de los eventos de Cowrie se adapta naturalmente a tablas 
      relacionales, permitiendo consultas SQL complejas para análisis de patrones.
    * Soporte nativo para tipos de datos como `TIMESTAMP`, `JSONB` e `INET` 
      (para IPs), que son exactamente los tipos que manejamos.
    * Imagen oficial en Docker Hub, integración directa con Docker Compose.
    * Compatible con herramientas de visualización y análisis como TablePlus, 
      DBeaver y pandas.
* **Negativas/Riesgos:**
    * Requiere definir el esquema antes de ingestar datos (menos flexible que 
      MongoDB para logs no estructurados).
    * Para volúmenes masivos de eventos en producción real se requeriría 
      particionamiento de tablas, lo cual está fuera del alcance académico 
      de este proyecto.
