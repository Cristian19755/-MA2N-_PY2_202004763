# -MA2N-_PY2_202004763

Requisitos:

    Formato de Audio: Los programas están diseñados para trabajar con archivos de audio en formato WAV. Este formato permite acceder a los archivos de audio sin requerir herramientas externas al sistema operativo.

    Versión de Python: Se requiere una versión de Python igual o superior a 3.6. Puede descargar Python desde el sitio oficial de Python.

    Instalación de Bibliotecas: Es necesario instalar las bibliotecas necesarias. Esto se puede lograr utilizando el siguiente comando en una consola de PowerShell:


    pip install numpy matplotlib tkinter wave

    Recomendación de IDE: Se recomienda el uso de Visual Studio Code (VSCode) como entorno de desarrollo para ejecutar los programas. Puede descargar VSCode desde el sitio web oficial de VSCode

Uso de Programa 1 - Efecto de Eco:

El programa efectuará la compresión de audio siguiendo estos pasos:

    Se leerá el archivo de audio en formato WAV especificado.

    Luego, calculará la Transformada de Fourier del audio.

    Se conservarán únicamente las componentes de frecuencia más significativas de acuerdo al factor de compresión especificado.

    Posteriormente, realizará la Transformada Inversa de Fourier para obtener el audio comprimido.

    El audio comprimido se guardará en un archivo de salida con el nombre "output_compressed.wav".

    Se mostrarán gráficos que permitirán visualizar tanto la transformada inversa como la función original.

    El rango del eje y se normalizará con el propósito de facilitar la visualización.

    Finalmente, se imprimirá un mensaje indicando que el archivo de audio comprimido se ha guardado exitosamente.

Uso de Programa 2 - Lectura y Compresión de Audio:

Al ejecutar el programa, se llevarán a cabo las siguientes acciones:

    Se mostrarán dos gráficos. Uno de ellos representará el espectro de frecuencia del audio, aparentemente constante para el oído humano, mientras que el otro mostrará el resultado de aplicar la Transformada Rápida de Fourier al audio.

    Un control deslizante (slider) estará presente y se inicializará con una frecuencia de 440 Hz. Este control deslizante permite ajustar la frecuencia que se aplicará al audio.

    En la parte inferior de la ventana, se encontrarán dos botones:

        "Guardar Audio": Al presionar este botón, se generará y guardará un archivo de audio en formato WAV. La frecuencia seleccionada en el slider se aplicará al audio resultante.

        "Cerrar Aplicación": Se recomienda utilizar este botón para cerrar la aplicación de manera apropiada.

