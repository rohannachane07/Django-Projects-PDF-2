# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .models import Author, Book

def generate_pdf(request):
    # Fetch data for both authors and books
    authors = Author.objects.all()
    books = Book.objects.all()

    # Pass data to the PDF template
    context = {'authors': authors, 'books': books}
    pdf_data = render_to_string('pdf_template.html', context)

    # Generate PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="library_report.pdf"'
    pisa_status = pisa.CreatePDF(pdf_data, dest=response)

    if pisa_status.err:
        return HttpResponse('PDF generation error')
    return response
