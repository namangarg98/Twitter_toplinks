from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
import sys
import tweepy
import twitter
import time
import timedelta
import requests
import datetime
from .models import Tweet


def home(request):
    return render(request, 'home.html')


def loginn(request):
    consumer_key = 'HGFIpUlpaoaVrH4JVvWc53FXv'  # App ID
    consumer_secret = 'JIyZc7IizAmSHATsRsD9hmD76wnqwkVfV24J30dhYB2mQg3zyS'  # App
    access_token = '872869696990842882-dwcC4Mrkga6eH1OXPkPJgREOtn8MFg3'
    access_secret = 'DDormiUPkRQX94M8wTNQcmzTpVLDeXEfESf7GB1e6Q8Rb'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    screen_name = "Namanga39554667"
    li, lis, l = [], [], []

    for follower in api.friends(screen_name, count=100):
        li.append(follower.screen_name)
    for i in li:
        tweetcount = 0
        for j in api.user_timeline(i):
            k = str(j.created_at).split(' ')[0]
            z1 = time.mktime(datetime.datetime.strptime(
                k, "%Y-%m-%d").timetuple())
            ct = str(datetime.datetime.now()).split(' ')[0]
            z2 = time.mktime(datetime.datetime.strptime(
                ct, "%Y-%m-%d").timetuple())
            temp = (z2-z1) <= 604800.0
            if 'https' in j.text and temp:
                lis.append([i, j.text])
                tweetcount += 1
        l.append([tweetcount, i])
    info = api.me()  # Get follower and following counts
    followers_cnt = info.followers_count
    following_cnt = info.friends_count
    maxtweet = max(l)[1]
    context = {'li': li, 'lis': lis, 'followers_cnt': followers_cnt,
               'following_cnt': following_cnt,  'maxtweet': maxtweet}
    return render(request, 'index.html', context)


def au(request):
    return redirect('authorization_url')


def userlogout(request):
    logout(request)
    messages.success(request, "Logged-out Successfully ")
    return redirect('/')
