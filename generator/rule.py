from typing import Union

MissingString = Union[str, None]
MissingStringList = Union[list[str], None]


class Rule:
    def __init__(self):
        self.name: MissingString = None
        self.type: MissingString = None
        self.description: MissingString = None
        self.categories: MissingStringList = None
        self.value: MissingString = None
        self.strict: bool = True
        self.options: MissingStringList = None
        self.extras: MissingStringList = None
        self.validators: MissingStringList = None

    def build(self):
        pass

    def __repr__(self):
        return f'{self.name}\n' \
               f'Type: {self.type}\n' \
               f'Categories: {self.categories}\n' \
               f'Description: {self.description}\n' \
               f'Extras: {self.extras}\n' \
               f'Default Value: {self.value}\n' \
               f'Options: {self.options}\n' \
               f'Strict: {self.strict}\n' \
               f'Validators: {self.validators}\n'


def get_default_values_for_type(value_type):
    match value_type:
        case 'boolean':
            return 'false'
        case 'int':
            return '0'
        case 'String':
            return ''
