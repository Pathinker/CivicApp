from customtkinter import *

class Ventana():

    def __init__(self):

        self.app = CTk()
        self.Ancho = self.obtenerAnchoPantala(self.app, 30)
        self.Largo = self.obtenerLargoPantalla(self.app, 90)
        self.app.geometry(f"{self.Ancho}x{self.Largo}")
        self.app.title("Civic App")
        self.app.after(201, lambda: self.app.iconbitmap("Frontend/Imagenes/Logo.ico"))

        self.app._set_appearance_mode("light")
        self.coloroFondo = "#FFFFFF"
        self.azul = "#A1D8FF"

        self.app.configure(fg_color = self.coloroFondo)
        self.crearWidgets(self.app, self.Largo, self.Ancho)

        self.app.mainloop()

    def obtenerAnchoPantala(self, Ventana, Porcentaje, Ancho = None):

        if(Ancho is None):

            Ancho = Ventana.winfo_screenwidth()

        return Ancho * Porcentaje // 100
    
    def obtenerLargoPantalla(self, Ventana, Porcentaje, Largo = None):

        if (Largo is None):

            Largo = Ventana.winfo_screenheight()
        
        return Largo * Porcentaje // 100
    
    def obtenerAncho(self, Porcentaje, Ancho = None):
        
        return Ancho * Porcentaje // 100
    
    def obtenerLargo(self, Porcentaje, Largo = None):

        return Largo * Porcentaje // 100

    def crearWidgets(self, Ventana, Ancho, Largo):

        Ventana.rowconfigure(0, weight = 1)
        Ventana.columnconfigure(0, weight = 1)

        contenedorAncho = Ancho
        contenedorLargo = Largo

        contenedorPrincipal = CTkFrame(master = Ventana,
                                     width = contenedorAncho,
                                     height = contenedorLargo,
                                     fg_color = self.coloroFondo,
                                     bg_color = self.coloroFondo,
                                     corner_radius= 0,
                                     border_width = 0)
        
        contenedorPrincipal.grid(row = 0, column = 0, sticky = "nsew", pady = 40, padx = 20)

        contenedorPrincipal.rowconfigure(0, weight = 1)
        contenedorPrincipal.rowconfigure(1, weihgt = 1)
        contenedorPrincipal.columnconfigure(0, weight = 1)
    
        usuarioAncho = self.obtenerAncho(contenedorAncho, 100)
        usuarioLargo = self.obtenerLargo(contenedorLargo, 70)

        adminAncho = self.obtenerAncho(contenedorAncho, 100)
        adminLargo = self.obtenerLargo(contenedorLargo, 30)

if(__name__ == "__main__"):

    Ventana()