from django.shortcuts import render
from django.conf import settings

# Create your views here.

def Form(request):
    return render(request, "form.html")

def contactar(request):
    if request.method =="POST":#SI LA INFO LLEGA POR POST (EL FORMULARIO)
        asunto=request.POST["txtAsunto"]#guarda en asunto lo que llegue por POST desde el input que nombramos txtAsunto
        mensaje=request.POST["txtMensaje"] + "/Email " + request.POST["txtEmail"]
#concatena en mensaje el el mensaje con lo que llega por /email, ese input recibia el mail
        email_desde= settings.EMAIL_HOST_USER #le llega un mail desde nuestro email (en settings configurado)
        email_para = ["ivanmacedonio778@gmail.com"]
        send_mail(asunto,mensaje, email_desde, email_para, fail_silently=False)
#send mail recibe por parametro (en orden) asunto mensaje quien envia, quien recibe y que falle sin mostrar error
        return render(request, "contactoexitoso.html") #si todo sale bien lo redireccionamos aca!
    return render(request, "form.html")#si no entra al post, que lo redirija al form 