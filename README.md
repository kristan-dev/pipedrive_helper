# Pipedrive REST API Helper

This is a helper library for Pipedrive's rest API. At the moment, the helper is capable of Add, Update, and Delete for Persons, Products, and Deals. 

This library is available in pypi.org to install:

```
python -m pip install pypedrive-helper
```

## Getting Started

Install all libraries in requirements.txt

To install:
There is only one requirement for the moment, that is the `request` library.
```
pip install -r requirements.txt
```

To start using the class the after installing:
```
from pypedrivehelper.helper import PipedriveHelper
```

## Prerequisites

Your Pipedrive API Token is required to use all the methods of this helper.

Provide an API token when creating an insance of the `PipedriveHelper` class, in str format.


## Sample Usage

When creating an instance of a class, provide the API token of type str.
```
pipedrive_api = PipedriveHelper(api_key)
```

When using functions. Provide the parameters of type dict. For details of function usage refer to the docstrings.
```
data = {
    "title": "test title 2"
  }

pipedrive_api.add_deal(data)
```

## Doc Strings
The information below can also be found within the library as docstrings. Use `help()` to view them.

```
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
```

Add Person
```
Adds a single contact in Pipedrive. Returns REST result status and API rate limit info.

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
```

Update Person
```
Updates an existing contact in Pipedrive. Returns REST result status and API rate limit info.

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
```

Delete Person
```
Deletes an existing contact in Pipedrive. Returns REST result status and API rate limit info.

Parameters
        ----------
        person_id : str
            Pipedrive person id
            
        Usage
        ----------
            delete_person("1") # where "1" is the pipedrive person id
```

Add Product
```
Add a single row to products in Piprdrive. Returns API call status and API rate limit info.

Parameters
        ----------
        product_args : dict
            Values for each column for a single contact. Accepts default fields and custom fields.
            
        Usage
        ----------
            data = {
              "name": "SCPH-90006", # where "name" is a sample of a default field
              "74f20ffc505c9708d4f0958333b0cc1df74a2ee9": 92, # where "74f20ffc505c970..." is a sample of custom field
              }
            add_product(data)
```

Update Product
```
Updates an existing product in Pipedrive.Returns REST result status and API rate limit info.

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
```

Delete Product
```
Deletes an existing product in Pipedrive. Returns REST result status and API rate limit info.

Parameters
        ----------
        product_id : str
            Pipedrive product id
            
        Usage
        ----------
            delete_product("1") # where "1" is the pipedrive product id
```

Add Deal
```
Creates a single deal to Pipedrive. Returns REST result status and API rate limit info.

Parameters
        ----------
        deal_args : dict
            Values for each column for a single deal. Accepts default fields and custom fields.
            
        Usage
        ----------
            data = {
              "title": John's Deal, # where "name" is a sample of a default field
              "74f20ffc505c9708d4f0958333b0cc1df74a2ee9": 92, # where "74f20ffc505c970..." is a sample of custom field
            }
```

Update Deal
```
Updates an existing deal in Pipedrive.Returns REST result status and API rate limit info.

Parameters
        ----------
        deal_args : dict
            Values for each column for a single deal. Accepts default fields and custom fields.
            
        Usage
        ----------
            data = {
              "title": John's Deal, # where "name" is a sample of a default field
              "74f20ffc505c9708d4f0958333b0cc1df74a2ee9": 92, # where "74f20ffc505c970..." is a sample of custom field
            }
```

Delete Deal
```
Deletes an existing deal in Pipedrive. Returns REST result status and API rate limit info.

Parameters
        ----------
        deal_id : str
            Pipedrive product id
            
        Usage
        ----------
            delete_deal("1") # where "1" is the pipedrive product id
```

## Versioning
Version 1.0.2
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Kristan Eres** - [kristan-dev](https://github.com/kristan-dev/pipedrive_helper)

## License

This project is licensed under the MIT License

MIT License

Copyright (c) 2020 Kristan Sangalang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

## Acknowledgments

* To pipedrive for the opportunity to create this module
* To my mentor for inspiring me to be better
