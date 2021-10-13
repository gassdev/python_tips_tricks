## working with json data using python json module

```python
import json
# string containing a json document to python object
# example
string_containing_a_json = '''
    {
        "key": "value"
    }
'''
data = json.loads(string_containing_a_json)

# file object containing a json document to python object
# example
with open('file.json') as f:
    data = json.load(f)

# python object to json formatted string
# example
string_data = json.dumps(object_data, indent=2, sort_keys=True)

# python object to json data file
# example
with open('file.json', 'w') as f:
    json.dump(object_data, f, indent=2)
```
