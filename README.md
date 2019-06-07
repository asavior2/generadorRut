# generadorRut

El escript generadorRut.py les permitira generar un archivo con todos los rut Chilenos validos.

## Requerimientos 

En el Script se requiere el archivo "rut" este debe contener todos los rut poble sin el numero verificador y el ru2 archivo de salida.
```
archivoRut = open('rut', 'r')
```
Para generar el archivo de los RUT sin el numero verificador pueden utilizar la herramienta "crunch" con el siguiente comando: 
```
crunch 8 8 -t 6%%%%%%>>rut  //los 6 millones 
crunch 8 8 -t 7%%%%%%>>rut   //los 7 millones 
crunch 8 8 -t 8%%%%%%>>rut   //los 8 millones 
crunch 8 8 -t 9%%%%%%>>rut
crunch 8 8 -t 1%%%%%%%>>rut  //los 10 hasta 19 millones 
crunch 8 8 -t 2%%%%%%%>>rut  //los 20 hasta 30 millones 
Creo que a la actualidad va por los 27 millones. 
```
Para mayor informacion de `man crunch` 
