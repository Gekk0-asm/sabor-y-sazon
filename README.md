# 🍽 Sabor & Sazón — Fase 2: Fundamentos de Abstracción y Modelado de Datos

**Autor:** Juan David Velasco Valderrama
**Curso:** Estructura de Datos (301305)
**Programa:** Ingeniería de Sistemas — ECBTI / UNAD
**Fase:** 2 — Fundamentos de Abstracción y Modelado de Datos (RAC 1)

---

## 📌 Descripción de la actividad

El restaurante **"Sabor & Sazón"** necesita una aplicación de escritorio que permita
gestionar los datos básicos de sus clientes y calcular el costo total del servicio
gastronómico según las sesiones tomadas y el precio por sesión asociado al tipo de menú
elegido.

La aplicación debe:

- Mostrar una **interfaz inicial de acceso** con una contraseña genérica enmascarada (`1793`).
- Permitir el **registro de datos del cliente**: identificación, nombre, género,
  tipo de menú, número de sesiones y fecha automática de registro.
- Autocompletar el **costo por sesión** según el menú seleccionado (campo deshabilitado).
- Exponer una **clase pública `GestionClientes`** que almacene los datos y ofrezca un
  método para calcular el costo total del servicio.
- Presentar un **formulario de reporte** con todos los datos del cliente y el total a pagar.
- Incluir botones de **Guardar**, **Calcular/Mostrar Reporte** y **Salir** (con confirmación).

Esta solución da cumplimiento al **RAC 1**: analizar colaborativamente los requerimientos
funcionales de una situación problémica mediante la abstracción y representación de
tipos de datos abstractos con clases y objetos.

---

## 🚀 Cómo ejecutar

Desde la raíz del proyecto:

```bash
python run.py
```

Eso es todo. `run.py` delega en `src.main.main()`, que a su vez crea una instancia de
`App` y arranca el bucle principal de Tkinter.

### Requisitos

- **Python 3.10+**
- **Tkinter** (viene incluido en la instalación estándar de Python)

No hay dependencias externas que instalar. Todo el proyecto funciona con la librería
estándar.

---

## 🗂 Estructura del proyecto

```
proyecto/
├── run.py                          # Punto de entrada
├── config.json                     # Configuración general (app + theme seleccionado)
├── README.md
└── src/
    ├── __init__.py
    ├── main.py                     # Carga config y arranca App
    ├── app.py                      # Ventana raíz de Tkinter (tk.Tk)
    ├── config/
    │   ├── __init__.py
    │   ├── config_manager.py       # Lectura de config.json y del theme activo
    │   └── themes/
    │       └── tokyo_night.json    # Paletas dark / storm / light
    ├── models/
    │   ├── __init__.py
    │   └── gestion_clientes.py     # Clase pública GestionClientes
    └── ui/
        ├── __init__.py
        ├── window.py               # MainWindow (controlador de navegación)
        └── frames/
            ├── __init__.py
            ├── base_frame.py       # Clase base para todos los frames
            ├── login_frame.py      # Pantalla de acceso
            ├── register_frame.py   # Formulario de registro del cliente
            └── report_frame.py     # Reporte con el total a pagar
```

---

## 🧩 Explicación de cada módulo

### `run.py`
Punto de entrada único del proyecto. Solo importa `main` desde `src.main` y lo ejecuta
cuando el archivo se corre directamente. Esto mantiene la raíz del proyecto limpia y
permite que el tutor pueda lanzar la app con un único comando.

### `src/main.py`
Se encarga de:

1. Localizar `config.json` en la raíz del proyecto.
2. Instanciar `App(config_path=...)`.
3. Manejar la salida limpia si el usuario interrumpe (`Ctrl+C`) o si ocurre un error fatal.

### `src/app.py`
Crea la ventana raíz de Tkinter (`tk.Tk`), le asigna el título, la geometría fija
(700×600) y aplica el color de fondo del tema activo. Luego construye `MainWindow`,
que se encarga de la navegación entre pantallas.

### `src/config/config_manager.py`
Gestiona la configuración del proyecto:

