Género_Arg
======================

Para correr el programa desde línea de comando, sólo vamos a necesitar un archivo CSV que vamos a leer como input. Como resultado obtendremos un archivo *'output.csv'*. Ejemplo:

`
python3 genero_arg.py --input 'test.csv'
`

Dentro del programa se encuentran dos funciones:

***Género:*** Identifica género a partir del primer nombre de la persona. La base utilizada para inferir género fue obtenida utilizando el [Registro Civil de la Ciudad de Buenos Aires](http://www.buenosaires.gob.ar/areas/registrocivil/nombres/busqueda/buscador_nombres.php?menu_id=16082).

***GéneroCSV:*** Permite recorrer un documento CSV, donde se espera un listado de nombres en la primer columna. Como resultado se obtiene un CSV con una columna adicional de género.

Para más información sobre la brecha de género en la industria IT, [Chicas en Tecnología](https://www.chicasentecnologia.org/) (CET) y [Medallia](http://www.medallia.com.ar) realizaron este estudio: [https://mujeresprogramadoras.com.ar/](https://mujeresprogramadoras.com.ar/)
