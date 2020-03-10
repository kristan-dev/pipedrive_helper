import requests
from datetime import datetime
import json
from util.config import cfg
import logging

class PipedriveHelper:
  """
  Class for Pipedrive Helper Module.

  Usage:
  When initializing the class, provide the Pipedrive API token
  pipedrive_test_object = PipedriveHelper(111aaaa2222bbbb333444cccc)

  """
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

  # /********** PERSON FUNCTIONS - START **********/
  def add_person(self, field_args: dict, field_keys: list) -> dict:
    """
    Adds a single person to the contacts section of your Pipedrive account.

    Usage:
    Default Field Keys are usually the lower case equivalent of the field's name.
    Custom Field Keys are alphanumeric and can be found in your pipedrive account's settings.

    dict structure
    <dict name> = {
      <field name>: <field key >
    }

    ex.
    fieldkeys_default = {
      "Name": "name",
      "Title": "title",
      "Organization": "org_id" 
    }
    """
    data = {}
    for field in field_keys:
      name = field[0]
      key = field[1]
      if(field_args.get(name, None)):
        data[key] = field_args[name]
    
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

  # /********** PERSON FUNCTIONS - END **********/

  # /********** PERSON FUNCTIONS - START **********/
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
  # /********** PERSON FUNCTIONS - END **********/

def test_ast(a, *, b = None):
  print("Hello")
  pass



if(__name__ == "__main__"):
  pipedrivehelper = PipedriveHelper(api_token='745fec504c69138bfbc4456716ca668dabf4f2da')
  pass
