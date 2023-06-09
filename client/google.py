import random
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBF3gIABF9jg6CPKqgpVgNrVR08w9mbLq0')

def getGoogleapi(address):
# 座標を取得したい住所
    address = address
# Geocoding APIを使って住所から座標を取得
    geocode_result = gmaps.geocode(address)

# 結果を表示
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        print(f"緯度: {location['lat']}, 経度: {location['lng']}")
        return location
    else:
        print("結果が見つかりませんでした。")
