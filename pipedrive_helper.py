import requests
from datetime import datetime
import json
from util.config import cfg
import logging

class PipedriveHelper:
  api_token = None
  product_url = "https://api.pipedrive.com/v1/products"
  person_url = "https://api.pipedrive.com/v1/persons"
  deal_url = "https://api.pipedrive.com/v1/deals"
  add_org_url = "https://api.pipedrive.com/v1/organizations"
  person_fields_url = "https://api.pipedrive.com/v1/personFields"
  org_fields_url = "https://api.pipedrive.com/v1/organizationFields"
  product_fields_url = "https://api.pipedrive.com/v1/productFields"
  deal_fields_url = "https://api.pipedrive.com/v1/dealFields"

  headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
  }

  def __init__(self, api_token):
    self.api_token = {"api_token":api_token}
  
  # /********** START - Pipedrive Person Functions

  def add_persons(self, person_args: dict): 
    #NOTE: Adds a contact using default fields
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
      self.person_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      return "Person Created: "+str(result.status_code)
    else:
      raise ValueError(result.content)

  def update_person(self, product_args: dict, customfieldkeys, person_id):
    update_url = self.person_url+r"/"+person_id

    data = {}

    for field in customfieldkeys:
      name = field[0]
      key = field[1]
      if(product_args.get(name, None)):
        data[key] = product_args[name]
    
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "PUT", 
      update_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "OK"):
      return "Product Created: "+str(result.status_code)
    else:
      raise ValueError(result.content)

  def get_all_personfields(self):
    response = requests.request(
      "GET", 
      self.person_fields_url, 
      headers=self.headers, 
      params=self.api_token
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  def add_person_field(self, field_name, field_type):
    #NOTE: adds a custom field of given name/field type of contact type: person
    data = {
      "name": field_name,
      "field_type": field_type
    }

    response = requests.request(
      "POST", 
      self.person_fields_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]

  def add_person_custom(self, person_args: dict, customfieldkeys):
    data = {}

    for field in customfieldkeys:
      name = field[0]
      key = field[1]
      if(person_args.get(name, None)):
        data[key] = person_args[name]
    
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "POST", 
      self.person_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      logging.debug("Person Created: "+str(result.status_code))
      rest_result = {}
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      rest_result["data"] = json.loads(result.text)["data"]
      return rest_result
    else:
      raise ValueError(result.content)

  def get_all_persons(self):
    #NOTE: Gets all persons
    response = requests.request(
      "GET", 
      self.person_url, 
      headers=self.headers, 
      params=self.api_token
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  def find_person_by_name(self, keyword: str):
    find_url = self.person_url+r"/"+"find"

    params = {
      "api_token": self.api_token,
      "term": keyword,
      "start": 0
    }

    response = requests.request(
      "GET", 
      find_url, 
      headers=self.headers, 
      params=params
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  def delete_person(self, person_id:str):
    #NOTE: Given a person_id delete a contact from pipedrive with the matching person_id
    delete_url = self.person_url+r"/"+person_id
    response = requests.request(
      "DELETE", 
      delete_url, 
      headers=self.headers, 
      params=self.api_token
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  def delete_person_bulk(self, person_ids):
    #NOTE: Given a person_ids delete all contacts from pipedrive with matching person_ids
    params = {
      "api_token": self.api_token,
      "ids": person_ids
    }
    response = requests.request(
      "DELETE", 
      self.person_url, 
      headers=self.headers, 
      params=params
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  def delete_personfield(self, personfield_id):
    delete_url = self.person_fields_url+r"/"+personfield_id
    response = requests.request(
      "DELETE", 
      delete_url, 
      headers=self.headers, 
      params=self.api_token
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]

  def delete_personfield_bulk(self, personfield_ids):
    params = {
      "api_token": self.api_token,
      "ids": personfield_ids
    }
    response = requests.request(
      "DELETE", 
      self.person_fields_url, 
      headers=self.headers, 
      params=params
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]

  # END PERSON FUNCTIONS ******************/
  
  # /************ START - PRODUCT FUNCTIONS
  
  def find_product_by_name(self, keyword: str):
    find_url = self.product_url+r"/"+"find"

    params = {
      "api_token": self.api_token,
      "term": keyword,
      "start": 0
    }

    response = requests.request(
      "GET", 
      find_url, 
      headers=self.headers, 
      params=params
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]

  def get_all_productfields(self):
    response = requests.request(
      "GET", 
      self.product_fields_url, 
      headers=self.headers, 
      params=self.api_token
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  def add_product_field(self, field_name, field_type):
    #NOTE: adds a custom field of given name/field type of Products
    data = {
      "name": field_name,
      "field_type": field_type
    }

    response = requests.request(
      "POST", 
      self.product_fields_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  def add_product_custom(self, product_args: dict, customfieldkeys):
    data = {}

    for field in customfieldkeys:
      name = field[0]
      key = field[1]
      if(product_args.get(name, None)):
        data[key] = product_args[name]
    
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "POST", 
      self.product_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      logging.debug("Product Created: "+str(result.status_code))
      rest_result = {}
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      rest_result["data"] = json.loads(result.text)["data"]
      return rest_result
    else:
      raise ValueError(result.content)
  
  def update_product(self, product_args: dict, customfieldkeys, product_id):
    update_url = self.product_url+r"/"+product_id

    data = {}

    for field in customfieldkeys:
      name = field[0]
      key = field[1]
      if(product_args.get(name, None)):
        data[key] = product_args[name]
    
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "PUT", 
      update_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "OK"):
      return "Product Updated: "+str(result.status_code)
    else:
      raise ValueError(result.content)

  def delete_product(self, product_id):
    delete_url = self.product_url+r"/"+product_id
    response = requests.request(
      "DELETE", 
      delete_url, 
      headers=self.headers, 
      params=self.api_token
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  def delete_products_bulk(self, product_ids):
    for product_id in product_ids:

      delete_url = self.product_url+r"/"+str(product_id)
      response = requests.request(
        "DELETE", 
        delete_url, 
        headers=self.headers, 
        params=self.api_token
      )

      result = bytes(response.content).decode("utf-8")
      result = json.loads(result)
      result = json.dumps(result["data"])
      logging.debug(result)
  
  def delete_productfield(self, productfield_id):
    delete_url = self.product_fields_url+r"/"+productfield_id
    response = requests.request(
      "DELETE", 
      delete_url, 
      headers=self.headers, 
      params=self.api_token
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  def delete_productfield_bulk(self, productfield_ids):
    params = {
      "api_token": self.api_token,
      "ids": productfield_ids
    }
    response = requests.request(
      "DELETE", 
      self.product_fields_url, 
      headers=self.headers, 
      params=params
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  # END PRODUCT FUNCTIONS ******************/

  # /************ START, ORGANIZATION FUNCTIONS
  
  def get_all_orgfields(self):
    response = requests.request(
      "GET", 
      self.org_fields_url, 
      headers=self.headers, 
      params=self.api_token
    )
    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  def add_org_field(self, field_name, field_type):
    #NOTE: adds a custom field of given name/field of contact type: organization
    data = {
      "name": field_name,
      "field_type": field_type
    }

    response = requests.request(
      "POST", 
      self.org_fields_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]

  def add_organizations(self, org_args: dict):
    #NOTE: Adds a contact using default fields
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
  
  # END, ORGANIZATION FUNCTIONS ******************/

  # /************ START, DEAL FUNCTIONS
  
  def get_all_dealfields(self):
    response = requests.request(
      "GET", 
      self.deal_fields_url, 
      headers=self.headers, 
      params=self.api_token
    )

    result = bytes(response.content).decode("utf-8")
    result = json.loads(result)
    return result["data"]
  
  def add_deal_custom(self, person_args: dict, customfieldkeys):
    data = {}

    for field in customfieldkeys:
      name = field[0]
      key = field[1]
      if(person_args.get(name, None)):
        data[key] = person_args[name]
    
    result = requests.request(
      "POST", 
      self.deal_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      logging.debug("Deal Created: "+str(result.status_code))
      rest_result = {}
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      rest_result["data"] = json.loads(result.text)["data"]
      return rest_result
    else:
      raise ValueError(result.content)

  def add_deal(self, title, person_id):
    if(title is None):
      raise ValueError("title arg t is required")

    if(person_id is None):
      raise ValueError("person id arg is required")

    data = {
      "title": title,
      "person_id": person_id
    }

    result = requests.request(
      "POST", 
      self.deal_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      logging.debug("Deal Created: "+str(result.status_code))
      rest_result = {}
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      rest_result["data"] = json.loads(result.text)["data"]
      return rest_result
    else:
      raise ValueError(result.content)
  
  def attach_product_to_deal(self, deal_id, product_id):
    if(deal_id is None):
      raise ValueError("deal id is required")

    if(product_id is None):
      raise ValueError("product_id is required")

    api_url = f"{self.deal_url}/{deal_id}/products"

    data = {
      "item_price": "0",
      "quantity": "1",
      "product_id": product_id
    }

    result = requests.request(
      "POST", 
      api_url,
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      logging.debug("Product attached to Deal: "+str(result.status_code))
      rest_result = {}
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      rest_result["data"] = json.loads(result.text)["data"]
      return rest_result
    else:
      raise ValueError(result.content)
  
  # END, DEAL FUNCTIONS ******************/


if(__name__ == "__main__"):
  #NOTE: Test implementation
  # pipedrivetest = PipedriveHelper(cfg["pipedrive"]["api_key"]["prod"])
  # response = pipedrivetest.add_product_to_deal(18, 542)
  
  # product_ids = (41, 42, 43, 44, 45, 46, 47, 48, 49, 50)
  # pipedrivetest.delete_products_bulk(product_ids)

  # person_fields = json.dumps(pipedrivetest.get_all_personfields())

  # test_args = {
  #   "name": "PB & J Co.",
  #   "visible_to": "3"
  # }
  # print("Organization: ")
  # print(test_args)
  # print(pipedrivetest.add_organizations(org_args=test_args))

  # test_args = {
  #   "name": "Peanut Butter",
  #   "simple_name": "PeanutButter&JellyCo",
  #   "email": "peanut.butterj@pbj.co",
  #   "phone": ("+63.999.999.995"),
  #   "visible_to": "3"
  # }
  # print("Person: ")
  # print(test_args)
  # print(pipedrivetest.add_persons(person_args=test_args))

  # test_args = {
  #   "name": "Peanut Butter"
  # }

  # pipedrivetest.update_person(test_args, ({"Name":"name"}), "22")

  pass


