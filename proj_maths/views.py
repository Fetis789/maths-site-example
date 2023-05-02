from django.shortcuts import render
from django.core.cache import cache
from . import terms_work


def index(request):
    return render(request, "main_page.html")

def info(request):
    return render(request, "project_info.html")

def words_list(request):
    words = terms_work.get_all_words()
    return render(request, "words-list.html", context={"words": words})

def lesson_list(request):
    lessons = terms_work.get_all_lessons()
    return render(request, "lesson-materials.html", context = {"lessons": lessons})

def add_word(request):
    return render(request, "add-word.html")

def add_term(request):
    return render(request, "add-word.html")

def add_lesson(request):
    return render(request, "add-lesson.html")

def send_word(request):
    if request.method == "POST":
        cache.clear()
        word = request.POST.get("word")
        trans = request.POST.get("translation")
        context = {"word": word}
        if len(trans) == 0:
            context["success"] = False
            context["comment"] = "Перевод должен быть не пустым"
        elif len(word) == 0:
            context["success"] = False
            context["comment"] = "Слово должно быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            terms_work.write_word(word, trans)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)

def send_lesson(request):
    if request.method == "POST":
        cache.clear()
        date = request.POST.get("date")
        theme = request.POST.get("theme")
        words = request.POST.get("newwords")
        context = {"theme": theme}
        if len(date) == 0:
            context["success"] = False
            context["comment"] = "Нужно отобразить дату урока"
        elif len(theme) == 0:
            context["success"] = False
            context["comment"] = "Требуется указать тему урока"
        elif len(words) == 0:
            context["success"] = False
            context["comment"] = "Список слов не должен быть пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            terms_work.write_lesson(date, theme, words)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)

def delete_word(request):
    terms_work.delete_word()
    words = terms_work.get_all_words()
    return render(request, "words-list.html",context={"words": words})

def delete_lesson(request):
    terms_work.delete_lesson()
    lessons = terms_work.get_all_lessons()
    return render(request, "lesson-materials.html",context={"lessons": lessons})

def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)
