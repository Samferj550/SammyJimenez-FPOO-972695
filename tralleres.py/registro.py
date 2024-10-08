# Clase para representar una tarea académica
class Tarea:
    def __init__(self, id_tarea, titulo, calificacion, categoria):
        self.id_tarea = id_tarea
        self.titulo = titulo
        self.calificacion = calificacion
        self.categoria = categoria

    def __str__(self):
        return f"ID: {self.id_tarea}, Título: {self.titulo}, Calificación: {self.calificacion}, Categoría: {self.categoria}"


# Función para registrar tareas
def registrar_tarea():
    id_tarea = input("Ingrese el ID de la tarea: ")
    titulo = input("Ingrese el título de la tarea: ")
    calificacion = float(input("Ingrese la calificación (0 a 5): "))
    categoria_num = int(input("Ingrese la categoría (1: quiz, 2: parcial, 3: trabajo): "))
    categoria = clasificar_categoria(categoria_num)

    tarea = Tarea(id_tarea, titulo, calificacion, categoria)
    return tarea


# Función para clasificar la categoría
def clasificar_categoria(categoria_num):
    if categoria_num == 1:
        return "quiz"
    elif categoria_num == 2:
        return "parcial"
    elif categoria_num == 3:
        return "trabajo"
    else:
        return "categoría desconocida"


# Función principal
def main():
    tareas = []
    
    while True:
        print("\nRegistro de tareas académicas")
        tarea = registrar_tarea()
        tareas.append(tarea)

        continuar = input("¿Desea registrar otra tarea? (s/n): ").strip().lower()
        if continuar != 's':
            break

    # Salida organizada de las tareas
    print("\nLista de tareas registradas:")
    for tarea in tareas:
        print(tarea)


if __name__ == "__main__":
    main()
