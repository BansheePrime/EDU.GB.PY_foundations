#!/usr/bin/env python3
# Разбор решения преподавателя
# pipenv shell
# pip install pyyaml
import yaml
import os

data_yaml = {'my_project':
    [{'settings': [
        '__init.py__', 'dev.py', 'prod.py'
    ],
    },
        {'mainapp': [
            '__init__.py', 'models.py', 'views.py', {'templates': [{
                'mainapp': ['base.html', 'index.html']}]
            }]},
        {'authapp': ['__init.py__', 'models.py', 'views.py', {'templates': [{
            'authapp': ['base.html', 'index.html']}]
        }
                    ]
        }
    ]
}

file = open('config.yaml', 'w')
file.write(yaml.dump(data_yaml))
file.close()

with open('config.yaml') as yaml_file:
    data_yaml = yaml.safe_load(yaml_file)


def create_data(data):
    for folder, data_temps in data.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for data_tmp in data_temps:
            if isinstance(data_tmp, dict):
                create_data(data_tmp)
            else:
                if os.path.exists(data_tmp):
                    if '.' in data_tmp:
                        with open(data_tmp, 'w') as f:
                            f.write('')
    else:
        os.chdir('../')

create_data(data_yaml)