import httplib2

json_data = '{"name": "adekola", "phone": "08034294027"}'
h = httplib2.Http()

resp, content = h.request('http://ks-gapps.appspot.com/getusers', 
        'GET',
    # json_data,
        headers={'Content-Type': 'application/json'})

print content

raw_input('enter to quit')