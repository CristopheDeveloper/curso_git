from datetime import date

def validar_edad(anio_nacimiento):
  """
  Valida si una persona es mayor de 18 años.
  
  Args:
    anio_nacimiento: El año de nacimiento de la persona.
    
  Returns:
    True si es mayor de 18 años, False en caso contrario.
  """
  anio_actual = date.today().year
  edad = anio_actual - anio_nacimiento
  return edad >= 18

def calcular_edad(fecha_nacimiento):
  """
  Calcula la edad de una persona en años a partir de su fecha de nacimiento.
  
  Args:
    fecha_nacimiento: Un objeto date con la fecha de nacimiento (YYYY, MM, DD).
    
  Returns:
    La edad de la persona en años.
  """
  today = date.today()
  # Restamos el año actual menos el año de nacimiento
  edad = today.year - fecha_nacimiento.year
  # Si el mes o el día actual son menores que el de nacimiento,
  # significa que aún no ha cumplido años, por lo que restamos 1.
  if (today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1
  return edad

# --- Ejemplo de uso ---

# Pedir la fecha de nacimiento al usuario
try:
  print("Por favor, ingresa tu fecha de nacimiento:")
  anio = int(input("Año (YYYY): "))
  mes = int(input("Mes (MM): "))
  dia = int(input("Día (DD): "))
  
  fecha_nacimiento_usuario = date(anio, mes, dia)
  
  # Calcular y mostrar la edad
  edad_calculada = calcular_edad(fecha_nacimiento_usuario)
  print(f"Tienes {edad_calculada} años.")
  
  # Validar si es mayor de 18 años
  if validar_edad(anio):
    print("Eres mayor de 18 años. ✅")
  else:
    print("Eres menor de 18 años. ❌")
    
except ValueError:
  print("Error: Ingresa una fecha válida (números enteros para año, mes y día).")
