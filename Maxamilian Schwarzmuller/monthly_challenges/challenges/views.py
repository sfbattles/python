from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.urls import reverse 
from django.template.loader import render_to_string
from django.http import Http404

monthly_challenges ={
    "january"  : "Eat no meat for the entire year",
    "february" : "Walk for at least 20 minutes every day",
    "march"    : "Learn Django for at least 20 minutes every day",
    "april"    : "April - Learn Django for at least 20 minutes every day",
    "may"      : "May - Learn Django for at least 20 minutes every day",
    "june"     : "June - Learn Django for at least 20 minutes every day",
    "july"     : "July - Learn Django for at least 20 minutes every day",
    "august"   : "August - Learn Django for at least 20 minutes every day",
    "september": "September - Learn Django for at least 20 minutes every day",
    "october"  : "October - Learn Django for at least 20 minutes every day",
    "november" : "November - Learn Django for at least 20 minutes every day",
    "december" : None,
}


# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    list_url = ""
    list_dict = {}

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        
        list_url += f"<li><a href={month_path}> {capitalized_month}</a> </li>"

        response_date = f"<li>{list_url}</li>"
        list_dict = {"months":months}

        # this way displays the html 12 times
        return render(request,"challenges/index.html",{
            "months": months
        })

    # return render(request,"challenges/index.html", list_dict)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    
    # return HttpResponse(f'<h1>{redirect_month}</h1>')
    redirect_path = reverse("month-challenge",  args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text} </h1>"
        response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, 'challenges/challenge.html', {
            "title": month,
            "text": challenge_text,
            "description" : month.capitalize() + " Challenge"
        })
    except:
        raise Http404()
        # there has to be a file called 404.html in the projects templates directory
        # in order to use the Http404() module
        
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
    
    
    # if month == "january":
    #     challenge_text = "<h3>Eat no meat for the entire month</h3>"
    # elif month == "february":
    #     challenge_text = "<h3>Walk for at least 20 minutes every day</h3>"
    # elif month == "march":
    #     challenge_text = "<h3>Learn Django for at least 20 minutes every day</h3>"
    # else:
    #     return HttpResponseNotFound(f"<h1>404 error - Month ( {month} ) was not found</h1>")

    # return HttpResponse(challenge_text)
