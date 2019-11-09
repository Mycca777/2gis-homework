import json
payload = '{"locale":"ru","point_a_name":"Source","point_b_name":"Target","points":[{"type":"pedo","x":37.610316,"y":55.747845,"object_id":"4504235282781932"},{"type":"pedo","x":37.62576,"y":55.7458,"object_id":"4504235282711290"}],"purpose":"autoSearch","type":"online5","viewport":{"topLeft":{"x":37.55929100875705,"y":55.7524829685509},"bottomRight":{"x":37.675847289048086,"y":55.73825901569989},"zoom":13.05606595365341}}'
payload_dict = json.loads(payload)
print(type(payload_dict))
print(payload_dict)
#==============================================================================================
print(payload_dict)
new_payload = json.dumps(payload_dict)
print(new_payload)
#==============================================================================================
import requests

request_url = 'https://catalog.api.2gis.ru/ctx/2.0/moscow?key=rurbbn3446'
payload_ctx = '{"locale":"ru","enable_schedule":false,"source":{"point":{"lon":37.610316,"lat":55.747845},"object_id":"4504235282781932","name":"Source"},"target":{"point":{"lon":37.62576,"lat":55.7458},"object_id":"4504235282711290","name":"Target"},"transport":["bus","trolleybus","tram","shuttle_bus","metro","suburban_train","funicular_railway","monorail","river_transport","cable_car","light_rail","premetro","light_metro","aeroexpress","pedestrian"],"purpose":"routeSearch","viewport":{"topLeft":{"x":37.61024342190405,"y":55.7514265905093},"bottomRight":{"x":37.62544511062968,"y":55.74120700809857},"zoom":15.809352289673843}}'
#request_url = 'https://catalog.api.2gis.ru/ctx/2.0/moscow?key=rurbbn3446'
#payload_ped = '{"locale":"ru","point_a_name":"Source","point_b_name":"Target","points":[{"type":"pedo","x":37.610316,"y":55.747845},{"type":"pedo","x":37.62576,"y":55.7458}],"type":"pedestrian","purpose":"autoSearch","viewport":{"topLeft":{"x":37.607544074845514,"y":55.75009527409279},"bottomRight":{"x":37.62543257248807,"y":55.73806861272502},"zoom":15.574551660132045}}'
data = requests.post(url=request_url, data=payload_ctx)

print(data)
print(response)
#=====================================================================================================
print(data)
print(data.text)
response = json.loads(data.text)
ku = json.dumps(response, indent=4, ensure_ascii=False)
print(ku)
#========================================================================================================
def replace_points_ctx(lat1: float, lon1: float, lat2: float, lon2: float):
    payload_ct = json.loads(payload_ctx)
    payload_ct["source"]["point"]["lat"] = lat1
    payload_ct["source"]["point"]["lon"] = lon1
    payload_ct["target"]["point"]["lat"] = lat2
    payload_ct["target"]["point"]["lon"] = lon2
print(replace_points_ped(55.747902, 67.567812, 55.745712, 37.625692))  #37.610569
#-----------------------------------------------------------------------------------------
def get_transport_duration_by_2_points(lat1: float, lon1: float, lat2: float, lon2: float):
    request_url = 'https://catalog.api.2gis.ru/ctx/2.0/moscow?key=rurbbn3446'
    payload_ctx = '{"locale":"ru","enable_schedule":false,"source":{"point":{"lon":37.610316,"lat":55.747845},"object_id":"4504235282781932","name":"Source"},"target":{"point":{"lon":37.62576,"lat":55.7458},"object_id":"4504235282711290","name":"Target"},"transport":["bus","trolleybus","tram","shuttle_bus","metro","suburban_train","funicular_railway","monorail","river_transport","cable_car","light_rail","premetro","light_metro","aeroexpress","pedestrian"],"purpose":"routeSearch","viewport":{"topLeft":{"x":37.61024342190405,"y":55.7514265905093},"bottomRight":{"x":37.62544511062968,"y":55.74120700809857},"zoom":15.809352289673843}}'
    replace_points_ctx(lat1, lon1, lat2, lon2)
    data = requests.post(url=request_url, data=payload_ctx)
    response_ctx = json.loads(data.text)
    return json.dumps(response[0]['total_duration'], ensure_ascii=False) + "сек"
print(get_transport_duration_by_2_points(55.747902, 37.610569, 55.745712, 37.625692))
#-------------------------------------------------------------------------------------

def get_pedestrian_duration_by_2_points(lat1: float, lon1: float, lat2: float, lon2: float):
    request_url = 'https://catalog.api.2gis.ru/pedestrian/4.0.0/moscow?key=rurbbn3446'
    payload_ped = '{"locale":"ru","point_a_name":"Source","point_b_name":"Target","points":[{"type":"pedo","x":37.651858,"y":55.742204,"object_id":"4504385606391048"},{"type":"pedo","x":37.679359,"y":55.735633,"object_id":"4504235282822322"}],"type":"pedestrian","purpose":"autoSearch","viewport":{"topLeft":{"x":37.64908169633543,"y":55.75849801823626},"bottomRight":{"x":37.681454303664566,"y":55.71566976315851},"zoom":13.52839812792528}}'
    payload = json.loads(payload_ped)
    payload["points"][0]["x"] = lon1
    payload["points"][0]["y"] = lat1
    payload["points"][1]["x"] = lon2
    payload["points"][1]["y"] = lat2
    payload_ped = json.dumps(payload)
    data = requests.post(url=request_url, data=payload_ped)
    print(data)
    response_ped = json.loads(data.text)
    return json.dumps(response_ped["result"][0]["total_duration"], ensure_ascii = False) + "сек"
print(get_pedestrian_duration_by_2_points(55.747902, 37.610569, 55.745712, 37.625692))
#--------------------------------------------------------------------------------------

def get_pedestrian_length_by_2_points(lat1: float, lon1: float, lat2: float, lon2: float):   
    request_url = 'https://catalog.api.2gis.ru/pedestrian/4.0.0/moscow?key=rurbbn3446'
    payload_ped = '{"locale":"ru","point_a_name":"Source","point_b_name":"Target","points":[{"type":"pedo","x":37.651858,"y":55.742204,"object_id":"4504385606391048"},{"type":"pedo","x":37.679359,"y":55.735633,"object_id":"4504235282822322"}],"type":"pedestrian","purpose":"autoSearch","viewport":{"topLeft":{"x":37.64908169633543,"y":55.75849801823626},"bottomRight":{"x":37.681454303664566,"y":55.71566976315851},"zoom":13.52839812792528}}'
    payload = json.loads(payload_ped)
    payload["points"][0]["x"] = lon1
    payload["points"][0]["y"] = lat1
    payload["points"][1]["x"] = lon2
    payload["points"][1]["y"] = lat2
    payload_ped = json.dumps(payload)
    data = requests.post(url=request_url, data=payload_ped)
    replace_points_ped(lon1, lat1, lon2, lat2)
    print(data)
    response_ped = json.loads(data.text)
    return json.dumps(response_ped["result"][0]["total_distance"], ensure_ascii = False ) + "м"
print(get_pedestrian_length_by_2_points(55.747902, 37.610569, 55.745712, 37.625692))
#--------------------------------------------------------------------------------------
x1, y1 = 55.723158, 37.564597 
x2, y2 = 55.788798, 37.680701
print(get_transport_duration_by_2_points(x1,y1,x2,y2))
print(get_pedestrian_length_by_2_points(x1,y1,x2,y2))
print(get_pedestrian_duration_by_2_points(x1,y1,x2,y2))
