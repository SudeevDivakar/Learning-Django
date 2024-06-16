from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# def january(request):
#     return HttpResponse('Eat more protein')

# def february(request):
#     return HttpResponse("Drink more water")

monthly_challenges = {
    'january': 'Eat more protein',
    'february': 'Drink more water',
    'march': 'Go to gym more',
    'april': 'Eat more veggies',
    'may': 'Have fun',
    'june': 'Learn Django',
    'july': 'Go to actuarial sciences course',
    'august': 'Watch World Cup',
    'september': 'Run more',
    'october': 'Finish capstone project',
    'november': 'Graduate',
    'december': None
}

def index(request):
    months = list(monthly_challenges.keys())
    # list_items = ""
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_url = reverse("month-challenge", args=[month])
    #     list_items += f'<li><a href="{month_url}">{capitalized_month}</a></li>'
    # responseMessage = f"""
    #     <ul>
    #         {list_items}
    #     </ul>
    # """
    # return HttpResponse(responseMessage)
    return render(request, "challenges/index.html", {
        "months": months
    })



def monthly_challenge_by_number(request, month):
    # try:
    #     return HttpResponse(list(monthly_challenges.values())[month-1])
    # except:
    #     return HttpResponseNotFound('This month is not supported')

    try:
        months = list(monthly_challenges.keys())
        redirectMonth = months[month-1]
        redirectPath = reverse("month-challenge", args=[redirectMonth])     #builds a path like /challenges/<month>    #for a path with multiple path params, we provide multiple values
        return HttpResponseRedirect(redirectPath)
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)



def monthly_challenge(request, month):
    try:
        challengeText = monthly_challenges[month]
        """Returning html text"""
        #responseData = f'<h1 style="color: blue">{challengeText}</h1>'
        """Converting html to string and returning as an http response"""
        # responseData = render_to_string("challenges/challenge.html")
        # return HttpResponse(responseData)
        """Directly rendering the html documents using the render function"""
        return render(request, "challenges/challenge.html",{
            "text": challengeText,
            "month": month
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()