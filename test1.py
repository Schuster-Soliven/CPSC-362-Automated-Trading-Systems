# Test 1: correct investment window

import json

def test1(dataFile):

    try:
        with open(dataFile) as actFile:
            data = json.load(actFile)

            if isinstance(dataFile, dict):
                print("PASS")
                return len(data)
            else:
                print("FAIL: Invalid file type")
    
    except FileNotFoundError:
        print("FAIL: File not found")

    except json.JSONDecodeError:
        print("FAIL: Unable to parse JSON")

days = test1('FNGD_data.json')
print(days)