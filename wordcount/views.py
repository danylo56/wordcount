from django.shortcuts import render
from django.http import HttpResponse
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fullText = request.GET['fullText']
    world_list = fullText.split()
    word_dictionary = {}

    for word in world_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # Add to the dictionary
            word_dictionary[word] = 1

        sortedWords = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',
                  {'fullText': fullText, 'count': len(world_list), 'sortedWords': sortedWords})

def about(request):
    return HttpResponse('<center><h1>Made by Danylo Zakharchenko</h1></center>')