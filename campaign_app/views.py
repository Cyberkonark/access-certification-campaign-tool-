@login_required
def review_access(request):
    entries = AccessEntry.objects.filter(manager=request.user)
    return render(request, 'review.html', {'entries': entries})


# Create your views here.
