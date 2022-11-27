# Module to strip and sort desired keys from TwitterAG JSON responses
import json

def strip(json_obj, dict_keys, target_id, target_type):

    if [json_obj, dict_keys, target_id, target_type] == None:

        print("Error: One or more parameters came back as \'None\' type.")
        return

    else:

        output_dictionary = {}

        for key in json_obj:
            if key in dict_keys:
                output_dictionary.update({target_id : {key : json_obj[key]}})

        json_return_obj = json.dumps(output_dictionary)
        
        return json_return_obj