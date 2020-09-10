#Este programa fue creado para la asignatura Programación (0790),
#dictada en la Universidad Central de Venezuela
#Autor : Carlos E. González C. github: c27gc
#Descripción: En este código se implementará una agenda telefónica básica, y
#tiene como fin único la enseñansa de Python, en particular la manipulación de
#archivos de texto.

#Para el nombramiento de las variables (objetos) se utilizará el estandar de nomenclatura
#recomendado en el PEP 8 de python. 
#más información en este link: https://www.python.org/dev/peps/pep-0008/


#Asignación: comente cada línea del código explicando que hace.

#Asignación: empaquete las funciones de este archivo en un módulo independiente.

def crear_contacto(agenda_path):
    """Esta función agrega un contacto a una agenda"""
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el telefono de {} :".format(nombre))
    direccion = input("Ingrese la dirección de {} :".format(nombre))

    contacto = {'Nombre':nombre, 'Telefono': telefono, 'Direccion': direccion}
    agenda = descargar_agenda(agenda_path)
    if len(agenda.keys()) == 0:
        id_contact = '0-0001'
    else:
        last_contact = int(list(agenda.keys())[-1].split('-')[-1])+1
        last_contact = (4-len(str(last_contact)))*'0'+str(last_contact)
        id_contact = '0-{}'.format(last_contact)

    agenda.update( {id_contact:contacto} )

    cargar_agenda(agenda_path,agenda)

def eliminar_contacto(agenda_path):
    """Esta función elimina un contacto de una agenda"""
    # Asinación : Hacer que los identificadores id se reacomoden cuando se elimine un contacto.
    Flag = True
    while Flag:
        nombre = input("Indique nombre (o parte del nombre) del contacto que desea eliminar de la agenda: ")
        agenda = descargar_agenda(agenda_path)
        print("Identifique el id del usuario que desea eliminar.")
        for element_key,element in buscar(agenda, nombre.lower()):
            print('id: {}\t nombre: {}'.format(element_key, element))

        id = input("Ingrese el id del contacto a eliminar de la agenda: ")
        
        agenda.pop(id)
        
        cargar_agenda(agenda_path,agenda)

        continuar =  input("Desea eleminar otro contacto? ( opciones 's' o 'n'):")
        if continuar.lower() == 'n':
            Flag = False
        elif continuar.lower() != 's':
            raise ValueError("Error, las opciones válidas son 's' o 'n'.")

    
# Asignación: agregar una función para editar un contacto.


def cargar_agenda(agenda_path, agenda):
    """La función cargar_agenda crea el archivo de texto donde se
    almacenará una agenda dada y escribe o sustituye su contenido. Se pasa
    como argumento la ruta donde está la agenda y la variable asociada al
    contacto a modificar."""

    with open(agenda_path+'.txt', 'wt') as file:
        count = 0
        for id, contenido in zip(agenda.keys(), agenda.values()):
            if count == 0:
                id_tag = 'id:{}'.format(id)
                count += 1
            else:
                id_tag = '\nid:{}'.format(id)

            file.writelines([id_tag,'\n\tContacto:{}'.format(contenido['Nombre']),\
            '\n\tTelefono:{}'.format(contenido['Telefono']),'\n\tDireccion:{}'.format(contenido['Direccion'])])



def descargar_agenda(agenda_path):
    """La función descargar_agenda busca el archivo de texto donde se
    encuentra almacenada una agenda dada y descarga su contenido. Se pasa
    como argumento la ruta donde está la agenda y la variable asociada al
    contacto a modificar."""
    agenda = {}
    with open(agenda_path+'.txt', 'r') as file:
        content = file.read().split('\n')
        for i in range(0,len(content),4):
            id = content[i].split(':')[1]
            nombre = content[i + 1].split(':')[1]
            telefono = content[i + 2].split(':')[1]
            direccion = content[i + 3].split(':')[1]
            contacto = {'Nombre': nombre, 'Telefono': telefono, 'Direccion': direccion}
            agenda.update( {id: contacto} )

    return agenda



def buscar(agenda, nombre):
    lista_id = []
    lista_nombre = []
    print(agenda.keys())
    for id in agenda.keys():
        if nombre.lower() in agenda[id]['Nombre'].lower():
            lista_id.append(id)
            lista_nombre.append(agenda[id]['Nombre'])

    return zip(lista_id, lista_nombre)

def main():
    """La función main es la instancia principal del programa, utiliza el tipo
    de dato dict para representar la agenda telefónica, así como para
    representar los contactos. Ejemplo:

        contacto1 = {'Nombre':'Carlos C. González E.', 'Telefono': '+58 0412 223
        1222', 'Direccion': 'Colinas de Bellomonte.'}

        contacto2 = {'Nombre':'Pedro P. McFly D.', 'Telefono': '+58 0413 333
        1442', 'Direccion': 'El Recreo.'}

        agenda = {'0-0001': contacto1, '0-0002': contacto2}"""
    # Asignación: agregar una opcion para mostrar un resumen del calendario en la consola,
    # este resumen debe estar formateado para facilitar su lectura.
    with open("agenda.txt", "w"):
        pass
    
    while(True):
        accion = input("Quiere crear o eliminar un contacto? (Escriba 'crear' o 'eliminar'): ")

        if accion.lower() == 'crear':
            crear_contacto('agenda')
        elif accion.lower() == 'eliminar':
            eliminar_contacto('agenda')
        else:
            raise ValueError("Error, opción no válida. Las opciones válidas son crear y editar.")

        
if __name__ == '__main__':
    main()

