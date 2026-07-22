import pandas as pd
import urllib.request, urllib.error
from google.transit import gtfs_realtime_pb2
import datetime
import os
import time 

token = "doebt5mdvzd7zaj9ne2u869izwnygjw6k8j7xs6m18xthqp7bo1v6k3l0nqcvpk3" #ユーザ登録で取得したアクセストークン
toei_bus_location_URL = "https://api.odpt.org/api/v4/gtfs/realtime/odpt_NishiTokyoBus_NTBus_vehicle?acl:consumerKey="
feed = gtfs_realtime_pb2.FeedMessage()
API_Endpoint = toei_bus_location_URL+token

column = ["id","trip_id","route_id","direction_id","lat","lon","current_stop_sequence","timestamp","stop_id"]
csv_file = "bus_data.csv"

def get_gtfs_rt():
    result = []
    now = datetime.datetime.now()
    now_str = now.strftime('%Y%m%dT%H%M%S')#現在時刻を文字型に変換

    with urllib.request.urlopen(API_Endpoint) as res:
        feed.ParseFromString(res.read())
        for entity in feed.entity:
                record = [
                entity.id,                            #車両ID
                entity.vehicle.trip.trip_id,          #一意に求まるルート番号
                entity.vehicle.trip.route_id,         #路線番号（≒系統）
                entity.vehicle.trip.direction_id,     #方向（上り下り）
                entity.vehicle.position.latitude,     #車両経度
                entity.vehicle.position.longitude,    #車両緯度
                entity.vehicle.current_stop_sequence, #直近で通過した停留所の発着順序
                entity.vehicle.timestamp,             #タイムスタンプ
                entity.vehicle.stop_id,               #直近で通過した停留所
                ]
                if entity.vehicle.trip.route_id in ["10009","10011", "10014", "10015"]:
                    result.append(record)

    new_df = pd.DataFrame(result, columns=column)
    new_df["timestamp"] = pd.to_datetime(new_df.timestamp, unit='s', utc=True).dt.tz_convert('Asia/Tokyo')  # タイムスタンプ情報をUNIX時間から日本時間に変換
    new_df["timestamp"] = new_df["timestamp"].dt.tz_localize(None)  # Timezone情報を削除
    if os.path.exists(csv_file):
        print(111111111111111111)
        old_df = pd.read_csv(csv_file)
        merged_df = pd.concat([old_df, new_df])
        print(merged_df)
        merged_df.drop_duplicates()  # 重複データを削除
        print(merged_df)
    else:
        merged_df = new_df

    # CSVファイルに保存
    merged_df.to_csv(csv_file, index=False)

    # print(merged_df)
while True:
    get_gtfs_rt()  # データ取得関数を実行
    time.sleep(20)  # 20秒間待機
