import requests
from datetime import datetime
import json
import logging

class PipedriveHelper:
  """
  A class that simplifies the use of the Pipedrive REST API

    ...
    Constructors
    ----------
    api_token : str
        your pipedrive api token.

    Attributes
    ----------
    product_url : str
        api url for all product methods
    person_url : str
        api url for all product methods
    deal_url : str
        api url for all deal methods
    org_url : str
        api url for all org methods
    person_fields_url : str
        api url for all personfield methods
    product_fields_url : str
        api url for all productfield methods
    deal_fields_url : str
        api url for all dealfield methods
    org_fields_url : str
        api url for all orgfield methods

    Methods
    -------
    add_person(self, person_args: dict) returns dict
        Add a single person to contacts in Piprdrive
    add_product(self, product_args: dict) returns dict
        Add a single person to products in Piprdrive
    update_product(self, product_args: dict, product_id: str) returns dict
        Updates an existing product in Pipedrive.
    delete_product(self, product_id: str) returns dict
        Deletes an existing product in Pipedrive.
  """
  api_token = None
  product_url = "https://api.pipedrive.com/v1/products"
  person_url = "https://api.pipedrive.com/v1/persons"
  deal_url = "https://api.pipedrive.com/v1/deals"
  org_url = "https://api.pipedrive.com/v1/organizations"
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

  # /********** START - PERSON FUNCTIONS **********/
  def add_person(self, person_args: dict) -> dict:
    """
    Parameters
        ----------
        person_args : dict
            Values for each column for a single contact. Accepts default fields and custom fields.
            
        Usage
        ----------
            data = {
              "name": Luke, # where "name" is a sample of a default field
              "74f20ffc505c9708d4f0958333b0cc1df74a2ee9": 92, # where "74f20ffc505c970..." is a sample of custom field
            }
    """

    data = person_args
    add_time = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
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

      logging.debug(rest_result["data"])
      
      return rest_result
    else:
      raise ValueError(result.content)
  
  def update_person(self, person_args: dict, person_id: str) -> dict:
    """Updates an existing contact in Pipedrive. Returns REST result status and API rate limit info.

    Parameters
        ----------
        person_args : dict
            Values for each column for a single contact. Accepts default fields and custom fields.
        product_id : str
            Pipedrive product id
            
        Usage
        ----------
            Only add the fields/customfields you want to update.

              data = {
                "name": John, # where "name" is a sample of a default field
                "74f20ffc505c9708d4f0958333b0cc1df74a2ee9": 92, # where "74f20ffc505c970..." is a sample of a custom field
                }
              update_product(data, "1")
    """
    update_url = self.person_url+r"/"+person_id
    data = person_args
    add_time = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "PUT", 
      update_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "OK"):
      # logging.debug("Person Updated: "+str(result.status_code))

      rest_result = {}
      rest_result["status"] = "Product Updated: "+str(result.status_code)
      rest_result["data"] = None
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      return rest_result
    else:
      raise ValueError(result.content)

  def delete_person(self, person_id: str) -> dict:
    """Deletes an existing contact in Pipedrive. Returns REST result status and API rate limit info.

    Parameters
        ----------
        person_id : str
            Pipedrive person id
            
        Usage
        ----------
            delete_person("1") # where "1" is the pipedrive person id
    """
    delete_url = self.person_url+r"/"+person_id

    result = requests.request(
      "DELETE", 
      delete_url, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "OK"):
      # logging.debug("Person Deleted: "+str(result.status_code))

      rest_result = {}
      rest_result["result"] = "Person Deleted: "+str(result.status_code)
      rest_result["data"] = None
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      return rest_result
    else:
      raise ValueError(result.content)

  # /********** END - PERSON FUNCTIONS **********/

  # /********** START - PRODUCT FUNCTIONS **********/

  def add_product(self, product_args: dict) -> dict:
    #TODO: Add proper documentation
    """Add a single row to products in Piprdrive. Returns API call status and API rate limit info.

    Parameters
        ----------
        person_args : dict
            Values for each column for a single contact. Accepts default fields and custom fields.
            
        Usage
        ----------
            data = {
              "name": "SCPH-90006", # where "name" is a sample of a default field
              "74f20ffc505c9708d4f0958333b0cc1df74a2ee9": 92, # where "74f20ffc505c970..." is a sample of custom field
              }
            add_product(data)
    """
    data = product_args
    add_time = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "POST", 
      self.product_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      # logging.debug("Product Created: "+str(result.status_code))

      rest_result = {}
      rest_result["status"] = "Product Created: "+str(result.status_code)
      rest_result["data"] = None
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      return rest_result
    else:
      raise ValueError(result.content)
  
  def update_product(self, product_args: dict, product_id: str) -> dict:
    """Updates an existing product in Pipedrive.Returns REST result status and API rate limit info.

    Parameters
        ----------
        product_args : dict
            Values for each column for a single contact. Accepts default fields and custom fields.
        product_id : str
            Pipedrive product id
            
        Usage
        ----------
            Only add the fields/customfields you want to update.

              data = {
                "name": "SCPH-90006", # where "name" is a sample of a default field
                "74f20ffc505c9708d4f0958333b0cc1df74a2ee9": 92, # where "74f20ffc505c970..." is a sample of a custom field
                }
              update_product(data, "1")
    """
    update_url = self.product_url+r"/"+product_id

    data = product_args
    add_time = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "PUT", 
      update_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "OK"):
      # logging.debug("Product Updated: "+str(result.status_code))

      rest_result = {}
      rest_result["status"] = "Product Updated: "+str(result.status_code)
      rest_result["data"] = None
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      return rest_result
    else:
      raise ValueError(result.content)
  
  def delete_product(self, product_id: str):
    """Deletes an existing product in Pipedrive. Returns REST result status and API rate limit info.

    Parameters
        ----------
        product_id : str
            Pipedrive product id
            
        Usage
        ----------
            delete_product("1") # where "1" is the pipedrive product id
    """
    delete_url = self.product_url+r"/"+product_id

    result = requests.request(
      "DELETE", 
      delete_url, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "OK"):
      # logging.debug("Product Deleted: "+str(result.status_code))

      rest_result = {}
      rest_result["result"] = "Product Deleted: "+str(result.status_code)
      rest_result["data"] = None
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      return rest_result
    else:
      raise ValueError(result.content)

  # /********** END - PRODUCT FUNCTIONS **********/

  # /********** START - DEAL FUNCTIONS **********/
  def add_deal(self, deal_args: dict) -> dict:
    """
    Parameters
        ----------
        deal_args : dict
            Values for each column for a single deal. Accepts default fields and custom fields.
            
        Usage
        ----------
            data = {
              "name": John, # where "name" is a sample of a default field
              "74f20ffc505c9708d4f0958333b0cc1df74a2ee9": 92, # where "74f20ffc505c970..." is a sample of custom field
            }
    """

    data = deal_args
    add_time = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time
    
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
  
  def update_deal(self, deal_args: dict, deal_id: str) -> dict:
    """
    Parameters
        ----------
        deal_args : dict
            Values for each column for a single deal. Accepts default fields and custom fields.
            
        Usage
        ----------
            data = {
              "name": John's Deal, # where "name" is a sample of a default field
              "74f20ffc505c9708d4f0958333b0cc1df74a2ee9": 92, # where "74f20ffc505c970..." is a sample of custom field
            }
    """
    update_url = self.deal_url+r"/"+deal_id

    data = deal_args
    add_time = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "PUT", 
      update_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "OK"):
      # logging.debug("Deal Updated: "+str(result.status_code))

      rest_result = {}
      rest_result["status"] = "Deal Updated: "+str(result.status_code)
      rest_result["data"] = None
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      return rest_result
    else:
      raise ValueError(result.content)

  def delete_deal(self, deal_id: str) -> dict:
    """Deletes an existing deal in Pipedrive. Returns REST result status and API rate limit info.

    Parameters
        ----------
        deal_id : str
            Pipedrive product id
            
        Usage
        ----------
            delete_deal("1") # where "1" is the pipedrive product id
    """

    delete_url = self.deal_url+r"/"+deal_id

    result = requests.request(
      "DELETE", 
      delete_url, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "OK"):
      # logging.debug("Product Deleted: "+str(result.status_code))

      rest_result = {}
      rest_result["result"] = "Product Deleted: "+str(result.status_code)
      rest_result["data"] = None
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      return rest_result
    else:
      raise ValueError(result.content)

  # /********** END - DEAL FUNCTIONS **********/

if(__name__ == "__main__"):
  pass