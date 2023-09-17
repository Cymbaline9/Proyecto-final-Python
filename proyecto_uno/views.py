from django.http import HttpResponse
from django.template import Template, Context, loader

#con cargador de template
def template (request):
    datos = {"nombre":"Pepe", "notas":[2, 4, 6, 8, 1]}
    plantilla = loader.get_template("template.html")
    documento = plantilla.render(datos)
    return HttpResponse (documento)




"""
#sin cargador de template
def template (request):
    #lee el html
    plantilla = open ("C:/Users/sabrina.e.tabares/Documents/Python - Coderhouse/django/proyecto1/proyecto1/plantillas/template.html")
    #el html lo convierte en template de django
    plant = Template (plantilla.read())
    plantilla.close()

    #creo un contexto (puede ser esto o algo que venga de la db por ej)
    mi_contexto = Context ({"nombre":"Pepe", "notas":[2, 4, 6, 8, 1]})

    #le mando el contexto al template
    documento = plant.render(mi_contexto)

    #le manda todo preparado al user
    return HttpResponse (documento)
"""