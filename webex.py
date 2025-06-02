import requests
import json

token = 'ZWZiM2FlMTgtNjU2OS00M2I5LTk2NGEtNGQ3YjUyOGEwOTU3MzA2MjE0ZjUtN2Vm_PE93_9fb05950-2b1b-4484-b5a5-670447d3d114' #aquí va el token
idsala= 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZjVlMDY5YjAtOGExNy0xMWVlLThiMTgtZGQ4MWYyYjQ4ZGZm' #sala 
mensaje=input("Escriba el mensaje enviado: ")
url= 'https://webexapis.com/v1/messages' #url de la apide webex
headers= {'Authorization':'Bearer ' + token,
         'Content-Type':'application/json'}
data= {
    'roomId': idsala,
    'text': mensaje}

resp_envio = requests.post(url, headers=headers, json=data)

if resp_envio.status_code == 200:
    print(" Mensaje enviado correctamente.\n")
    op=input("¿Desesas ver los mensajes recientes?(si/no): ")
    if op == 'si':
        # Obtener el roomId desde la respuesta
        room_id = resp_envio.json().get('roomId')
        if not room_id:
            print(" No se pudo obtener el ID de la sala desde la respuesta.")
        else:
            # Obtener mensajes recientes de esa sala
            url_mensajes = f'https://webexapis.com/v1/messages?roomId={room_id}'
            resp_mensajes = requests.get(url_mensajes, headers=headers)

            if resp_mensajes.status_code == 200:
                mensajes = resp_mensajes.json().get('items', [])
                print("\n Mensajes recientes en la sala:\n")
                for msg in mensajes:
                    persona = msg.get('personEmail', 'Desconocido')
                    texto = msg.get('text', '[Mensaje sin texto]')
                    print(f"{persona} escribio: {texto}")
            else:
                print("Error al obtener los mensajes de la sala:", resp_mensajes.text)
    else:
        print("Hasta luego!!!!")
else:
     print("Error al enviar el mensaje:", resp_envio.text)

