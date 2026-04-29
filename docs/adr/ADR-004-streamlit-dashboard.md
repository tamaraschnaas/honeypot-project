# ADR-004: Elección de Streamlit para el Dashboard

## Estado
Aceptado

## Contexto
Necesitábamos una herramienta para visualizar la telemetría almacenada: 
eventos recientes, IPs más frecuentes, tipos de ataque y línea de tiempo 
de actividad. Evaluamos Streamlit y Grafana como opciones principales.

## Decisión
Elegimos **Streamlit** como herramienta para el dashboard de visualización.

## Consecuencias
* **Positivas:**
    * Desarrollo 100% en Python, sin necesidad de aprender un lenguaje de 
      templating adicional ni configurar datasources externos como requiere 
      Grafana.
    * Integración directa con librerías de análisis y visualización del 
      ecosistema Python (pandas, plotly, altair), que el equipo ya maneja.
    * Tiempo de desarrollo significativamente menor que Grafana para un 
      caso de uso académico.
    * Se containeriza fácilmente con un Dockerfile simple, manteniendo la 
      arquitectura 100% en Docker Compose.
* **Negativas/Riesgos:**
    * Grafana ofrecería dashboards más avanzados y configurables para un 
      entorno de producción real, con alertas y mayor variedad de 
      visualizaciones out-of-the-box.
    * Streamlit recarga el script completo en cada interacción del usuario, 
      lo que puede ser ineficiente con volúmenes grandes de datos sin 
      implementar caché explícito (`@st.cache_data`).
