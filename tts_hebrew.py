import nexmo, os, json

application_id='41756501-ba9c-4dbe-8536-b5c29077c9df'
private_key = open('./private_key', 'r').read()

client = nexmo.Client(application_id=application_id, private_key='private_key')

response = client.create_call({
  'to': [{'type': 'phone', 'number': '447971245857'}],
  'from': {'type': 'phone', 'number': '442038929013'},
  'answer_url': ['https://olivier.nexmodemo.com/ncco/ncco_hebrew.json']
})

print(response)
