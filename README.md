# expense-tracker

Una aplicación de línea de comandos para rastrear y gestionar gastos personales.

## 📋 Requisitos previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- git (opcional, para clonar el repositorio)

## 🚀 Instalación paso a paso

### 1. Clonar o descargar el proyecto

Si tienes git instalado:
```bash
git clone https://github.com/juanfvega/expense-tracker.git
cd expense-tracker
```

O descarga el proyecto manualmente y navega a la carpeta.

### 2. Crear un entorno virtual (recomendado)

Crear un entorno virtual ayuda a mantener las dependencias aisladas:

```bash
python3 -m venv venv
```

### 3. Activar el entorno virtual

**En Linux/Mac:**
```bash
source venv/bin/activate
```

**En Windows:**
```bash
venv\Scripts\activate
```

Deberías ver `(venv)` al inicio de tu línea de comandos.

### 4. Instalar el proyecto en modo desarrollo

Esto instalará el paquete y todas sus dependencias:

```bash
pip install -e .
```

El flag `-e` instala en modo "editable", lo que significa que los cambios en el código se reflejan inmediatamente sin necesidad de reinstalar.

### 5. Instalar dependencias de desarrollo (opcional)

Si deseas ejecutar los tests:

```bash
pip install pytest
```

## 📖 Uso

Una vez instalado, puedes usar el comando `expense-tracker` desde cualquier lugar:

### Agregar un gasto

```bash
expense-tracker add --amount 50.5 --description "Almuerzo" --category "Comida"
```

### Listar todos los gastos

```bash
expense-tracker list
```

### Ver la ayuda

```bash
expense-tracker --help
```

## 🧪 Ejecutar tests

Para verificar que todo funciona correctamente:

```bash
pytest
```

Deberías ver que todos los tests pasan:
```
====== 6 passed in 0.02s ======
```

## 📁 Estructura del proyecto

```
expense-tracker/
├── expense_tracker/       # Código principal de la aplicación
│   ├── __init__.py
│   ├── cli.py            # Interfaz de línea de comandos
│   ├── logic.py          # Lógica de negocio
│   ├── models.py         # Modelos de datos
│   └── storage.py        # Gestión de almacenamiento
├── tests/                # Tests unitarios
│   └── test_basic.py
├── README.md             # Este archivo
├── requirements.txt      # Dependencias del proyecto
└── setup.py             # Configuración de instalación
```

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
