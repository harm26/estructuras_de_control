# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
# que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar
# sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumnos:
    nombre = ""
    nota = 0

    def __int__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_alumno(self, nombre, nota):
        if nota > 51:
            return "El nombre del alumno es: " + nombre + " y 'SI' aprobó el curso con una nota de " + str(nota)
        else:
            return "El nombre del alumno es: " + nombre + " y 'NO' aprobó el curso, su nota es: " + str(nota)

alumno = Alumnos()

print(alumno.mostrar_alumno("Humberto", 93))
print(alumno.mostrar_alumno("Pablo", 51))
print(alumno.mostrar_alumno("Pepe", 50))
print(alumno.mostrar_alumno("Maria", 75))





