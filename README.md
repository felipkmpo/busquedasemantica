## COMO EJECUTAR PROYECTO

***Proyecto buscador de peliculas semantico*** este proyecto permite a un usuarios obtener recomendaciones sobre peliculas, el usuario debe ingresar la tematica o descripcion corta sobre una pelicula y el proyecto le mostrará en pantalla varias resultados, que contiene peliculas relacionadas con dicha tematica o descripcion, tambien mostrará informacion relevante sobre la misma (reparto, director y descripción).

1. Decargar repositorio https://github.com/felipkmpo/busquedasemantica, descargar los archivos de la carpeta ***"src"***
   
2. Desde el ambiente de desarrollo (visual studio code)  o prompt deseado , abrir folder o carpeta que contiene los archivos del repositorio recien descargado.
   
3. Ejecutar terminal en ambiente de desarrollo o prompt, validamos que tengamos instalado python:
      - Desde el terminal podemos escribir "python --p", debera aparecernos la version del paquete, si no aparece debemos descargar el paquete de python dependiendo tu sistema, podras descargarlo en este enlace https://www.python.org/downloads/
        
        ![image](https://github.com/user-attachments/assets/48f917ed-80f4-43f6-a4a4-f1f54be39430)
        
        ***observacion:*** si por algun motivo, tienes python instalado pero tu terminal no reconoce los las variables de entorno debes configurarlas, puedes apoyarte con el siguiente tutorial https://www.youtube.com/watch?v=Fo-jkW8rPs8&ab_channel=divcode, se recomienda reiniciar el ambiente de desarrollo o el terminal para una correcta ejecucion e identificacion de las variables de entorno.
        
4. Procedemos con la instalacion de nuestro entorno virtual para eso utilizamos la herramienta ***"virtualenv"*** que podemos utilizar con python, mediante la siguiente instruccion "virtualenv --version" validamos si esta instalado, si no esta instalado utilizamos la instruccion "pip install virtualenv", y posteriormente validamos su correcta instalación:

 ![image](https://github.com/user-attachments/assets/7178b2e8-48f3-4ceb-ab25-5199dcbe454f)

5. Para la correcta ejecucion de nuestro proyecto se instalaron las librerias ***pandas y sentence-trasnformes***, el archivo "requerimientos.txt" esta disponible dentro de la carpeta ***src*** para la instalacion de las dependencias requeridas para ejecutar el proyecto, esto lo podemos hacer ejecutando el comando "pip install - requerimientos.txt" mediante terminal, de esta manera garantizamos que todas las dependencias necesarias para la ejecucion de nuestro proyecto se instalen en la maquina.

6. A continuacion creamos nuestro entorno virtual, ejecutamos la instruccion "virtualenv env" donde ***env*** sera el nombre de nuestro entorno (se puede modificar a preferencia):

    ![image](https://github.com/user-attachments/assets/271bcd78-b0c6-446d-838b-a91a49736eb0)


    - Como observamos ha creado una carpeta nueva con el nombre de nuestro entorno, en este caso el nombre es ***env2***, y dicha carpeta tiene la siguiente estructura:
      
    ![image](https://github.com/user-attachments/assets/6e29acc1-bf92-49a4-b781-250d21a783e1)

   - Para poder activar nuestro entorno virtual debemos estar sobre el directorio ***Scripts*** y ejecutar la instruccion "Activate":
     
    ![image](https://github.com/user-attachments/assets/2dd5b0ab-0979-4fec-8f8a-0ff8cab841d4)

***observacion:*** Confirmamos que se esta ejecutando correctamete nuestro entorno cuando la palabra ***env*** se habilita.


7. Ahora continuamos con la ejecucion de nuestro proyecto, para eso debemos ejecutar el archivo .py con nombre "busquedasemantica.py", en el terminal nos situamos sobre el directorio src y ejecutamos el siguiente comando ***"python busquedasematica.py"*** :

![image](https://github.com/user-attachments/assets/e870df14-0f0c-4b94-aa94-deeff6d12d4b)

   - el usuario deberá escribir una descripcion deseada y presionar enter para que el programa arroje los resultados:

     ![image](https://github.com/user-attachments/assets/863bdced-89ba-4ac7-9cf2-b65062d6b289)

   - si el usuario no desea realizar mas busquedas debe escribir la palabra ***"salir"*** de esta manera el programa detendrá la busqueda:

     ![image](https://github.com/user-attachments/assets/1651476f-2cf5-4330-99da-d2c84f5569ee)



