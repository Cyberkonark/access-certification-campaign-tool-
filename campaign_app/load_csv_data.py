import csv
from django.http import HttpResponse

def export_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="review_report.csv"'
    writer = csv.writer(response)
    writer.writerow(['User', 'App', 'Role', 'Status'])

    for entry in AccessEntry.objects.all():
        writer.writerow([entry.user.username, entry.application.name, entry.role, entry.status])
    
    return response
