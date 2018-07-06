import requests
import json
# req = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=1259229&cnt=40&appid=6d4c202370ae8d7c76ee8edefc512a4f')
# print(req)

app_id= '6d4c202370ae8d7c76ee8edefc512a4f'


def get_weather_data(city_id=1259229):
    weather_api_url = 'http://api.openweathermap.org/data/2.5/forecast?id=' + str(city_id) + '&cnt=40&appid=' + str(app_id)
    req = requests.get(weather_api_url)
    city_json_response = req.json()
    # print(city_json_response['cod'])
    return city_json_response


def load_city(jsonfile='TestIndiaCities.json'):
    with open(jsonfile) as json_file:
        city_list = json.load(json_file)
        city_id_list = set([city['id'] for city in city_list])
        # print(city_id_list)
        # return
        for city_id in city_id_list:
            # print(city_id)
            weather_data = get_weather_data(city_id)
            process_weather_data(weather_data)


def process_weather_data(weather_data):
    if weather_data['cod'] != '200':
        print("Not Able to process data for city_id {} and city_name {}".format(weather_data['city']['id'],
                                                                                weather_data['city']['name']))
        return

    weather_data_list = weather_data['list']
    temp_dict = {}
    for each in weather_data_list:
        # print(each)
        # print(each['dt_txt'])
        date = each['dt_txt'].split()[0]
        temp_dict[date] = temp_dict.get(date, []).append("ada")

    print(temp_dict)


load_city()
