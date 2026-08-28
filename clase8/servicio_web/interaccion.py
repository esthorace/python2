import requests

r = requests.get("http://localhost:7001/student")
alumno = r.json()
if r.status_code == 200:
    alumno = r.json()
    for alumno in alumno["students"]:
        print("Alumno", alumno["id"])
        print("Nombre:", alumno["nombre"])
        print("Cursos:", alumno["cursos"])
else:
    print("Ocurrió un error.")

# r = requests.post("http://localhost:7001/student", json={"name": "Lautaro", "courses": 3})
# print("Código de estado:", r.status_code)

# alumnos = (("Juan", 1), ("Sofia", 5), ("Martin", 2))
# for nombre, cursos in alumnos:
#     r = requests.post("http://localhost:7001/student", json={"name": nombre, "courses": cursos})
#     print("Código de estado:", r.status_code)
#     print("Contenido de la respuesta:", r.json())


# r = requests.get("http://localhost:7001/student")
# respuesta = r.json()
# print("Contenido de la respuesta:", respuesta)

# datos = {"courses": 1006}
# r = requests.put("http://localhost:7001/student/300", json=datos)
# print("Código de estado:", r.status_code)

print("********************")
r = requests.get("http://localhost:7001/student/3")
alumno = r.json()
if r.status_code == 200:
    alumno = r.json()
    print(alumno["nombre"])
else:
    print("Ocurrió un error.")
