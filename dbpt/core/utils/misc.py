import yaml # ignore

def yaml_coerce(value):
    if isinstance(value, str):
        '''
        yaml.load returns a python project
        it converrs string dict to python dict
        Useful becauaw we need to stringify settings this way (like in dockerfile)
        '''
        
        
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']
    
    return value