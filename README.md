El proyecto se ha desarrollado en WSl-Ubuntu desde donde se ha levantado en un contenedor de docker, para usarse se recomienda levantar el docker, no es necesario que sea desde WSl-Ubuntu, aunque si se buildea desde Windows tensorflow no detectará las GPUs disponibles y el entreno será muy lento. En caso de que no se detecte la GPU o GPUs, se recomienda revisar este link: https://www.tensorflow.org/install/gpu.



Las carpetas contienen distintos archivos comprimidos por volúmenes con el uso de 7zip. No son archivos necesarios ya que se pueden generar por medio del código pero si se quieren usar ya generados se pueden descomprimir con 7zip.

La carpeta de Modelos contiene los pesos de un único modelo ya entrenado que se puede extraer en la ruta ./Modelos, en caso de que no se quiera entrenar el VAE.



En la carpeta Nombre\_Vectores se pueden descomprimir vectores.npy y nombres.npy que se deben incluir en la misma ruta que el jupyter notebook. También se pueden generar a partir del código, hay que tener en cuenta que estos archivos se generaron a partir del modelo ya entrenado que se encuentra en /Modelos, si se entrena de nuevo se deben generar desde cero.



En la carpeta RealImg se pueden encontrar imágenes de ejemplo, la carpeta en la que se descompriman se debe definir en el código del notebook.

ids.npy contiene todas las ids de las cartas. También se puede generar a partir del código.



Modelo.ipynb es un notebook con el código del modelo.

ImgDownload.py es el código con el que se descargan las imágenes a través de un JSON descargado de la pagina de Scryfall(https://scryfall.com/docs/api/bulk-data).

crearArchivos.py crea nombres.npy



