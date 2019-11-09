import json
payload = '{"locale":"ru","point_a_name":"Source","point_b_name":"Target","points":[{"type":"pedo","x":37.610316,"y":55.747845,"object_id":"4504235282781932"},{"type":"pedo","x":37.62576,"y":55.7458,"object_id":"4504235282711290"}],"purpose":"autoSearch","type":"online5","viewport":{"topLeft":{"x":37.55929100875705,"y":55.7524829685509},"bottomRight":{"x":37.675847289048086,"y":55.73825901569989},"zoom":13.05606595365341}}'
payload_dict = json.loads(payload)
print(type(payload_dict))
print(payload_dict)

print(payload_dict)
new_payload = json.dumps(payload_dict)
print(new_payload)
