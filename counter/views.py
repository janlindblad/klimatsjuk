from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Quote


def get_client_ip(request):
    """Get the client's IP address from the request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def landing(request):
    """Landing page view for the counter app."""
    approved_quotes = Quote.objects.filter(approved=True)
    quote_count = 40 + sum(approved_quotes.values_list('days_count', flat=True)) or 0
    return render(request, 'counter/landing.html', {'quote_count': quote_count})


def planeten(request):
    """Den sjuka planeten page."""
    approved_quotes = Quote.objects.filter(approved=True)
    quote_count = 40 + sum(approved_quotes.values_list('days_count', flat=True)) or 0
    return render(request, 'counter/planeten.html', {'quote_count': quote_count})


def radd(request):
    """Jag är sjukt rädd page."""
    approved_quotes = Quote.objects.filter(approved=True)
    quote_count = 40 + sum(approved_quotes.values_list('days_count', flat=True)) or 0
    return render(request, 'counter/radd.html', {'quote_count': quote_count})


def systemet(request):
    """Det sjuka systemet page."""
    approved_quotes = Quote.objects.filter(approved=True)
    quote_count = 40 + sum(approved_quotes.values_list('days_count', flat=True)) or 0
    return render(request, 'counter/systemet.html', {'quote_count': quote_count})


def submit_quote(request):
    """Form page for submitting a new quote."""
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        days_count = int(request.POST.get('days_count', 1))
        
        if len(text) > 2000:
            return render(request, 'counter/submit_quote.html', 
                        {'error': 'Reflektionen får högst vara 2000 tecken lång.'})
        
        # Hash the IP address
        client_ip = get_client_ip(request)
        ip_hash = Quote.hash_ip(client_ip)
        
        # Create the quote
        Quote.objects.create(
            text=text,
            days_count=days_count,
            ip_hash=ip_hash,
            approved=False
        )
        
        return render(request, 'counter/quote_submitted.html')
    
    return render(request, 'counter/submit_quote.html')


@require_http_methods(["GET"])
def approved_quotes_api(request):
    """API endpoint to get all approved quotes."""
    quotes = Quote.objects.filter(approved=True).values('id', 'text')
    return JsonResponse(list(quotes), safe=False)
