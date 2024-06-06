import requests
from datetime import date

Fecha=date.today()
User='marc.lopezm@duocuc.cl'
Pass='Datenryu7.'
tipos=['Yen','Euro','Dolar']
Codigos=['F072.CLP.JPY.N.O.D','F072.CLP.EUR.N.O.D','F073.TCO.PRE.Z.D']
Cod='F072.CLP.EUR.N.O.D'
Moneda=''


#obtener valor de dollar de la api del banco central de chile
def Funcion_retorna():
  api_url=f"https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user={User}&pass={Pass}&firstdate={Fecha}&lastdate={Fecha}&timeseries={Cod}&function=GetSeries"
  try:
    response= requests.get(api_url)
    if response.status_code == 200:
      response_info = response.json()
      val = response_info['Series']['Obs'][0]['value']
      #val = response_info['value']
      return float(val)  #Asegúrate de que 'uf' es la clave correcta y que el tipo es convertible a float
      #return response_info
    else:
            print("Error al obtener la UF: HTTP ", response.status_code)
            return 0.0  # Devuelve un valor por defecto o maneja el error según sea necesario
  except Exception as e:
      print("Error al procesar la solicitud:", e)
      return 0.0



def convertir(a, b):
    resultado = a * b
    return resultado 
    
