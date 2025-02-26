from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Cantidad de elementos por página
    page_size_query_param = 'page_size'  # Permite cambiar el tamaño de página con un parámetro en la URL
    max_page_size = 100  # Límite máximo de elementos por página
