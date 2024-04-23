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
    if employee.get("name", "") == "emma":
        break
payable = employee.get("payable", {})
total = payable.get("salary", 0) + payable.get("bonus", 0)
print(f"Emma has a total salary with bonus: {total}")

# Version 2
content = json.loads(sampleJson)
employees = content['company']['employees']

for employee in employees:
    if employee['name'] == 'emma':
      salary = employee['payable']['salary']
      print(salary + employee["payable"]["bonus"])
