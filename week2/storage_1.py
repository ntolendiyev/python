import sys
import os
import tempfile
import argparse as ar

parser = ar.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

val = str(args.val)
key = str(args.key)
key_value_list=dict()

if not os.path.exists(storage_path):
    with open(storage_path, 'w') as f:
        f.write("")


with open(storage_path, 'r') as f:
    data_text = f.read()
    if data_text:
        key_value_list=eval(data_text)

#print(key_value_list)

if args.val:
    if key in key_value_list:
        key_value_list[key] += ", " + val
    else:
        key_value_list[key] = val

else:
    if key in key_value_list:
        print(key_value_list[key])
    else:
        print(" ")


with open(storage_path, 'w') as f:
    f.write(str(key_value_list))

        
