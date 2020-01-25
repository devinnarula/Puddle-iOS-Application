rawcode = {'meta': {'code': 200, 'hasMore': False}, 'geofences': [{'_id': '5e2cb76b8be83700b72f0ebd', 'geometryCenter': {'coordinates': [34.67918715194163, -82.83663725176865], 'type': 'Point'}, 'live': False, 'enabled': True, 'description': 'Test', 'type': 'polygon', 'createdAt': '2020-01-25T21:47:23.651Z', 'geometry': {'type': 'Polygon', 'coordinates': [[[34.68216965456513, -82.84807573583319], [34.68140454618486, -82.8367726354168], [34.67935767062538, -82.83029241843673], [34.67381673639116, -82.83140821738792], [34.68216965456513, -82.84807573583319]]]}, 'geometryRadius': 774, 'tag': 'ICE', 'externalId': '164724', 'updatedAt': '2020-01-25T21:47:23.652Z'}, {'_id': '5e2cb4564ad6ac0076232873', 'geometryCenter': {'coordinates': [34.67918715194163, -82.83663725176865], 'type': 'Point'}, 'live': False, 'enabled': True, 'description': 'Test', 'type': 'polygon', 'createdAt': '2020-01-25T21:34:14.850Z', 'geometry': {'type': 'Polygon', 'coordinates': [[[34.68216965456513, -82.84807573583319], [34.68140454618486, -82.8367726354168], [34.67935767062538, -82.83029241843673], [34.67381673639116, -82.83140821738792], [34.68216965456513, -82.84807573583319]]]}, 'geometryRadius': 774, 'tag': 'ICE', 'externalId': '163416', 'updatedAt': '2020-01-25T21:34:14.851Z'}, {'_id': '5e2c9db2f4226c012eead8f1', 'geometryCenter': {'coordinates': [-82.8384410237492, 34.678585998401964], 'type': 'Point'}, 'live': False, 'enabled': True, 'description': 'Clemson Campus', 'type': 'polygon', 'createdAt': '2020-01-25T19:57:38.594Z', 'geometry': {'type': 'Polygon', 'coordinates': [[[-82.84807573583119, 34.68216965456513], [-82.8367726354168, 34.68140454618486], [-82.83029241843683, 34.67935767062518], [-82.83140821738702, 34.67381673639106], [-82.84565611167413, 34.6761813842436], [-82.84807573583119, 34.68216965456513]]]}, 'geometryRadius': 763, 'tag': 'ice', 'externalId': '145739', 'updatedAt': '2020-01-25T19:57:38.595Z'}]}
def clean_geo(rawcode):
    coordinates = []
    tag = []
    externalId = []
    description = []
    for i in range(0,len(rawcode['geofences'])):
        coordinates = coordinates + rawcode['geofences'][i]['geometry']['coordinates'][0]
        tag = tag + rawcode['geofences'][i]['tag']
        externalId = externalId + rawcode['geofences'][i]['externalId']
        description = description + rawcode['geofences'][i]['description']
    data = {'coordinates' : coordinates, 'tag' : tag, 'externalId' : externalId, 'description' : description}
    return data
print(clean_geo(rawcode))