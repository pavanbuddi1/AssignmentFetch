import json
import re
def fix_json(file_path):
    res = []
    with open(file_path, 'r') as f:
        # Reading each line from the json file
        for line in f:
            obj = json.loads(line)
            res.append(obj)

    # Writing the fixed JSON data back to the file
    with open(file_path, 'w') as f:
        # Writing the opening square bracket
        f.write('[')
        # Writing each JSON object separated by a comma
        for i, obj in enumerate(res):
            f.write(json.dumps(obj))
            # Adding a comma after each JSON object except for the last one
            if i < len(res) - 1:
                f.write(',')
            f.write('\n')

        # Writing the closing square bracket
        f.write(']')

def fix_uuid_format(obj):
    if '_id' in obj:
        # getting the current UUID value
        current_uuid = obj['_id'].get('$oid')
        if current_uuid:
                # Correcting the UUID format
            corrected_uuid = '-'.join([current_uuid[:8], current_uuid[8:12], current_uuid[12:16], current_uuid[16:20], current_uuid[20:]])
            obj['_id']['$oid'] = corrected_uuid
    return obj

