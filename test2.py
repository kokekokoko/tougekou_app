from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime , timedelta,time 
import jpholiday 
import pytz 
from zikokuhyou import kasugaeki, keiosinjukustation 
import requests
import pandas as pd
import urllib.request, urllib.error
from google.transit import gtfs_realtime_pb2
import datetime

feed = gtfs_realtime_pb2.FeedMessage()
API_Endpoint = 'https://api.odpt.org/api/v4/gtfs/realtime/odpt_NishiTokyoBus_NTBus_vehicle?acl:consumerKey=doebt5mdvzd7zaj9ne2u869izwnygjw6k8j7xs6m18xthqp7bo1v6k3l0nqcvpk3'
print(API_Endpoint)
# print(res.status_code)
# print(res.content)
# res = urllib.request.urlopen(API_Endpoint)
# feed.ParseFromString(res.read())
# for i in range(len(feed.entity)):
    
#     print(feed.entity[i].id)
# res_json = res.json()
# results = res_json[0]['dc:title']
# print(results)