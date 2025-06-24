from django.shortcuts import render
from django.http import HttpResponse

def show_feed(reqeust):
    return HttpResponse("show feed")
# Create your views here.

def one_feed(reqeust, feed_id, feed_content):
    return HttpResponse(f"feed id: {feed_id}, {feed_content}")

def all_feed(reqeust):
    return HttpResponse("all feed")