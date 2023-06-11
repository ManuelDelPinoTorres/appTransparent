# importo request para poder realizar cominicaciones con otros servicios web o servidores externos
import requests
# importo socker para poder realizar obtener la resolucion de dns
import socket
from django.http import JsonResponse
from django.views import View

class MedirTiempoRespuestaView(View):
    def get(self,request,*args, **kwargs):
        dominio = request.GET.get('dominio', '')
        ip = request.GET.get('ip','')
        
            #validacion para comprobar si se ha introducido un dominio o ip 
        if dominio or ip:
            # validacion para actuar en caso de que haya una ip
             
            if ip:
                url=f'http://{ip}/'
            else:
                ip = socket.gethostbyname(dominio)
                url=f'http://{ip}/'
            
            try:
                # realizamos una peticion get a la url que hemos generado
                response=requests.get(url)
                # obtenemos el tiempo de respuesta y el codigo de respuesta
                tiempoRespuesta = response.elapsed.total_seconds()
                statusCode = response.status_code
                
                # almacenamos la informacion en un diccionario y la pasamos por json
                data={
                    'tiempoRespuesta':tiempoRespuesta,
                    'statusCode':statusCode
                }
                return JsonResponse(data)
            # recogemos la excepcion en caso de que no se pueda realizar la peticion
            
            except requests.exceptions.RequestException:
                data={
                    'error':'No se ha podido realizar la peticion'
                }
                return JsonResponse(data, status=500)
        else:
            data={
                'error':'Parametro del dominio faltante'
            }
            
            return JsonResponse(data, status=400)

