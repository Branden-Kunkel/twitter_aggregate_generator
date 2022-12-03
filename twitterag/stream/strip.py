# Module to strip and sort desired keys from TwitterAG JSON responses
import json

def strip(file_path, search_keys, target_type):

    try:

        new_write_dict = {}


        with open(file_path, mode='r') as readfile:

            parsable_json_object = json.load(readfile)

            for value in search_keys:
                for key in parsable_json_object:
                    if key in ["data"]:
                        for sub_key in parsable_json_object[key]:
                            if value == sub_key:
                                new_write_dict.update({sub_key : parsable_json_object[key][sub_key]})
                            else:
                                pass
                    else:
                        pass

        file_name_annotation = "strip-{}.json".format(str(target_type))
        info_out = json.dumps(new_write_dict, indent=4, sort_keys=True)

        with open(file_name_annotation, mode='a') as writefile:
            json.dump(info_out, writefile, indent=4, sort_keys=True)

        return

    except FileNotFoundError as fp_err:
        print("Error: File not found. This is an odd behavior. Please report to dev @kunkel.branden6130@gmail.com")
        return
