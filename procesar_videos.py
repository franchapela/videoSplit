import os
import shutil
from pathlib import Path

def procesar_videos(ruta_origen):
    # Crear la carpeta 'subir' si no existe
    ruta_subir = os.path.join(ruta_origen, 'subir')
    os.makedirs(ruta_subir, exist_ok=True)
    
    # Obtener lista de videos en la ruta
    videos = [f for f in os.listdir(ruta_origen) if f.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]
    
    # Obtener las carpetas ya existentes en 'subir' y su número
    carpetas_existentes = [d for d in os.listdir(ruta_subir) if os.path.isdir(os.path.join(ruta_subir, d)) and d.isdigit()]
    carpetas_existentes = sorted([int(d) for d in carpetas_existentes])
    
    if carpetas_existentes:
        ultima_carpeta = carpetas_existentes[-1]
        carpeta_actual = ultima_carpeta
        ruta_carpeta_actual = os.path.join(ruta_subir, str(carpeta_actual))
        videos_en_carpeta = len([f for f in os.listdir(ruta_carpeta_actual) if f.lower().endswith((".mp4", ".avi", ".mkv", ".mov"))])
    else:
        carpeta_actual = 1
        videos_en_carpeta = 0
    
    # Procesar cada video
    for video in videos:
        # Obtener el nombre sin extensión
        nombre_base, extension = os.path.splitext(video)
        
        # Encontrar la posición del primer #
        pos_hash = nombre_base.find('#')
        if pos_hash != -1:
            # Tomar solo la parte antes del primer #
            nuevo_nombre = nombre_base[:pos_hash].strip()
        else:
            nuevo_nombre = nombre_base
            
        # Agregar los hashtags
        nuevo_nombre = f"{nuevo_nombre} #peliclips #peliculas #series{extension}"
        
        # Si la carpeta actual ya tiene 5 videos, pasar a la siguiente
        if videos_en_carpeta >= 5:
            carpeta_actual += 1
            videos_en_carpeta = 0
        carpeta_destino = os.path.join(ruta_subir, str(carpeta_actual))
        os.makedirs(carpeta_destino, exist_ok=True)
        
        # Ruta completa del archivo original y destino
        ruta_origen_completa = os.path.join(ruta_origen, video)
        ruta_destino_completa = os.path.join(carpeta_destino, nuevo_nombre)
        
        # Mover el archivo
        shutil.move(ruta_origen_completa, ruta_destino_completa)
        videos_en_carpeta += 1
        print(f"Procesado: {video} -> {nuevo_nombre} (Carpeta {carpeta_actual})")

if __name__ == "__main__":
    # Solicitar la ruta al usuario
    ruta = input("Ingrese la ruta donde se encuentran los videos: ")
    
    # Verificar si la ruta existe
    if not os.path.exists(ruta):
        print("La ruta especificada no existe.")
    else:
        try:
            procesar_videos(ruta)
            print("\nProceso completado exitosamente.")
        except Exception as e:
            print(f"Error durante el proceso: {str(e)}") 