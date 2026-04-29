# ADR-003: Elección de FastAPI como Capa de API

## Estado
Aceptado

## Contexto
Necesitábamos una capa intermedia entre el honeypot y la base de datos que 
recibiera eventos, los validara y los persistiera. También debía exponer 
los datos almacenados para su consumo por el dashboard. Evaluamos FastAPI 
y Flask como opciones en el ecosistema Python.

## Decisión
Elegimos **FastAPI** como framework para la capa de API REST.

## Consecuencias
* **Positivas:**
    * Generación automática de documentación OpenAPI (Swagger UI en `/docs` 
      y ReDoc en `/redoc`) sin configuración adicional, cubriendo directamente 
      el Requisito 5 de la rúbrica del proyecto.
    * Validación automática de payloads mediante modelos Pydantic, lo que 
      garantiza que los eventos recibidos tengan la estructura correcta antes 
      de persistirlos.
    * Alto rendimiento gracias a su naturaleza asíncrona (ASGI), adecuado 
      para recibir eventos en tiempo real desde el log shipper.
    * Tipado estático que facilita el mantenimiento y la detección temprana 
      de errores.
* **Negativas/Riesgos:**
    * Curva de aprendizaje inicial con el modelo asíncrono (`async/await`) 
      para desarrolladores no familiarizados.
    * Para este proyecto académico la asincronía no es estrictamente necesaria, 
      aunque no representa un problema.
