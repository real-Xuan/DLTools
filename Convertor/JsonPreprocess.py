import json

# Normalize the json from "serializers.serialize("json", data.objects.all())"
def djangoSerializersJsonNormalize(data):  
    serialize_data_arrays = json.loads(data)
    getdata = []
    for serialize_data_arrays_getserialize in serialize_data_arrays:
        getdata.append(serialize_data_arrays_getserialize['fields'])
    return getdata