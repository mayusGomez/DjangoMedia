from django.db import models


class Company(models.Model):
    """."""
    name = models.CharField(max_length=10, blank=True, null=True, verbose_name='Nombre')

    def __str__(self):
        """."""
        return '%s-%s' % (self.id, self.name)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class DocumentType(models.Model):
    """."""
    model = models.CharField(max_length=30)
    description_type = models.CharField(max_length=100)
    file_extension = models.CharField(max_length=10)
    file_size = models.IntegerField()
    folder_path = models.CharField(max_length=250)

    def __str__(self):
        """."""
        return '%s' % self.description_type

    class Meta:
        verbose_name = 'Document Type'
        verbose_name_plural = 'Document Types'


def directory_path(instance, filename):
    """."""
    file_path = '{0}/{1}'.format(instance.document_type_code.folder_path, 'test')
    return file_path


class DocumentManager(models.Manager):
    """."""

    id_company = None

    def __init__(self, model, company):
        """Init company"""
        super().__init__()
        self.model = model
        self.id_company = company

    def create(self, **kwargs):
        """."""
        kwargs['company'] = Company.objects.get(pk=self.id_company)
        return super().create(**kwargs)

    def get_queryset(self):
        """."""
        return super().get_queryset().filter(company=self.id_company)


class Document(models.Model):
    """."""
    document_type = models.ForeignKey(DocumentType, on_delete='DO_NOTHING')
    element_id = models.IntegerField(verbose_name="id_element")
    from_model = models.CharField(max_length=20)
    element_id_from_model = models.CharField(max_length=20)
    attachment_file = models.FileField(verbose_name="File", upload_to=directory_path, max_length=100)
    file_name = models.CharField(verbose_name="File name", max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    company = models.ForeignKey('Company', editable=False, on_delete='DO_NOTHING')

    all_objects = models.Manager()

    @classmethod
    def objects(cls, company):
        """Definir nuevo acceso a los objetos, evitando acceso total."""
        return DocumentManager(cls, company)

    def __str__(self):
        """."""
        return '%s' % self.file_name

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'


class TelemetryTest(models.Model):
    """."""
    date = models.DateTimeField()
    contractor = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    energy_meter = models.CharField(max_length=100)
    ip = models.CharField(max_length=20)
    port = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    imei = models.CharField(max_length=30)
    tc_relationship = models.CharField(max_length=5)
    tp_relationship = models.CharField(max_length=5)
