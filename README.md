# Separador de Videos

Este proyecto permite organizar y renombrar automáticamente archivos de video en carpetas de hasta 5 elementos, añadiendo hashtags personalizados al nombre de cada archivo. Es ideal para preparar lotes de videos para subir a redes sociales o plataformas de contenido.

## Características
- Renombra los videos agregando hashtags personalizados.
- Organiza los videos en carpetas numeradas, con un máximo de 5 videos por carpeta.
- Si ya existen carpetas, el script continúa llenando la última carpeta incompleta antes de crear nuevas.
- Compatible con archivos `.mp4`, `.avi`, `.mkv` y `.mov`.

## Requisitos
- Python 3.7 o superior
- (Opcional) PyInstaller para crear un ejecutable portable

## Instalación
1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias (solo Python estándar).

## Uso
1. Coloca los videos que deseas organizar en una carpeta.
2. Ejecuta el script desde la terminal o doble clic si usas el ejecutable.
3. Ingresa la ruta de la carpeta donde están los videos cuando el programa lo solicite.
4. El script creará una subcarpeta llamada `subir` y organizará los videos en carpetas numeradas dentro de ella.

### Ejemplo de ejecución en terminal
```sh
python procesar_videos.py
```

### Ejemplo de estructura generada
```
/videos_a_organizar
├── video1.mp4
├── video2.avi
└── ...

/videos_a_organizar/subir
├── 1
│   ├── video1 #peliclips #peliculas #series.mp4
│   └── ...
├── 2
│   └── ...
└── ...
```

## Compilación a ejecutable portable (Windows)
1. Instala PyInstaller:
   ```sh
   pip install pyinstaller
   ```
2. Genera el ejecutable:
   ```sh
   pyinstaller --onefile procesar_videos.py
   ```
   El archivo `.exe` estará en la carpeta `dist`.

## Notas adicionales
- Si la carpeta `subir` ya existe y contiene carpetas numeradas, el script continuará llenando la última carpeta incompleta antes de crear nuevas.
- El script no sobrescribe archivos existentes con el mismo nombre en las carpetas destino.
- Puedes modificar los hashtags editando la línea correspondiente en el script.

## Licencia
Este proyecto se distribuye bajo la licencia MIT.

---

# Video Separator (English)

This project automatically organizes and renames video files into folders of up to 5 items, adding custom hashtags to each file name. It is ideal for preparing batches of videos to upload to social networks or content platforms.

## Features
- Renames videos by adding custom hashtags.
- Organizes videos into numbered folders, with a maximum of 5 videos per folder.
- If folders already exist, the script continues filling the last incomplete folder before creating new ones.
- Compatible with `.mp4`, `.avi`, `.mkv`, and `.mov` files.

## Requirements
- Python 3.7 or higher
- (Optional) PyInstaller to create a portable executable

## Installation
1. Clone this repository or download the files.
2. Install the necessary dependencies (only standard Python).

## Usage
1. Place the videos you want to organize in a folder.
2. Run the script from the terminal or double-click if using the executable.
3. Enter the path to the folder where the videos are located when prompted.
4. The script will create a subfolder called `subir` and organize the videos into numbered folders inside it.

### Example of terminal execution
```sh
python procesar_videos.py
```

### Example of generated structure
```
/videos_to_organize
├── video1.mp4
├── video2.avi
└── ...

/videos_to_organize/subir
├── 1
│   ├── video1 #peliclips #peliculas #series.mp4
│   └── ...
├── 2
│   └── ...
└── ...
```

## Build a portable executable (Windows)
1. Install PyInstaller:
   ```sh
   pip install pyinstaller
   ```
2. Generate the executable:
   ```sh
   pyinstaller --onefile procesar_videos.py
   ```
   The `.exe` file will be in the `dist` folder.

## Additional notes
- If the `subir` folder already exists and contains numbered folders, the script will continue filling the last incomplete folder before creating new ones.
- The script does not overwrite existing files with the same name in the destination folders.
- You can modify the hashtags by editing the corresponding line in the script.

## License
This project is licensed under the MIT License. 