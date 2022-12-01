# Module to strip and sort desired keys from TwitterAG JSON responses
import json

def strip(json_obj, search_key, target_id, target_type):

    output_dictionary = {}
    target = str(target_id)
    t_type = str(target_type)

    output_dictionary.update([("target_types", target_type)])

    for key in json_obj:
        if key in ["data"]:
            for sub_key in json_obj[key]:
                if search_key == sub_key:
                    output_dictionary.update([(target, json_obj[key][sub_key])])
        else:
            pass

    info_out = json.dumps(output_dictionary)

    return info_out
           # for sub_key in json_obj[key]:
               # if value == sub_key:
                   # output_dictionary.update({target_id : {value : json_obj[key][sub_key]}})


    #info_out = json.dumps(output_dictionary)
    
    #return info_out