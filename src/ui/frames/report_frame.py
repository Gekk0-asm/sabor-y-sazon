import tkinter as tk

from .base_frame import BaseFrame
from ...models import GestionClientes


class ReportFrame(BaseFrame):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.apply_bg()
        self._build()

    def _build(self):
        tk.Label(
            self,
            text="📋 Reporte del Cliente",
            font=("Segoe UI", 18, "bold"),
            bg=self.theme["bg"],
            fg=self.theme["accent"],
        ).pack(pady=(30, 20))

        self.txt = tk.Text(
            self,
            width=55,
            height=15,
            bg=self.theme["secondary"],
            fg=self.theme["fg"],
            font=("Consolas", 11),
            bd=0,
            padx=15,
            pady=15,
        )
        self.txt.pack(padx=30)

        tk.Button(
            self,
            text="Volver al registro",
            bg=self.theme["primary"],
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=20,
            command=self._volver,
        ).pack(pady=20)

    def on_enter(self):
        self.app.title("Sabor y Sazón - Reporte")

        cliente: GestionClientes = self.controller.cliente_actual
        self.txt.delete("1.0", tk.END)

        if cliente is None:
            self.txt.insert(tk.END, "No hay datos registrados.")
            return

        costo_sesion = GestionClientes.costo_por_menu(cliente.tipo_menu)
        total = cliente.calcular_costo_total(cliente.numero_sesiones, costo_sesion)

        reporte = (
            f"  IDENTIFICACIÓN : {cliente.identificacion}\n"
            f"  NOMBRE         : {cliente.nombre}\n"
            f"  GÉNERO         : {cliente.genero}\n"
            f"  TIPO DE MENÚ   : {cliente.tipo_menu}\n"
            f"  COSTO/SESIÓN   : $ {costo_sesion:,}\n"
            f"  SESIONES       : {cliente.numero_sesiones}\n"
            f"  FECHA REGISTRO : {cliente.fecha_registro}\n"
            f"  -----------------------------------------\n"
            f"  TOTAL A PAGAR  : $ {total:,}\n"
        ).replace(",", ".")

        self.txt.insert(tk.END, reporte)

    def _volver(self):
        from ..window import RegisterFrame

        self.controller.show_frame(RegisterFrame)
