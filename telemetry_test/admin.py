from django.contrib import admin
from .models import Document, TelemetryTest, Company, DocumentType

admin.site.register(Document)
admin.site.register(TelemetryTest)
admin.site.register(Company)
admin.site.register(DocumentType)
