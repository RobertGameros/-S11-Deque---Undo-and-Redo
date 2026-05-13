# Sistema Gestor de Acciones (Undo/Redo) 🔄

Este es un sistema gestor de estados desarrollado en Python utilizando programación orientada a objetos, separación de responsabilidades y estructuras de datos personalizadas.

## 🚀 Características
- Implementación de una estructura `Deque` (Double-Ended Queue) propia.
- Motor de transacciones Undo/Redo (Deshacer/Rehacer).
- Interfaz gráfica con Tkinter en modo oscuro.
- Atajos de teclado incorporados (`Enter`, `Ctrl+Z`, `Ctrl+Y`).
- **Plus:** Registro de auditoría (Event Sourcing) que documenta todo el ciclo de vida de los eventos.

## 📂 Estructura del Proyecto
- `Estructura.py`: Contiene la clase `Deque` aislada.
- `ManagerActions.py`: Lógica de negocio y manejo de historiales.
- `Interfaz(Tkinter).py`: Interfaz gráfica que consume las clases anteriores.
- `Unittest.py`: Suite de pruebas automatizadas.

## ⚙️ Requisitos
- Python 3.12 o superior.
- No requiere dependencias externas (utiliza librerías estándar).

## 🏃‍♂️ Cómo ejecutar el programa
1. Clona el repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el siguiente comando para abrir la interfaz:
   ```bash
   python "Interfaz(Tkinter).py"
