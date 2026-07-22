from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime , timedelta,time 
import jpholiday 
import pytz 
from zikokuhyou import kasugaeki, keiosinjukustation 
import pandas as pd
import urllib.request, urllib.error
from google.transit import gtfs_realtime_pb2
from geopy.distance import geodesic 
import json 
from linebot import LineBotApi
from linebot.models import TextSendMessage




import urllib.request
import json
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict


API_Endpoint = "https://api.odpt.org/api/v4/gtfs/realtime/odpt_NishiTokyoBus_NTBus_vehicle?acl:consumerKey=doebt5mdvzd7zaj9ne2u869izwnygjw6k8j7xs6m18xthqp7bo1v6k3l0nqcvpk3"
feed = gtfs_realtime_pb2.FeedMessage()

with urllib.request.urlopen(API_Endpoint) as res:
    feed.ParseFromString(res.read())

data = MessageToDict(feed)
output_path = r"C:\Users\kenji\Downloads\bus_data.json"

# JSONファイルとして保存
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"保存しました: {output_path}")