- `get("clave.anidada")`: lee valores de `config.json` con notación de puntos
  (por ejemplo, `"app.author"`).
- `get_theme()`: carga el archivo de tema indicado en `config.json`
  (`theme.name`) y devuelve la paleta correspondiente al modo seleccionado
  (`theme.mode`), con **fallback a la paleta por defecto** si algo falta.

### `src/config/themes/tokyo_night.json`
Archivo de tema con **tres variantes** de la paleta Tokyo Night:

| Variante | Fondo base | Descripción |
|---|---|---|
| `dark`  | `#1a1b26` | Paleta original Tokyo Night |
| `storm` | `#24283b` | Variante con fondo azulado más claro |
| `light` | `#e6e7ed` | Versión clara de la paleta |

### `src/models/gestion_clientes.py`
Contiene la **clase pública `GestionClientes`** exigida por el Anexo 1. Es el
**tipo de dato abstracto (TDA)** que modela al cliente del restaurante.

Responsabilidades:

- Almacenar los atributos: identificación, nombre, género, tipo de menú,
  número de sesiones y fecha de registro.
- Exponer propiedades de solo lectura (`@property`) y setters explícitos.
- Ofrecer el método **`calcular_costo_total(numero_sesiones, costo_por_sesion)`**
  que retorna el costo total del servicio (tal como lo pide la actividad).
- Centralizar en `COSTOS_MENU` el precio por sesión de cada tipo de menú
  (Tabla 2 del Anexo 1), accesible vía `costo_por_menu(tipo_menu)`.

### `src/ui/window.py`
Clase `MainWindow`, que actúa como **controlador de navegación**. Mantiene un
diccionario de frames instanciados y expone `show_frame(ClaseFrame)` para cambiar
entre pantallas sin re-crear widgets. También guarda el `cliente_actual`, usado
para pasar datos desde el registro hacia el reporte.

### `src/ui/frames/base_frame.py`
Clase base de la que heredan todos los frames. Resuelve automáticamente el acceso
a:

- `self.controller` → la `MainWindow`
- `self.app` → la `App` (root de Tkinter)
- `self.config` → el `ConfigManager`
- `self.theme` → la paleta activa

Define además los hooks `on_enter()`, `on_exit()` y `refresh()`, y el helper
`apply_bg()` para pintar el fondo del frame con el color del tema.

### `src/ui/frames/login_frame.py`
Pantalla inicial de acceso. Contraseña genérica enmascarada (`show="*"`), validación
con `Enter` o con el botón **Ingresar**, y carga dinámica del nombre del autor y la
versión desde `config.json`.

### `src/ui/frames/register_frame.py`
Formulario de registro. Incluye:

- Campos de identificación y nombre.
- Selección de género con `Radiobutton`.
- Selección del tipo de menú con `ttk.Combobox`, que autocompleta el **costo por
  sesión** en un campo deshabilitado (`state="disabled"`).
- Campo de sesiones con validación numérica.
- Fecha de registro generada automáticamente por el sistema.
- Botones **Guardar**, **Calcular / Mostrar Reporte** y **Salir** (con confirmación).

### `src/ui/frames/report_frame.py`
Formulario de reporte. Recupera el `cliente_actual` desde la `MainWindow`, calcula
el total usando `GestionClientes.calcular_costo_total(...)` y lo muestra en un
`tk.Text` con formato de tabla. Incluye un botón **Volver al registro**.

---

## 🎨 Sistema de temas

### Por qué existe

La guía de la actividad pide que **cada integrante del grupo personalice su
formulario con un color de fondo diferente** para que, al consolidar los cinco
proyectos en una única solución grupal, cada aporte se distinga visualmente.

En lugar de hardcodear los colores en cada frame, decidí **tomarme la libertad de
implementar un sistema de temas configurable**: una paleta externa en JSON que se
carga según lo indique `config.json`. Esto trae varias ventajas:

1. **Cumple el requisito** de personalización con un color distinto al de mis
   compañeros (Tokyo Night dark es mi firma visual).
