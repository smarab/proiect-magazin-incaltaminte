# LABORATORUL 1 - CERINTA 8: Middleware pentru obtinerea IP-ului
class Middleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        str_lista_ip = request.META.get("HTTP_X_FORWARDED_FOR")

        if str_lista_ip:
            request.ip_client = str_lista_ip.split(",")[-1].strip()
        else:
            request.ip_client = request.META.get("REMOTE_ADDR")

        response = self.get_response(request)
        return response