# Fantasy Maker

Este script permite replicar el procedimiento publicado en la Revista de la Escuela de Educación de Rosario (De Grande, 2025) para la generación de identificadores ficticios (de fantasía) a partir de identificadores de nueve dígitos (código único de establecimientos) de Argentina.

No debe utilizarse para generar listados en los que sea de interés mantener protegida la confidencialidad de la información, debido a que el procedimiento es fácilmente reversible.

## Datos

Se incluyen para poder realizar pruebas los listados de cueanexos publicados por el Ministerio de Educación en el mapa educativo (2014) y el Padrón de Establecimientos Educativos (2017 y 2021). En el caso de los últimos dos, las ubicaciones (latitud/longitud) fueron obtenidas por medio de pedidos de acceso a la información pública. 

Corresponde a los niveles inicial, primaria y secundario de todas las modalidades.

## Uso 

Para ejecutarlo, indicar:

> python3 fantasy-maker.py

Para utilizar diferentes archivos de entrada, editar las líneas finales del script fantasy-maker.py. El script espera archivos csv que contengan una columna 'cueanexo' de nueve dígitos, y produce un archivo de salida donde a las columnas existentes en el archivo de entrada agrega una columna adicional llamada 'id' con el identificador de fantasía de 15 dígitos.

## Propósito

Este script es parte de una publicación académica realizada para evaluar la fiabilidad de la protección de identificadores de establecimientos llevada adelante por el Ministerio de la Nación Argentina entre los años 2012 y 2022. Debido a la baja confiabilidad del esquema de protección, no debe utilizarse para proteger identificadores de información que se desea anonimizar, y se presenta aquí solo para fines ilustrativos de los hallazgos de la investigación realizada.

## Contacto

Para consultas o comentarios, escribir a Pablo De Grande (pablodg@gmail.com).

## Referencias

De Grande, Pablo (2025). Problemáticas en la difusión de datos educativos. El tratamiento de su confidencialidad en Argentina. e-ISSN: 2362-3349 - Revista de la Escuela de Ciencias de la Educación, 20 (1), 100-117 [https://revistacseducacion.unr.edu.ar/index.php/educacion/article/view/865]
