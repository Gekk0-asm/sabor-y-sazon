from datetime import datetime


class GestionClientes:
    """
    Clase pública que almacena los datos del cliente
    y calcula el costo total del servicio.
    """

    # Costos por sesión según tipo de menú (Tabla 2 del Anexo 1)
    COSTOS_MENU = {
        "Menú ejecutivo": 35000,
        "Menú vegetariano": 28000,
        "Menú degustación": 75000,
        "Menú infantil": 20000,
        "Menú gourmet": 95000,
    }

    def __init__(
        self,
        identificacion: str = "",
        nombre: str = "",
        genero: str = "",
        tipo_menu: str = "",
        numero_sesiones: int = 0,
        fecha_registro: str = "",
    ):
        self._identificacion = identificacion
        self._nombre = nombre
        self._genero = genero
        self._tipo_menu = tipo_menu
        self._numero_sesiones = numero_sesiones
        self._fecha_registro = fecha_registro or datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    # --- Propiedades ---
    @property
    def identificacion(self):
        return self._identificacion

    @property
    def nombre(self):
        return self._nombre

    @property
    def genero(self):
        return self._genero

    @property
    def tipo_menu(self):
        return self._tipo_menu

    @property
    def numero_sesiones(self):
        return self._numero_sesiones

    @property
    def fecha_registro(self):
        return self._fecha_registro

    # --- Setters ---
    def set_identificacion(self, v):
        self._identificacion = v

    def set_nombre(self, v):
        self._nombre = v

    def set_genero(self, v):
        self._genero = v

    def set_tipo_menu(self, v):
        self._tipo_menu = v

    def set_numero_sesiones(self, v):
        self._numero_sesiones = v

    def set_fecha_registro(self, v):
        self._fecha_registro = v

    # --- Método de cálculo (requerido por el Anexo 1) ---
    def calcular_costo_total(
        self, numero_sesiones: int, costo_por_sesion: float
    ) -> float:
        """
        Recibe el número de sesiones y el costo por sesión
        y retorna el costo total del servicio.
        """
        return numero_sesiones * costo_por_sesion

    @classmethod
    def costo_por_menu(cls, tipo_menu: str) -> int:
        return cls.COSTOS_MENU.get(tipo_menu, 0)
