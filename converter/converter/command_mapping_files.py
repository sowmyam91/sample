import argparse
import os
import json
from jinja2 import Template
import re

template_schema = """{
    "product": "{{ data.provider_product_id}}",
    "resource": "{{ data.resource_type }}",
    "label_field": "",
    "type": "bpprov_full",
    "provider_resource_id_field": "",
    "device_namespace_props": [],
    "commands": {
        "list": {
            "command": "list-{{ data.name }}.json"
        },
        "post": {
            "command": "create-{{ data.name }}.json"
        },
        "put": {
            "command": "update-{{ data.name }}.json",
            "returns_resource": true
        },
        "get": {
            "command": "get-{{ data.name }}.json"
        },
        "delete": {
            "command": "delete-{{ data.name }}.json"
        }
    }
}"""


def get_products_path(ra_name):
    path = "model/resources/products.json"
    return os.path.join(ra_name, path)


def get_products(path):
    with open(path, 'r') as product_f:
        str_products = product_f.read()
        products = json.loads(str_products)
    return products


def create_file(path, data):
    with open(path, 'w') as fd:
        json.dump(data, fd, indent=4,
                  ensure_ascii=False)


def render_dict(**context):
    try:
        template = Template(template_schema)
        temp_data = template.render(**context)
        return json.loads(temp_data)
    except Exception as e:
        print e


def get_from_template(**product):
    tmp_in = {"data": product}
    return render_dict(**tmp_in)


def convert_name(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()


def create_command_mapping_file(ra_name, products_path):
    products = get_products(products_path)
    resource_path = os.path.join(ra_name, "model/resources")
    for product in products:
        resource_type = product.get('resource_type')
        name = resource_type.split(".")[2]
        path = os.path.join(resource_path, resource_type)
        if not os.path.exists(path):
            product['name'] = convert_name(name)
            data = get_from_template(**product)
            create_file(path, data)
            print "Command mapping files created for {0}".format(product.get('name'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", help="Path of  RA")
    args = parser.parse_args()
    if not args.p:
        print "Enter RA Name"
        exit(0)
    else:
        path = get_products_path(args.p)
    create_command_mapping_file(args.p, path)
