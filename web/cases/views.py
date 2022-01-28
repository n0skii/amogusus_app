from django import http
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from .models import Case

from .forms import NativeCaseForm


def case_create_view(request: HttpRequest):
    form = NativeCaseForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()

    context = {"form": form}
    return render(request, "cases/case_create.html", context)


def case_detail_view(request: HttpRequest, ref_id: int):
    cur_case = get_object_or_404(Case, id=ref_id)
    context = {"object": cur_case}

    return render(request, "cases/case_detail.html", context)


def case_list_view(request: HttpRequest):
    query_list = Case.objects.all()
    context = {"object_list": query_list}

    return render(request, "cases/cases_list.html", context)
