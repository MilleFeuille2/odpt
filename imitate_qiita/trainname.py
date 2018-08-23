# -*- coding:utf-8 -*-


def trainname(s):

    namelist = {
        "odpt.Railway:TokyoMetro.Fukutoshin": "副都心線",
        "odpt.Railway: TokyoMetro.Marunouchi": "丸ノ内線",
        "odpt.Railway: TokyoMetro.Hibiya": "日比谷線",
        "odpt.Railway: TokyoMetro.Chiyoda": "千代田線",
        "odpt.Railway: TokyoMetro.Ginza": "銀座線",
        "odpt.Railway: TokyoMetro.Hanzomon": "半蔵門線",
        "odpt.Railway: TokyoMetro.Namboku": "南北線",
        "odpt.Railway: TokyoMetro.Yurakucho": "有楽町線",
        "odpt.Railway: TokyoMetro.Tozai": "東西線",
        "副都心線": "odpt.Railway: TokyoMetro.Fukutoshin",
        "丸ノ内線": "odpt.Railway: TokyoMetro.Marunouchi",
        "日比谷線": "odpt.Railway: TokyoMetro.Hibiya",
        "千代田線": "odpt.Railway: TokyoMetro.Chiyoda",
        "銀座線": "odpt.Railway: TokyoMetro.Ginza",
        "半蔵門線": "odpt.Railway: TokyoMetro.Hanzomon",
        "南北線": "odpt.Railway: TokyoMetro.Namboku",
        "有楽町線": "odpt.Railway: TokyoMetro.Yurakucho",
        "東西線": "odpt.Railway: TokyoMetro.Tozai"
    }
    return namelist[s]
