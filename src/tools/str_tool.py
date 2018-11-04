# coding: utf-8

"""
FIXME
"""

def get_config_name(module_name: str) -> str:
    return '../configs/{}.yaml'.format(module_name[2:-2])
