# Test 1: correct investment window (currently only checks if it's a dictionary)

import json

def test1(dataFile):

    try:
        with open(dataFile) as actFile:
            data = json.load(actFile)

            if isinstance(data, dict):
                print("PASS")
                return len(data)
            else:
                print("FAIL: Invalid file type")        # Currently returns this
    
    except FileNotFoundError:
        print("FAIL: File not found")

    except json.JSONDecodeError:
        print("FAIL: Unable to parse JSON")

days = test1('FNGD_data.json')
print(days)

# Test 2:

# Test 3:
