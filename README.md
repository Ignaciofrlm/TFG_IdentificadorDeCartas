El proyecto se ha desarrollado en Ubuntu-WSl, en un contenedor de docker.

Las carpetas contienen distintos archvos comprimidos por volumenes con el uso de 7zip. No son archivos necesarios ya que se pueden generar por medio del codigo pero si se quieren usar ya generados se pueden descomprimir con 7zip.
La carpeta de Modelos contiene un unico modelo que se debe extraer en la ruta ./Modelos
En la carpeta Nombre_Vectores se pueden descomprimir vectores.npy y nombres.npy que se deben incluir en la misma ruta que el jupyter notebook.
En la carpeta RealImg se pueden encontrar imagenes de ejemplo, la carpeta en la que se descompriman se debe definir en el codigo del notebook.

RealImg contiene imágenes tratadas y sin tratar de mis cartas.

ids.npy contiene todas las ids de las cartas.

TratamientoImagenes.ipynb es un notebook con el código del tratamiento de imágenes.

Modelo.ipynb es un notebook con el código del modelo.

ImgDownload.py es el código con el que se descargan las imágenes a través de un JSON descargado de la pagina de Scryfall(https://scryfall.com/docs/api/bulk-data).

crearArchivos.py crea nombres.npy


