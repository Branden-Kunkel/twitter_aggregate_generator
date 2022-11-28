# Module to strip and sort desired keys from TwitterAG JSON responses
import json

def strip(json_obj, search_keys, target_id, target_type):

    output_dictionary = {}

    for value in search_keys:
        for key in json_obj:
            if key in value:
                output_dictionary.update({target_type : {target_id : {key : json_obj[key]}}})

    info_out = json.dumps(output_dictionary)
    
    
    return info_out