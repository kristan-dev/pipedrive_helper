# Pipedrive REST API Helper

This is a helper library for Pipedrive's rest API. At the moment, the helper is capable of Add, Update, and Delete for Persons, Products, and Deals. 

## Getting Started

Install all libraries in requirements.txt

To install:
There is only one requirement for the moment, that is the `request` library.
```
pip install -r requirements.txt
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
These doc strings below can also be found by invoking `help()` function.

A class that simplifies the use of the Pipedrive REST API

```    ...
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

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Kristan Eres** - *Initial work* - [kristan-dev](https://github.com/kristan-dev/pipedrive_helper)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to Pipedrive
* Thanks to my mentor, Luke Simkins
