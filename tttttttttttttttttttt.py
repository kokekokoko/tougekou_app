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
def message():
    info = json.load(open("info.json","r"))
    channel_access_token = info["channel_access_token"]
    channel_ID = info["channel_ID"]
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(channel_ID, TextSendMessage(text="バスが到着しました"))
    
if __name__ == '__main__':
    message()
# info = json.load(open("info.json","r"))