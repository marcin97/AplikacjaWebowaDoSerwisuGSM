import io

from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas

# Create your views here.
from main.models import Repair


@staff_member_required
def generatePDF(request, id):
    buffer = io.BytesIO()
    x = canvas.Canvas(buffer)
    result = Repair.objects.filter(id=id)
    x.drawString(100, 100, f"{result}")
    x.showPage()
    x.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'{result}.pdf')


@staff_member_required
def sendMail(request, id):
    repair = Repair.objects.filter(id=id)
    client_mail = repair.client.mail
    mail = send_mail(
        'Seriws GSM',
        'Telefon został naprawiony, zapraszamy po odbiór',
        'from@example.com',
        [client_mail],
        fail_silently=False,
    )
    return HttpResponse(mail)
