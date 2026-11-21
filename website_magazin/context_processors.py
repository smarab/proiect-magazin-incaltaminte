from django.conf import settings
from datetime import datetime

# LABORATORUL 2 - TASK 2, CERINTA 6: Context processor pentru datele firmei si copyright
def date_firma(request):
    return {
        "date_firma": settings.DATE_FIRMA,
        "ip_client": request.ip_client,
        "copyright": f"© {datetime.now().year} {settings.DATE_FIRMA['nume']}. Toate drepturile rezervate."
    }