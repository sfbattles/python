# from django.http import Http404
# from django.shortcuts import render
# from django.http import HttpResponseNotFound, HttpResponseRedirect
# from django.urls import reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect 
from django.shortcuts import render, HttpResponse 
from django.urls import reverse 
from django.template.loader import render_to_string 
from django.http import Http404



# Create your views here.
monthly_challenges = {
    "January": "Happy New Year Baby",
    "February": "Walk 20 minutes a day",
    "March": "March is when you start planting in green house",
    "April": "Eat no Meat",
    "May": "Walk 20 minutes a day",
    "June": "March is when you start planting in green house",
    "July": "Eat no Meat",
    "August": "Walk 20 minutes a day",
    "September": "March is when you start planting in green house",
    "October": "Eat no Meat",
    "November": "Walk 20 minutes a day",
    "December": "ITs christmas time baby"
    }


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html" ,{
        "all_months" : months
    })

def monthly_challenge_by_number(request, month):
    print(f"current month {month}")
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge",
                            args=[redirect_month])  # /challenge/January
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        print(f"{challenge_text}")
        print(f"{month}")
        return render(request, 'challenges/challenge.html',{
            "text" : challenge_text,
            "selected_month" : month,
        }) 
    except:
        # return HttpResponseNotFound("<h1>This Month is not supported</h1>")
        raise Http404()
