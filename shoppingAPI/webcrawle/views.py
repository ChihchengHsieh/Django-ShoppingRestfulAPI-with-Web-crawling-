from rest_framework.decorators import api_view
from rest_framework.response import Response
from webcrawle.crawlingFunction import crawleChemistWarehouse

@api_view()
def craw_chemistwarehouse(request):
    # This work
    return Response(crawleChemistWarehouse())

# Create your views here.