2. **Separa la presentación de la lógica**: los frames solo piden colores por
   clave semántica (`bg`, `fg`, `primary`, `accent`…), no valores hex sueltos.
3. **Facilita el consolidado grupal**: si el Compilador quiere unificar la
   apariencia, solo cambia el `mode` en `config.json` y toda la app se re-pinta.
4. **Demuestra abstracción**: el `ConfigManager` resuelve la paleta con fallback,
   merge con `DEFAULT_THEME` y validación de variantes.

### Cómo se elige el tema

Todo se controla desde `config.json`:

```json
{
  "theme": {
    "name": "tokyo_night",
    "mode": "dark"
  }
}
```

| Clave | Significado |
|---|---|
| `theme.name` | Archivo a cargar dentro de `src/config/themes/` (sin `.json`) |
| `theme.mode` | Variante dentro del archivo: `dark`, `storm` o `light` |

Cambiar de `dark` a `light` (o `storm`) es cuestión de editar una sola palabra
y reiniciar la app.

### Estructura de un archivo de tema

```json
{
  "name": "tokyo_night",
  "mode": {
    "dark":  { "bg": "...", "fg": "...", "primary": "...", ... },
    "storm": { ... },
    "light": { ... }
  }
}
```

Cada variante define las mismas claves semánticas:

| Clave | Uso típico |
|---|---|
| `bg` | Fondo principal de frames y ventana |
| `fg` | Texto principal |
| `primary` | Color de acciones principales |
| `secondary` | Paneles y contenedores elevados |
| `accent` | Acento (títulos, botón secundario) |
| `red` / `green` / `yellow` / `orange` | Estados semánticos (error, éxito, advertencia) |
| `cyan` / `blue` / `purple` / `pink` | Variantes de acento |
| `comment` | Texto deshabilitado o secundario |
| `selection` / `border` | Selección y bordes finos |
| `muted` / `subtle` / `bright` | Tonos intermedios de texto |

### ¿Qué pasa si falta algo?

`ConfigManager.get_theme()` hace **merge** con `DEFAULT_THEME`, así que cualquier
clave que no esté en el archivo de tema se rellena automáticamente con el valor
por defecto de Tokyo Night dark. La aplicación **nunca crashea** por un tema
malformado o incompleto.

---

## 🌃 Créditos del tema

La paleta usada en este proyecto está basada en **Tokyo Night**, una paleta de
colores para editores y terminales inspirada en la estética nocturna de Tokio.

Sitio oficial de referencia:

> https://wixdaq.github.io/Tokyo-Night-Website/index.html

Los colores fueron extraídos directamente de esa fuente y organizados en las
tres variantes oficiales (`dark`, `storm`, `light`) respetando la nomenclatura
original. Agradezco a los autores de Tokyo Night por publicar la paleta abierta
y permitir su uso en proyectos educativos.

---

## 🧠 Decisiones técnicas relevantes

- **Patrón Frame + Controlador**: `MainWindow` actúa como controlador y los
  `BaseFrame` como vistas intercambiables. Evita re-crear widgets y mantiene
  un solo `tk.Tk()` raíz (requisito para el consolidado grupal).
- **Tema externo en JSON**: permite cambiar la apariencia sin recompilar ni
  tocar código, y demuestra abstracción de configuración.
- **Fallback a `DEFAULT_THEME`**: ninguna UI queda sin colores si el archivo de
  tema falta, está mal formado o no tiene la variante pedida.
- **Clase `GestionClientes` desacoplada de la UI**: el cálculo y el modelado de
  datos viven en `src/models/`, totalmente independientes de Tkinter. Esto
  facilita las pruebas y es la evidencia central de la abstracción para el RAC 1.
- **Formulario centrado y alineado**: se usan `grid_columnconfigure(minsize=...)`
  y `sticky="ew"` para que todos los inputs midan lo mismo y los labels queden
  alineados a la derecha, sin depender de `width` individual por widget.

---

## ✍️ Autor

**Juan David Velasco Valderrama**
Estudiante de Ingeniería de Sistemas — UNAD
Curso: Estructura de Datos (301305) — Fase 2