#!/usr/bin/python3

from customer import Customer

## Use Organization API Keys generated in Rapid7 Platform
## User Input for required information
TOKEN_ORIGINAL = input("Enter Original Customer API Key: ")
TOKEN_DESTINATION = input("Enter Destination Customer API Key: ")

# TOKEN_ORIGINAL = ('REDACTED')       # source
# TOKEN_DESTINATION = ('REDACTED')    # destination

## Enumerate applications in the original customer
enumerate_origin_apps = Customer(TOKEN_ORIGINAL)
if TOKEN_ORIGINAL != "":
    ##enumerate_origin_apps.get_apps()
    app_enumeration = enumerate_origin_apps.get_apps()
else:
    print("Original Customer API Key is missing.")

# print(app_enumeration)

create_app_in_cust_two = Customer(TOKEN_DESTINATION)
for app in app_enumeration:
    create_app_in_cust_two.create_apps(app['name'], app.get('description', ''))

# """

# ## Enumerate app_list to create a list of apps with their appid, name and description
# ## This will be used to feed back into the customer class to tell the
# ## create_apps function what apps to create
# ## Is this the correct place to put this or should this work be done in the Customer class??

# # app_name = [app_enumeration]

# # print(app_info(app_enumeration))

# ## Pseudocode for remaining requirements

# """
# """
# - pull app names from old customer -> app_list
#     - app_list - content
#         - app id
#         - app name
#         - app description
# - create apps in new customer based on app name(s) in app_list

# - pull users from old customer -> user_list
#     - user_list - content
#         - user name
#         - user email

# - iterate through apps to pull configs from each app -> config_list
#     - config_list - content
#         - config name
#         - config.xml
#         - files

# - pull app ids and names from new customer -> app_list_new
#     - app_list_new - content
#         - app id
#         - app name

# - upload files from old customer to new customer

# - create configs in new customer based on config name in config_list

# """
