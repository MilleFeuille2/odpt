# -*- coding:utf-8 -*-

""" 東京公共交通オープンデータを取得する """

import json
import urllib
import urllib.parse
import urllib.request
import pandas as pd
import trainname
import busname
import airplanename
#####
# sslでエラーが出る。証明書の問題？ セキュリティー上あんま良くないと思う
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#####


def search_info(rdf_type):
    """ データ検索API """
    request_url = endpoint + API_TYPE + 'odpt:' + rdf_type + '?' + 'acl:consumerKey=' + API_KEY

    response = urllib.request.urlopen(request_url)
    # text = response.read().decode()
    text = response.read().decode('utf-8')
    df = pd.DataFrame.from_records(json.loads(text))
    df.to_csv('../csv/df_{0}.csv'.format(rdf_type))

    return text


def dump_info(rdf_type):
    """ データダンプAPI """
    request_url = endpoint + API_TYPE + 'odpt:' + rdf_type + '.json?' + 'acl:consumerKey=' + API_KEY

    response = urllib.request.urlopen(request_url)
    # text = response.read().decode()
    text = response.read()
    df = pd.DataFrame.from_records(json.loads(text))
    df.to_csv('../csv/df_{0}.csv'.format(rdf_type))

    return text


def get_info(rdf_type):
    """ データ取得API """
    urn = ''
    request_url = endpoint + API_TYPE + 'datapoints/' + urn + '?' + 'acl:consumerKey=' + API_KEY

    response = urllib.request.urlopen(request_url)
    # text = response.read().decode()
    text = response.read()
    df = pd.DataFrame.from_records(json.loads(text))
    df.to_csv('../csv/df_{0}.csv'.format(rdf_type))

    return text


def search_loc(rdf_type):
    """ 地物情報検索API """
    lon = '139.766926'  # 取得範囲の中心緯度
    lat = '35.681265'  # 取得範囲の中心軽度
    radius = '1000'  # 取得範囲の半径（m）0〜4000
    request_url = endpoint + API_TYPE + 'places/odpt:' + rdf_type +\
                  "?lon=" + lon + "&lat=" + lat + "&radius=" + radius + "&acl:consumerKey=" + API_KEY

    response = urllib.request.urlopen(request_url)
    # text = response.read().decode()
    text = response.read()
    df = pd.DataFrame.from_records(json.loads(text))
    df.to_csv('../csv/df_{0}.csv'.format(rdf_type))

    return text


def train_info_top(target=None):
    # 運行情報を取得
    # jsonをstrに変換して格納
    infdata = json.loads(search_info('Train'))
    # infdata = json.loads(dump_info('Train'))

    result = []

    for inf in infdata:

        # if inf["odpt:railway"] == trainname.train_name(target):

        # 生データ（デバッグの時とかに見る）
        # print(inf)

        # 情報公開日時のフォーマット処理
        date = inf["dc:date"]
        date = date.split("T")
        date[1] = date[1].split("+")
        date = date[0] + ";" + date[1][0]

        result.append({
            "line": trainname.train_name(inf["odpt:railway"], True),
            "presentationTime": date,
            "destination": inf["odpt:destinationStation"][0],
            "from": inf["odpt:fromStation"]
            })

    return result


def bus_info_top(target=None):
    # 運行情報を取得
    # jsonをstrに変換して格納
    infdata = json.loads(search_info('Bus'))

    result = []

    for inf in infdata:

        # 生データ（デバッグの時とかに見る）
        # print(inf)

        # 情報公開日時のフォーマット処理
        date = inf["dc:date"]
        date = date.split("T")
        date[1] = date[1].split("+")
        date = date[0] + ";" + date[1][0]

        result.append({
            "busroute": inf["odpt:busroute"],
            "presentationTime": date
            })

    return result


def airplane_info_top(target=None):
    # 運行情報を取得
    # jsonをstrに変換して格納
    infdata = json.loads(search_info('FlightInformationArrival'))

    result = []

    for inf in infdata:

        # 生データ（デバッグの時とかに見る）
        # print(inf)

        # 情報公開日時のフォーマット処理
        date = inf["dc:date"]
        date = date.split("T")
        date[1] = date[1].split("+")
        date = date[0] + ";" + date[1][0]

        result.append({
            "presentationTime": date,
            "airline": inf['odpt:airline'],
            "flightNumber": inf['odpt:flightNumber'],
            "estimatedTime": inf['odpt:estimatedTime'],
            "scheduledTime": inf['odpt:scheduledTime'],
            "departureAirport": inf['odpt:departureAirport'],
            "destinationAirport": inf['odpt:destinationAirport']
            })

    return result


if __name__ == '__main__':

    endpoint = 'https://api-tokyochallenge.odpt.org'
    API_TYPE = '/api/v4/'
    API_KEY = 'a6809267eb0804fe8d296583e0a21ea969045a1b70f673c1f311dbcb893d43db'

    # print(train_info_top("常磐線"))
    result = train_info_top()
    # result = bus_info_top()

    # result = airplane_info_top()
    # result = search_loc('Station')
    
    for i in range(len(result)):
        print(result[i])


