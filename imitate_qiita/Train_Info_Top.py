# -*- coding:utf-8 -*-

import json
from trainname import trainname
from CatchTrainInf import train_info
#####
# sslでエラーが出る。証明書の問題？ セキュリティー上あんま良くないと思う
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#####


def train_info_top(target):
    # 運行情報を取得
    # jsonをstrに変換して格納
    infdata = json.loads(train_info())

    for inf in infdata:

        if inf["odpt:railway"] == trainname(target):

            # 生データ（デバッグの時とかに見る）
            print(inf)

            # 情報公開日時のフォーマット処理
            date = inf["dc:date"]
            date = date.split("T")
            date[1] = date[1].split("+")
            date = date[0] + ";" + date[1][0]

            return {
                "line": trainname(inf["odpt:railway"]),
                "presentationTime": date,
                "inf": inf["odpt:trainInformationText"],
                "normal_operation": "平常" in inf["odpt:trainInformationText"]
                }


# デバッグ用
if __name__ == '__main__':

    print(train_info_top("丸ノ内線"))

