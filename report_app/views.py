from django.shortcuts import render


def report(request):
    r = "This is the report main page."
    context = {"main_sentence": r}
    return render(request, "report_app/report_page.html", context)


def capital_goods(request):
    r = "This is the capital goods main page."
    context = {"main_sentence": r}
    return render(request, "report_app/report_page.html", context)
