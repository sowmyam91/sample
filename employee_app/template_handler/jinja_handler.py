import os
import ast
from jinja2 import Environment, FileSystemLoader


def render_dict(tpl_path, **context):
    try:
        path, filename = os.path.split(tpl_path)
        return Environment(
            loader=FileSystemLoader(path or './')
        ).get_template(filename).render(context)
    except Exception as e:
        print e


def convert_response(template_path, **kwargs):
    temp_data = render_dict(template_path, **kwargs)
    return ast.literal_eval(temp_data)
