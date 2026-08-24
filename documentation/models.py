import pymupdf
from django.core.files.base import ContentFile
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Document(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    pdf = models.FileField(
        upload_to="documentation/pdfs/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
    )
    preview_image = models.ImageField(
        upload_to="documentation/previews/", blank=True, editable=False
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="documents")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        regenerate_preview = self._needs_preview_regeneration()
        super().save(*args, **kwargs)
        if regenerate_preview:
            self._generate_preview()
            super().save(update_fields=["preview_image"])

    def _needs_preview_regeneration(self):
        if not self.pk:
            return True
        if not self.preview_image:
            return True
        # PDF file replaced with a new one
        previous = Document.objects.filter(pk=self.pk).values_list("pdf", flat=True).first()
        return previous != self.pdf.name

    def _generate_preview(self):
        self.pdf.open("rb")
        pdf_bytes = self.pdf.read()
        self.pdf.close()

        with pymupdf.open(stream=pdf_bytes, filetype="pdf") as doc:
            page = doc.load_page(0)
            pixmap = page.get_pixmap()
            png_bytes = pixmap.tobytes("png")

        filename = f"{slugify(self.title) or self.pk}.png"
        self.preview_image.save(filename, ContentFile(png_bytes), save=False)