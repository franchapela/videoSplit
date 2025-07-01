import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from procesar_videos import procesar_videos
import threading

class VideoProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de Videos")
        self.root.geometry("600x400")
        
        # Configurar tema oscuro
        self.root.configure(bg='#2b2b2b')
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configurar colores
        self.style.configure('TFrame', background='#2b2b2b')
        self.style.configure('TLabel', background='#2b2b2b', foreground='#ffffff')
        self.style.configure('TButton', 
                           background='#404040', 
                           foreground='#ffffff',
                           padding=10)
        self.style.map('TButton',
                      background=[('active', '#505050')],
                      foreground=[('active', '#ffffff')])
        
        # Frame principal
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        self.title_label = ttk.Label(
            self.main_frame, 
            text="Procesador de Videos", 
            font=('Helvetica', 16, 'bold')
        )
        self.title_label.pack(pady=20)
        
        # Frame para la selección de ruta
        self.path_frame = ttk.Frame(self.main_frame)
        self.path_frame.pack(fill=tk.X, pady=10)
        
        # Entrada de ruta
        self.path_var = tk.StringVar()
        self.path_entry = ttk.Entry(
            self.path_frame, 
            textvariable=self.path_var,
            width=50
        )
        self.path_entry.pack(side=tk.LEFT, padx=5)
        
        # Botón de búsqueda
        self.browse_button = ttk.Button(
            self.path_frame,
            text="Buscar",
            command=self.browse_directory
        )
        self.browse_button.pack(side=tk.LEFT, padx=5)
        
        # Botón de procesar
        self.process_button = ttk.Button(
            self.main_frame,
            text="Procesar Videos",
            command=self.start_processing
        )
        self.process_button.pack(pady=20)
        
        # Barra de progreso
        self.progress = ttk.Progressbar(
            self.main_frame,
            mode='indeterminate',
            length=400
        )
        self.progress.pack(pady=20)
        
        # Etiqueta de estado
        self.status_label = ttk.Label(
            self.main_frame,
            text="",
            wraplength=500
        )
        self.status_label.pack(pady=10)
        
        # Configurar el estilo de la entrada
        self.style.configure('TEntry', 
                           fieldbackground='#404040',
                           foreground='#ffffff',
                           insertcolor='#ffffff')
        
        # Configurar el estilo de la barra de progreso
        self.style.configure('TProgressbar',
                           background='#404040',
                           troughcolor='#2b2b2b')
    
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.path_var.set(directory)
    
    def update_status(self, message):
        self.status_label.config(text=message)
        self.root.update()
    
    def process_videos_thread(self):
        try:
            ruta = self.path_var.get()
            if not ruta:
                messagebox.showerror("Error", "Por favor, seleccione una ruta")
                return
            
            if not os.path.exists(ruta):
                messagebox.showerror("Error", "La ruta especificada no existe")
                return
            
            self.update_status("Procesando videos...")
            procesar_videos(ruta)
            self.update_status("¡Proceso completado exitosamente!")
            messagebox.showinfo("Éxito", "Los videos han sido procesados correctamente")
            
        except Exception as e:
            self.update_status(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Ocurrió un error durante el proceso:\n{str(e)}")
        
        finally:
            self.progress.stop()
            self.process_button.config(state='normal')
    
    def start_processing(self):
        if not self.path_var.get():
            messagebox.showerror("Error", "Por favor, seleccione una ruta")
            return
        
        self.process_button.config(state='disabled')
        self.progress.start()
        self.update_status("Iniciando procesamiento...")
        
        # Iniciar el procesamiento en un hilo separado
        thread = threading.Thread(target=self.process_videos_thread)
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoProcessorApp(root)
    root.mainloop() 