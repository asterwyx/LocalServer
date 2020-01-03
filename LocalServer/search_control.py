from django.shortcuts import render
from django.http import HttpResponse
import DataSearch.models as dm
from DataSearch.models import Table16794231, Table6574487, Table1351379, Table23172676
import re
table23172676 = dm.Table23172676()
table1351379 = dm.Table1351379()
table6574487 = dm.Table6574487()
table16794231 = dm.Table16794231()


# database operation
def result_form(request):
    context = {}
    request.encoding = 'utf-8'
    if 'keyword' in request.GET and request.GET['keyword']:
        keyword = request.GET['keyword']
        response = ""
        regex = re.compile(keyword)
        up_name_list = dm.Upname.objects.all()
        for up in up_name_list:
            if regex.match(up.name):
                table_name = "Table" + str(up.uid)
                table = globals()[table_name]
                for row in table.objects.all():
                    response += "<p>" + row.title + "</p>"
                break
        context['result'] = response
    else:
        context['result'] = "Please set your filter."

    return render(request, 'result_form.html', context)
