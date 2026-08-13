# Consigna: Sistema de Gestión de Productos

Crear una estructura modular en Python para administrar el catálogo de una tienda. El sistema debe organizar el código mediante un paquete y cumplir con las siguientes especificaciones técnicas:

## 1. Estructura de archivos

* Crea una carpeta llamada `gestion_tienda`.
* Define esa carpeta como un paquete de Python creando el archivo correspondiente.
* Crea un módulo llamado `productos.py` dentro de dicho paquete.
* Crea un archivo `main.py` en la raíz del proyecto para ejecutar las pruebas.

## 2. Definición de la clase Producto

Dentro del módulo `productos.py`, define la clase `Producto` con las siguientes especificaciones:

* **Variables de clase:**
  * `porcentaje_iva`: número flotante que represente el IVA aplicable (por ejemplo, `0.21`).
  * `cantidad_total`: contador numérico entero que inicie en `0`.

* **Constructor (`__init__`) y variables de instancia:**
  * Debe recibir el `nombre` del producto y el `precio_base`.
  * Asigna estos valores a variables de instancia.
  * Incrementa en 1 la variable de clase `cantidad_total` cada vez que instancies un producto.

* **Métodos de instancia:**
  
  * `calcular_precio_final()`: retorna el precio base sumando el porcentaje de IVA definido en la clase.
  * `aplicar_descuento(porcentaje)`: recibe un porcentaje de descuento (por ejemplo, `10` para un 10%) y actualiza la variable de instancia del precio base.

## 3. Módulo principal main.py

* Importar la clase `Producto` desde el paquete `gestion_tienda`.
* Instanciar al menos dos productos distintos.
* Imprimir la cantidad total de productos creados mediante la variable de clase.
* Mostrar el precio final de uno de los productos, aplícale un descuento y muestra nuevamente su valor actualizado.