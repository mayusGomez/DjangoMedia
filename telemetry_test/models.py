from django.db import models
import hashlib
from django.core.files.storage import Storage


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
    folder_path = models.CharField(max_length=10)
    sub_folder_path = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        """."""
        return '%s' % self.description_type

    class Meta:
        verbose_name = 'Document Type'
        verbose_name_plural = 'Document Types'


def directory_path(instance, filename):
    """."""

    # In COR_PARAMETER, add a new parameter by company, in this repo is a dict
    base_folder_by_company = {
        1: 'ftpettc',
        5: 'ftpnrcc'
    }

    #  Concat filename with time for generate new_name
    filename_new = '{}{}'.format(filename, instance.date.strftime('%H:%M:%S'))
    filename_new = hashlib.md5(filename_new.encode()).hexdigest()

    company = base_folder_by_company[instance.company.id]
    file_path = '{}/{}/'.format(company, instance.document_type.folder_path)

    sub_folder_list_conf = instance.document_type.sub_folder_path.split(',') \
        if instance.document_type.sub_folder_path else []
    sub_folder_list = instance.folder_params.split(',') \
        if instance.folder_params else []
    sub_folder = ''

    # validate sub_folder structure
    if sub_folder_list_conf and len(sub_folder_list) == len(sub_folder_list_conf):
        storage = Storage()
        for sub_folder_item in sub_folder_list:
            valid_sub_folder = storage.get_valid_name(sub_folder_item)
            if valid_sub_folder != '':
                sub_folder += '{}/'.format(valid_sub_folder)
            else:
                # if not is a valid subfolder, dicard subfolder
                sub_folder = ''
                break

    file_path += sub_folder
    file_path += filename_new
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
    company = models.ForeignKey('Company', on_delete='DO_NOTHING')
    folder_params = models.CharField(max_length=100, null=True, blank=True)

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
