## COMO EJECUTAR PROYECTO
1. Decargar repositorio https://github.com/felipkmpo/busquedasemantica.
   
2. Desde ambiente de desarrollo (visual studio code)  o prompt deseado , abrir folder o carpeta que contiene los archivos del repositorio recien descargado.
   
3. Ejecutar terminal del ambiente de desarrollo o prompt, validamos que tengamos instalado python:
      - Desde el terminal podemos escribir "python --p", debera aparecernos la version del paquete, si no aparece debemos descargar el paquete de python dependiendo tu sistema, podras descargarlo en este enlace https://www.python.org/downloads/
        
        ![image](https://github.com/user-attachments/assets/48f917ed-80f4-43f6-a4a4-f1f54be39430)
        
        ***observacion:*** si por algun motivo, tienes python instalado pero tu terminal no reconoce los las variables de entorno debes configurarlas, puedes apoyarte con el siguiente tutorial https://www.youtube.com/watch?v=Fo-jkW8rPs8&ab_channel=divcode,
        se recomienda reiniciar el ambiente de desarrollo o el terminal para una correcta ejecucion e identificacion de las variables de entorno.
        
4. Procedemos con la instalacion de nuestro entorno virtual para eso utilizamos la herramienta ***"virtualenv"*** que podemos utilizar con python, mediante la siguiente instruccion "virtualenv --version" validamos si esta instalado, si no esta instalado utilizamos
   la instruccion "pip install virtualenv", y posteriormente validamos su correcta instalación:

 ![image](https://github.com/user-attachments/assets/7178b2e8-48f3-4ceb-ab25-5199dcbe454f)

5. A continuacion creamos nuestro entorno virtual, ejecutamos la instruccion "virtualenv env" donde ***env*** sera el nombre de nuestro entorno (se puede modificar a preferencia):

     ![image](https://github.com/user-attachments/assets/271bcd78-b0c6-446d-838b-a91a49736eb0)


    - Como observamos ha creado una carpeta nueva con el nombre de nuestro entorno, en este caso el nombre es ***env2***, y dicha carpeta tiene la siguiente estructura:
      
    ![image](https://github.com/user-attachments/assets/6e29acc1-bf92-49a4-b781-250d21a783e1)

   - Para poder activar nuestro entorno virtual debemos estar sobre el directorio ***Scripts*** y ejecutar la instruccion "Activate":
     
![image](https://github.com/user-attachments/assets/2dd5b0ab-0979-4fec-8f8a-0ff8cab841d4)

***observacion:*** Confirmamos que se esta ejecuanto correctamete nuestro entorno cuando la palabra ***env*** se habilita.

6. Para la correcta ejecucion de nuestro proyecto instalamos las librerias ***pandas y sentence-trasnformes***, por tal motivo ejecutamos las siguientes isntrucciones:
     - pip install pandas
     - pip install sentence-transformes

     ![image](https://github.com/user-attachments/assets/cfa828e6-ab34-4923-9109-e61165515882)

***observación:*** Con la instrucción "pip list", validamos que las librearias hayan quedado instaladas.

7. 
10. 

REQUERIMIENTOS
PYTHON 3.10 +
ENTORNO DESARROLLO (VISUAL STUDIO CODE)


CONFIGURANDO VIRTUALENV
