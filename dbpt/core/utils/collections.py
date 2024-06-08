def deep_update(base_dict, update_with):
    # iterate over the items in the update_with dict
    for key, value in update_with.items():
        
        # if the value is a dict, get the value of the key in the base_dict
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key, {})
            
            # if the value of the key in the base_dict is a dict, call deep_update recursively
            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
                
            # if the value of the key in the base_dict is not a dict, update the value in the base_dict    
            else:
                base_dict[key] = value
        # if the value is not a dict, update the value in the base_dict
        else:
            base_dict[key] = value
            
    return base_dict