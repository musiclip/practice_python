#json 파일 읽어보기

import json
import folium

def get_data(file_names):
    with open(file_names, encoding = 'utf-8') as f:
        datas = json.load(f)
    return datas

data = get_data('food_hot_place.json')

def map_add(maps, data):
    for item in data:
        name = item['RESTRT_NM']
        if item['REFINE_WGS84_LAT']:
            latitude = float(item['REFINE_WGS84_LAT'])
            longtitude = float(item['REFINE_WGS84_LOGT'])
            folium.CircleMarker([latitude, longtitude], radius = 4, popup = name, color = 'red', fill_color = 'red').add_to(maps)            
    return maps

def FoliumMap(data, save_file = 'result.html'):
    maps = folium.Map(location = [37.5602,126.982], zoom_start = 7)
    map_add(maps,data)
    maps.save(save_file)

FoliumMap(data)
         


#Class의 이해

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self): 
        return self.first / self.second
    
class SafeFourCal(FourCal):
    def div(self):
        if self.first == 0 or self.second == 0:
            return 0
        return self.first / self.second
    
fc = FourCal(1,2)
print(fc.add())
print(fc.mul())
print(fc.sub())
print(fc.div())
fc.setdata(10,2)
print(fc.add())
print(fc.mul())
print(fc.sub())
print(fc.div())

sfc = SafeFourCal(10, 0)
print(sfc.div())
sfc.setdata(0, 7)
print(sfc.div())