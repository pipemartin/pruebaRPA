from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

""" Librerias a autilizar"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

""" Autor  """

""" 
    Autor: Juan Felipe Martin Diaz
    Dia de creacion: 08/16/2023
"""

""" Declaracion de Variables"""
website = 'https://es.wikipedia.org/wiki/Anexo:Ganadores_del_Premio_Nobel'
driver = webdriver.Edge()
driver.get(website)
df = {"years": [], "physical": [], "chemistry": [], "medicine": [], "literature": [], "peace": []}

""" 
    Se recorre mediante un ciclo for las etiquetas de la tabla de wikipedia
"""
for i in range(1,122):
    """ 
        Se implementa el try para el manejo de error de webdriverwait al momento de no encontrar la etiqueta 
        definida
    """
    try:
        years_nobel = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,f'//table/tbody/tr[{i}]/td[1]'))).text
        df['years'].append(years_nobel)
    except TimeoutException:
        """ 
            si hay un error se manda una excepcion u procedimiento a seguir a ese error
        """
        print("Error no encontro etiqueta tiempo")
    try:
        physical_nobel = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,f'//table/tbody/tr[{i}]/td[2]/span[2]'))).text
        df['physical'].append(physical_nobel)
    except TimeoutException:
        """ 
            al momento de no encontrar la etiqueta se lanza la excepcion para la siguiente busqueda de etiqueta
            con una nueva ruta
        """
        try:
            physical_nobel = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,f'//table/tbody/tr[{i}]/td[2]/a'))).text
            df['physical'].append(physical_nobel)
        except TimeoutException:
            """ 
                Si con la nueva ruta no se encuentra la etiqueta con el valor, se procede a rellenar el espacio 
                con el valor null. ya que no se encontro un valor a agregar.
            """
            df['physical'].append("null")
            print("Error no encontro etiqueta physical")
    try:
        chemistry_nobel = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,f'//table/tbody/tr[{i}]/td[3]/span[2]'))).text
        df['chemistry'].append(chemistry_nobel)
    except TimeoutException:
        try:
            chemistry_nobel = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,f'//table/tbody/tr[{i}]/td[3]/a'))).text
            df['chemistry'].append(chemistry_nobel)
        except TimeoutException:
            df['chemistry'].append("null")
            print("Error no encontro etiqueta chemistry")
    try:
        medicine_nobel = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,f'//table/tbody/tr[{i}]/td[4]/span[2]'))).text
        df['medicine'].append(medicine_nobel)
    except TimeoutException:
        try:
            medicine_nobel = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,f'//table/tbody/tr[{i}]/td[4]/a'))).text
            df['medicine'].append(medicine_nobel)
        except TimeoutException:
            df['medicine'].append("null")
            print("Error no encontro etiqueta medicine")
    try:
        literature_nobel = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,f'//table/tbody/tr[{i}]/td[5]/span[2]'))).text
        df['literature'].append(literature_nobel)
    except TimeoutException:
        try:
            literature_nobel = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,f'//table/tbody/tr[{i}]/td[5]/a'))).text
            df['literature'].append(literature_nobel)
        except TimeoutException:
            df['literature'].append("null")
            print("Error no encontro etiqueta literature")
    try:
        peace_nobel = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,f'//table/tbody/tr[{i}]/td[6]/span[2]'))).text
        df['peace'].append(peace_nobel)
    except TimeoutException:
        try:
            peace_nobel = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,f'//table/tbody/tr[{i}]/td[6]/a'))).text
            df['peace'].append(peace_nobel)
        except TimeoutException:
            df['peace'].append("null")
            print("Error no encontro etiqueta peace")


""" 
    Luego de manejar cada excepcion del ciclo u de las etiquetas de la pagina, 
    se procede a cerrar el browser
"""
driver.quit()
#print(df)
""" 
    a continuacion, el arreglo df procede a convertirse en data frame con la ayuda de la libreria pandas
"""
df = pd.DataFrame(df)
""" 
    Por ultimo, el data frame creado pasa ser guardado en un archivo csv con el nombre de prizesNobels
"""
df.to_csv('prizesNobels.csv', index=False)

