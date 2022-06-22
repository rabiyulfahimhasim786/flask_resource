import os

path = 'test'

# Check whether the specified path exists or not
isExist = os.path.exists(path)
print('path was exist')

if not isExist:
    # Create a new directory because it does not exist 
    os.makedirs(path)
    print("The new directory is created!")