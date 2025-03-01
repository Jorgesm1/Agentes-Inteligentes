# Agente de Semáforo Inteligente

Este es un agente reactivo que controla un semáforo, cambiando su estado (verde, amarillo, rojo) según el flujo de tráfico. El agente ajusta la duración del estado verde en función del número de vehículos detectados.

## Funcionamiento

1. **Estados del Semáforo**:
   - Verde: Permite el paso de vehículos.
   - Amarillo: Indica precaución.
   - Rojo: Detiene el tráfico.

2. **Detección de Vehículos**:
   - El número de vehículos se simula aleatoriamente (entre 0 y 20).

3. **Ajuste del Tiempo en Verde**:
   - Si hay más de 15 vehículos, el tiempo en verde es de 15 segundos.
   - Si hay entre 10 y 15 vehículos, el tiempo en verde es de 12 segundos.
   - Si hay menos de 10 vehículos, el tiempo en verde es de 10 segundos.

4. **Ejecución**:
   - El semáforo cambia de estado en un bucle infinito, imprimiendo el estado actual y el tiempo de espera.

## Requisitos

- Python 3.x
- Módulo `random` (incluido en la biblioteca estándar de Python).

## Ejecución

Para ejecutar el programa, usa el siguiente comando:

```bash
python semaforo_inteligente.py