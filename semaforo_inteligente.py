import time
import random

class SemaforoInteligente:
    def __init__(self):
        self.estado = "rojo"  # Estado inicial del semáforo
        self.tiempo_verde = 10  # Tiempo inicial en verde
        self.tiempo_amarillo = 3  # Tiempo en amarillo
        self.tiempo_rojo = 5  # Tiempo en rojo

    def detectar_vehiculos(self):
        """Simula la detección de vehículos."""
        return random.randint(0, 20)  # Número aleatorio de vehículos detectados

    def ajustar_tiempo_verde(self, vehiculos):
        """Ajusta el tiempo en verde según el número de vehículos."""
        if vehiculos > 15:
            self.tiempo_verde = 15  # Más tiempo si hay mucho tráfico
        elif vehiculos > 10:
            self.tiempo_verde = 12
        else:
            self.tiempo_verde = 10

    def cambiar_estado(self):
        """Cambia el estado del semáforo."""
        while True:
            # Estado verde
            self.estado = "verde"
            print(f"Semáforo en {self.estado} por {self.tiempo_verde} segundos.")
            time.sleep(self.tiempo_verde)

            # Estado amarillo
            self.estado = "amarillo"
            print(f"Semáforo en {self.estado} por {self.tiempo_amarillo} segundos.")
            time.sleep(self.tiempo_amarillo)

            # Estado rojo
            self.estado = "rojo"
            print(f"Semáforo en {self.estado} por {self.tiempo_rojo} segundos.")
            time.sleep(self.tiempo_rojo)

            # Detectar vehículos y ajustar el tiempo en verde
            vehiculos = self.detectar_vehiculos()
            print(f"Vehículos detectados: {vehiculos}")
            self.ajustar_tiempo_verde(vehiculos)

if __name__ == "__main__":
    semaforo = SemaforoInteligente()
    semaforo.cambiar_estado()