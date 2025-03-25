import sys
import os
import json
args = sys.argv
arg = args[1]
prog_file = args[0]

print(f'Hello {arg} from {prog_file}')

if len(sys.argv) ==2:
    ds_names = json.loads(sys.argv[1])
    print(ds_names)
    print("hi")
else:
    print("------------------------------")
    print(args[0])
    print(args[1])
        


# host = os.environ.get('HOST')
# print(f'Connecting to {host}')


# appdev -> appdbdev (retail_db, retail_user, retaildevpassword)

# appuat -> appuatdb (retail_db, retail_user, 12345678)