import requests
from datetime import datetime
import json

class PipedriveLocal:
  api_token = None
  add_person_url = "https://api.pipedrive.com/v1/persons"
  add_org_url = "https://api.pipedrive.com/v1/organizations"
  headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
  }

  def __init__(self, api_token):
    self.api_token = {"api_token":api_token}

  def add_organizations(self, org_args: dict):
    name = org_args.get("name", None)
    if(name is None):
      raise ValueError("name argument is required")

    data = {}
    data["name"] = name

    visible_to = org_args.get("visible_to", None)
    if(visible_to):
      data["visible_to"] = visible_to
    
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "POST", 
      self.add_org_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      return "Organization Created: "+str(result.status_code)
    else:
      raise ValueError(result.content)

  def add_persons(self, person_args: dict):
    name = person_args.get("name", None)
    if(name is None):
      raise ValueError("name argument is required")

    data = {}
    data["name"] = name

    owner_id = person_args.get("owner_id", None)
    if(owner_id):
      data["owner_id"] = owner_id

    org_id = person_args.get("org_id", None)
    if(org_id):
      data["org_id"] = org_id

    email = person_args.get("email", None)
    if(email):
      data["email"] = email
 
    phone = person_args.get("phone", None)
    if(phone):
      data["phone"] = phone

    visible_to = person_args.get("visible_to", None)
    if(visible_to):
      data["visible_to"] = visible_to
    
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "POST", 
      self.add_person_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      return "Person Created: "+str(result.status_code)
    else:
      raise ValueError(result.content)

if(__name__ == "__main__"):
  #NOTE: Test implementation
  pipedrivetest = PipedriveLocal("")

  test_args = {
    "name": "PB & J Co.",
    "visible_to": "3"
  }
  print("Organization: ")
  print(test_args)
  print(pipedrivetest.add_organizations(org_args=test_args))

  # test_args = {
  #   "name": "Peanut Butter",
  #   "email": "peanute.butter.jr@pbj.co",
  #   "phone": ("+63.999.999.995"),
  #   "visible_to": "3"
  # }
  # print("Person: ")
  # print(test_args)
  # print(pipedrivetest.add_persons(person_args=test_args))


