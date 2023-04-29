from django.shortcuts import render
from django.http import HttpResponse

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from gpt import chatGPT


def home(request):
    context = {
        "header": "Duc's GPT",
    }
    if request.method == "POST":
        name = request.POST.get("name")
        prompt_ans = chatGPT(name)
        context["name"] = name
        context["prompt_ans"] = prompt_ans
    return render(request, "home.html", context)
