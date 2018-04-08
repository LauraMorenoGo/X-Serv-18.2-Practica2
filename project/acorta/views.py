from django.shortcuts import render
from django.http import HttpResponse
from .models import urls
from django.views.decorators.csrf import csrf_exempt



def Formulario():
    formulario = """
    <form action="" method="POST">Introduzca la URL que desea acortar:<br><input type="text" name="url" placeholder="URL a acortar"><br><input type="submit" value="Enviar"></form> 
    """
    return formulario
    


@csrf_exempt
def Process(Request,resource):

    formulario = Formulario()
    ident = 0


    if Request.method == "GET":
        if resource == "":

            lista = urls.objects.all()
            respuesta = "<html>ACORTADOR DE URLS:<br></html>"
            for entry in lista:
                respuesta += "<li>URL ORIGINAL: " + entry.url_original + "   URL ACORTADA: http://localhost:1234/" + str(entry.url_acortada)
                ident= str(entry.url_acortada)

            htmlAnswer = "<html><body>" + formulario + "<br>" + respuesta + "</body></html>"

        else:   #REDIRECCIONES
            try:
                urlguardada = urls.objects.get(url_original=resource)
                htmlAnswer = "<html><body><meta http-equiv='refresh'" + "content='1 url=" + urlguardada + "'>" + "</p></body></html>"

            except urls.DoesNotExist:
                urlguardada = urls.objects.get(url_acortada=resource)
                htmlAnswer = "<html><body><meta http-equiv='refresh'" + "content='1 url=" +	urlguardada.url_original + "'>" + "</p></body></html>"

            except ValueError:
                htmlAnswer = "<html><body>ERROR RECURSO NO DISPONIBLE</body></html>"

    elif Request.method == "POST":
        url = Request.POST['url']

        if url == "":   #Cuerpo vacío
            returnCode = "404 Not Found"
            htmlAnswer = "<html><body>ERROR 400 Resource not found!\n</body></html>"
            return HttpResponse(htmlAnswer)

        elif url.find("http") == -1:    #No encuentra la url ya que no tiene http y ahora se lo añadimos
            url = "http://" + url


        htmlAnswer = "<html><body>" + url + "</body></html>"

        try:
        
            urlguardada = urls.objects.get(url_original=url)
            ident = urlguardada.url_acortada

        except:
        
            lista = urls.objects.all()
            for i in lista:
                ident= str(i.url_acortada)

            ident = int(ident) + 1 
            bd = urls(url_original=url, url_acortada=ident)    #Guardamos en base de datos
            bd.save()


        htmlAnswer ="<html><body>URL ORIGINAL:   <a href=" + url + ">" + url + "</a>      URL ACORTADA: <a href=" + str(ident) + ">http://localhost:1234/" + str(ident) + "</a>\n" + "<p><a href='http://127.0.0.1:8000/'>Volver al formulario</a></p></body></html>"

    else:

        htmlAnswer = "<html><body>ERROR</body></html>"
    
    return HttpResponse(htmlAnswer)
