from django.db import models
from django.utils.translation import gettext_lazy as _
from pacientes.models import Paciente

class Diagnostico(models.Model):
    class Especialidad(models.TextChoices):
        alergia = "Alergia", _("Alergia")
        anatom_pat = "Anatomia Patologica", _("AnatomPat")
        cirugia = "Cirugia", _("Cirugia")
        geriatria = "Geriatria", _("Geriatria")
        ginecob = "Ginecob", _("Ginecob")
        imagenologia = "Imagenologia", _("Imag")
        labcli = "Lab_Clinico", _("Lab_Clinico")
        maxilo = "Maxilofacial", _("Maxilofacial")
        medicina_fis_rehab = "Med_Fis_Rehab", _("Med_Fis_Rehab")
        medicina_interna = "Med_Interna", _("Med_Interna")
        medicina_trabajo = "Med_Trabajo", _("Med_Trabajo")
        microbio = "Microbiologia", _("Microbiologia")
        nefrologia = "Nefrologia", _("Nefrologia")
        neurocirugia = "Neurocirugia", _("Neurocirugia")
        neurologia = "Neurologia", _("Neurologia")
        oftalmologia = "Oftalmologia", _("Oftalmologia")
        orl = "ORL", _("ORL")
        oncologia = "Oncologia", _("Oncologia")
        ortopedia = "Ortopedia", _("Ortopedia")
        proctologia = "Proctologia", _("Proctologia")
        psiquiatria = "Psiquiatria", _("Psiquiatria")
        quemado = "Quemado", _("Quemado")
        urologia = "Urologia", _("Urologia")
        reumatologia = "Reumatologia", _("Reumatologia")
        vdigest = "Vias_digestivas", _("VDigest")
    
    class Estado(models.TextChoices):
        grave = "Grave", _("Grave")
        levemente_grave = "Levemente grave", _("Levemente Grave")
    especialidad = models.CharField(max_length=255, choices=Especialidad)
    enfermedad = models.TextField(max_length=255)
    sintomas = models.TextField(max_length=450)
    estado = models.CharField(max_length=30, choices=Estado)
    paciente = models.OneToOneField(Paciente, on_delete=models.PROTECT, related_name='paciente', null=True, blank=True)
    class Meta:
        db_table = 'Diagnostico'
        verbose_name = 'diagnostico'
        verbose_name_plural = 'diagnosticos'
        ordering = ['especialidad']
        permissions = (("es_doctor", "Puede administrar"),)

    def __str__(self):
        return self.especialidad
