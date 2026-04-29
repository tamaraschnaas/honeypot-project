# ADR-001: Elección de Cowrie como honeypot principal

## Estado
Aceptado

## Contexto
Para este proyecto de Fuentes de Datos se necesitaba una fuente de datos realista, estructurada y relevante para analizar eventos de ciberseguridad defensiva. En lugar de trabajar con un dataset estático, se decidió construir una arquitectura capaz de capturar telemetría generada por intentos de acceso no autorizado.

El sistema requería un honeypot que pudiera simular servicios comúnmente atacados, especialmente SSH y Telnet, sin exponer el sistema real del equipo. Además, era importante que la herramienta generara registros estructurados para poder integrarlos posteriormente con una API, una base de datos y un dashboard de análisis.

## Decisión
Se eligió Cowrie como honeypot principal del proyecto.

Cowrie es un honeypot de interacción media que simula servicios SSH y Telnet. Permite registrar intentos de autenticación, credenciales utilizadas, comandos ejecutados por los atacantes y otros eventos relevantes. Esta información puede utilizarse como materia prima para un flujo de ingesta, almacenamiento, procesamiento y visualización de datos.

## Consecuencias

### Positivas
- Permite capturar eventos de seguridad en un formato útil para análisis posterior.
- Genera logs estructurados que pueden integrarse con procesos ETL o APIs.
- Simula servicios ampliamente atacados, por lo que es adecuado para observar patrones reales de automatización ofensiva.
- Puede ejecutarse en Docker, lo que facilita la replicabilidad del proyecto.
- Mantiene aislado el entorno simulado y reduce el riesgo de comprometer el host real.

### Negativas o limitaciones
- Al ser un honeypot de interacción media, puede ser detectado por atacantes avanzados.
- Requiere cuidado en su configuración para evitar exponer servicios reales.
- La calidad del análisis depende de la cantidad y variedad de eventos capturados.
- Para una integración completa con FastAPI, se necesita un mecanismo adicional de ingesta, como un log shipper o un proceso que lea los eventos generados por Cowrie.

## Alternativas consideradas
Se consideró utilizar otros enfoques, como analizar datasets públicos de ciberseguridad o construir un generador sintético de eventos. Sin embargo, estas opciones no ofrecían el mismo nivel de realismo ni permitían demostrar una arquitectura completa de captura, procesamiento y visualización de datos.

También se pudieron utilizar otros honeypots, pero Cowrie fue elegido por su documentación, facilidad de despliegue con Docker y utilidad específica para registrar actividad asociada a SSH/Telnet.

## Resultado
Cowrie se mantiene como el componente de ingesta principal del proyecto. Su función es generar la telemetría inicial que después será almacenada, consultada y visualizada mediante PostgreSQL, FastAPI y Streamlit.
