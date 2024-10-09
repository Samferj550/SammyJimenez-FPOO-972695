class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial_clinico = []

    def agregar_historial(self, cita):
        self.historial_clinico.append(cita)

    def listar_historial(self):
        print(f"Historial clínico de {self.nombre}:")
        if not self.historial_clinico:
            print("No hay citas registradas.")
        for cita in self.historial_clinico:
            print(cita.get_info())


class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Nombre: {self.nombre}, Especialidad: {self.especialidad}"


class CitaMedica:
    def __init__(self, fecha, doctor, paciente):
        self.fecha = fecha
        self.doctor = doctor
        self.paciente = paciente

    def get_info(self):
        return f"Cita médica: {self.fecha}, Doctor: {self.doctor.nombre}, Paciente: {self.paciente.nombre}"


class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []
        self.pacientes = []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)
        print(f"Doctor {doctor.nombre} agregado al hospital.")

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)
        print(f"Paciente {paciente.nombre} agregado al hospital.")

    def listar_doctores(self):
        print("Doctores registrados:")
        for doctor in self.doctores:
            print(doctor)

    def listar_pacientes(self):
        print("Pacientes registrados:")
        for paciente in self.pacientes:
            print(f"Nombre: {paciente.nombre}, Edad: {paciente.edad}")

    def asignar_cita(self, paciente, doctor, fecha):
        cita = CitaMedica(fecha, doctor, paciente)
        paciente.agregar_historial(cita)
        print(f"Cita programada: {cita.get_info()}")


# Ejemplo de uso
hospital = Hospital("Hospital General")

# Agregar doctores
doctor1 = Doctor("Dr. Smith", "Cardiología")
doctor2 = Doctor("Dr. Johnson", "Neurología")
doctor3 = Doctor("Dr. Brown", "Pediatría")
doctor4 = Doctor("Dr. Taylor", "Ginecología")
hospital.agregar_doctor(doctor1)
hospital.agregar_doctor(doctor2)
hospital.agregar_doctor(doctor3)
hospital.agregar_doctor(doctor4)

# Agregar pacientes
paciente1 = Paciente("Juan Pérez", 30)
paciente2 = Paciente("María Gómez", 25)
paciente3 = Paciente("Luis Fernández", 40)
hospital.agregar_paciente(paciente1)
hospital.agregar_paciente(paciente2)
hospital.agregar_paciente(paciente3)

# Listar doctores y pacientes
hospital.listar_doctores()
hospital.listar_pacientes()

# Programar citas
hospital.asignar_cita(paciente1, doctor1, "2024-10-15 10:00")
hospital.asignar_cita(paciente2, doctor2, "2024-10-16 11:00")
hospital.asignar_cita(paciente3, doctor3, "2024-10-17 12:00")

# Listar historial clínico de los pacientes
paciente1.listar_historial()
paciente2.listar_historial()
paciente3.listar_historial()
