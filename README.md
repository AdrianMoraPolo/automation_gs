# Prueba Automatización - GENERAL SOFTWARE 
En este readme encontrarás:

- Una breve descripción sobre la estructura del proyecto
- Instalaciones necesarias
- Cómo lanzar el proyecto

### Descripción del proyecto

- EL proyecto realiza una búsqueda en google de la palabra deseada y comprueba los resultados para ver si superan o no la cantidad deseada
- He añadido segundos entre cada paso para que se pueda apreciar mejor la prueba, pero normalmente al lanzar un test de automatización primaría la velocidad. Por lo que esos segundos de espera no estarían implementados.
- Prioricé estructurar el proyecto de la forma más básica y eficaz para que se pueda diferenciar cada paso y no resulte complicado entender el funcionamiento

### Instalaciones necesarias
  Para poder lanzar los test correctamente es necesario tener instalado lo siguiente:
  - Descargar e instalar Python https://www.python.org/downloads/
  - Comprobar que lo tenemos instalado y que versión con: `python` en cmd
  - Instalar Selenium con `pip install selenium`
  - Actualizar Selenium en su directorio raiz con `python -m pip install --upgrade pip`
  - Instalar Visual Studio Code y añadir los siguientes pluggins:
    - Katalium Selenium
    - WebDriverIO snippets
  - Yo he añadido un archivo de Chromedriver a la carpeta "path" dentro del proyecto acorde a mi versión de Chrome. Yo tengo la "Versión 108.0.5359.125 (Build oficial) (64 bits)" En caso de que no funcione, comprobar la versión de chrome y descargar (no aparece la de x64, así que descargar la de win32
     ![image](https://user-images.githubusercontent.com/50373485/208441214-963e0fc3-76ee-4fce-aa8d-f92daf4849ed.png)
   ![image](https://user-images.githubusercontent.com/50373485/208441743-9b3ae51a-5043-4eb4-a70d-751f917fc452.png)
   - Instalamos Pycharm y creamos un nuevo proyecto 
   - Vamos a settings y añadimos los siguientes interpretes: "selenium", "pytest", "pytest-thml"
![image](https://user-images.githubusercontent.com/50373485/208442350-cfe9b4b1-2a5c-4396-9bb0-af80745c2106.png)

### Lanzar el proyecto
Con Pytest Html he añadido una funcionalidad para que cada vez que se ejecute un test se genere un archivo html que se puede abrir con Chrome o Firefox para ver el resultado de los test. Y en caso de que un test hubiese fallado podríamos ver el punto exacto y el motivo detallado.

![html](https://user-images.githubusercontent.com/50373485/208444724-eebca571-0e93-47d3-89c0-883d2a446a3e.jpg)
- test_end2end.py
  - Para lanzar "applesearch.py" debemos tener abierto el proyecto y en el ternimal escribimos `pytest .\applesearch.py  --html=Reporte_test` y se lanzará el test. Cuando finalice tendremos un reporte en el terminal y también se creará un archivo html llamado "Reporte_test". Además tendremos otra evidencia, un Screenshot que se guardará en la carpeta "Screenshots" llamado "screenshot.png"
  - Otra opción para lanzar "applesearch.py" es hacer click en el botón verde de RUN en Pycharm con el test seleccionado, pero no obtendremos el html de resultados
  - ¿Que hace exactamente este test? 
    - Abrimos el navegador de google.es
    - Buscamos "apple"
    - Extraemos la cantidad de resultados
    - Comparamos los resultados con 100000


 

