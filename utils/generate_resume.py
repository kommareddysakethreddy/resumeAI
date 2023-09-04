
from jinja2 import Template

def generate_resume(json_data, template_file_path=r"./templates/resume_template.html"):
    with open(template_file_path, 'r') as template_file:
        template_content = template_file.read()
    template = Template(template_content)
    rendered_html = template.render(**json_data)
    # write to example.html
    with open('example.html', 'w') as f:
        f.write(rendered_html)
    return rendered_html