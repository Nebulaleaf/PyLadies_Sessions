import json

json_string = """
    {
      "name": "Anna",
      "city": "Brno",
      "languages": ["Czech", "English", "Python"],
      "age": 26
    }
"""

data = json.loads(json_string)
print(data)
print(data['city'])

print(json.dumps(data, ensure_ascii = False, indent = 2))
{
  "name": "Anna",
  "city": "Brno",
  "languages": [
    "Czech",
    "English",
    "Python"
  ],
  "age": 26
}

import json

sampleJson = """{
  "company":{
    "employees":[
      {
        "name":"emma",
        "payable":{
          "salary":7000,
          "bonus":800
        }
      },
      {
        "name":"anna",
        "payable":{
          "salary":5500,
          "bonus":1000
        }
      }
    ]
  }
}"""
content = json.loads(sampleJson)
employees = content.get("company", {}).get("employees", [])
for employee in employees:
    name = employee.get('name')
    if name == "emma":
      payable = employee.get("payable", {})
      total = payable.get("salary", 0) + payable.get("bonus", 0)
      print(f"{name} has a total salary with bonus: {total}")


poem_file = open('session12_poem.txt', encoding='utf-8')
content = poem_file.read()
print(content)
poem_file.close()

print('I heard this poem:')
print()
poem_file = open('session12_poem.txt', encoding='utf-8')
for line in poem_file:
    print('    ' + line)
poem_file.close()
print()
print('How do you like it?')

with open('session12_second-poem.txt', mode='w', encoding='utf-8') as poem_file:
    poem_file.write('Our old chiming clock\n')
    poem_file.write("Is beating four o'clock\n")

with open('second-poem.txt', mode='w', encoding='utf-8') as poem_file:
    print('Our old chiming clock', file=poem_file)
    print('Is beating', 2+2, "o'clock", file=poem_file)