from django.http import HttpResponse
import datetime as dt
from django.template import Template, Context
from django.template import loader

def saludo (request):
    return HttpResponse('Hola Coder')

def segunda_vista(request):
    return HttpResponse('<br> Es facil, ya sabemos como hacer esto :) <br>')


def diahoy(request):
    #datetime.now() => muestra la fecha exacta actual
    dia = dt.datetime.now()
    txt = f'hoy es :<br> {dia} <br>'
    return HttpResponse(txt)


    

def Mi_nombre(self,nombre):
    texto = f'mi nombre es: <br><br> {nombre}'
    return HttpResponse(texto)




def probandoTemplate(self):

    html = open("E:\\Lucas\\programacion\\PROYECTOS\\Python\\Coder1\\ProyectoIntroductorio\\ProyectoIntroductorio\\plantillas\\template.html")

    plantilla = Template(html.read())

    
    html.close()

    contexto = Context()

    doc = plantilla.render(contexto)

    return HttpResponse(doc)


def Template_Mejorado(self):

    #creando variables
    name = 'Alejo'
    lastname = 'Juarez'
    dia = dt.datetime.now()
    notas = {2,3,3,7,2,8,8,9,5}

    diccionario = {"nombre" : name,
                   "apellido" : lastname,
                   "hoy" : dia,
                   "notas":notas,}
                   
    
    #html_mejorado = open("E:\\Lucas\\programacion\\PROYECTOS\\Python\\Coder1\\ProyectoIntroductorio\\ProyectoIntroductorio\\plantillas\\template.html")

    #plantilla = Template(html_mejorado.read())

    #html_mejorado.close()

    #contexto = Context(diccionario)

    #documento = plantilla.render(contexto)
    

    #AHORA DESDE ACA VEREMOS NUESTRO LOADER...
    plantilla = loader.get_template('template.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)



