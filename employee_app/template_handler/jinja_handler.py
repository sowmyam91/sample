import json
import os
import ast
from jinja2 import Environment, FileSystemLoader


def render_dict(tpl_path, **context):
    path, filename = os.path.split(tpl_path)
    return Environment(
        loader=FileSystemLoader(path or './')
    ).get_template(filename).render(data=context)


def render_multiple_dict(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return Environment(
        loader=FileSystemLoader(path or './')
    ).get_template(filename).render(context)


def convert_response(template_path, *args, **kwargs):
    temp_data = render_dict(template_path, **kwargs)
    print temp_data
    return ast.literal_eval(temp_data)

# data = {'SALARY': 20000.0, 'first_name': u'johnty', 'last_name': u'rd', 'designation': u'SE',
#         'expirience': 3, 'business_unit': 2, 'ADDRESS': u'Mumbai', 'id': 2}
# # data = json.dumps(data)
#
# t = render_dict('../templates/employee_details', **data)
# a = ast.literal_eval(t)
# print a
# print dict(a)
