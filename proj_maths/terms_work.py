from proj_maths.models import Translations, Lessons

def get_all_words():
    words = []
    for item in Translations.objects.all():
        words.append([item.word_id, item.word, item.translation])
    return words

def get_all_lessons():
    lessons = []
    for item in Lessons.objects.all():
        lessons.append([item.lesson_id, item.date_lesson, item.theme, item.newwords])
    return lessons

def write_word(word, trans):
    term = Translations(word=word, translation = trans)
    term.save()

def write_lesson(date, theme, words):
    lesson = Lessons(date_lesson = date, theme = theme, newwords = words)
    lesson.save()

def delete_word():
    #delword = Translations.objects.get(-1)
    #delword.delete()
    Translations.objects.order_by('-word_id')[0].delete()

def delete_lesson():
    #delword = Translations.objects.get(-1)
    #delword.delete()
    Lessons.objects.order_by('-lesson_id')[0].delete()


def get_terms_stats():
    db_terms = 0
    user_terms = 0
    defin_len = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            term, defin, added_by = line.split(";")
            words = defin.split()
            defin_len.append(len(words))
            if "user" in added_by:
                user_terms += 1
            elif "db" in added_by:
                db_terms += 1
    stats = {
        "terms_all": db_terms + user_terms,
        "terms_own": db_terms,
        "terms_added": user_terms,
        "words_avg": sum(defin_len)/len(defin_len),
        "words_max": max(defin_len),
        "words_min": min(defin_len)
    }
    return stats
