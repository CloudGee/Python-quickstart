# Method Definitions:
computer = {
    "brand": "HP",
    "RAM": "8GB",
    "CPU": "i7",
    "storage": "1TB HDD",
}

# Lookup Methods:
brand = computer["brand"]
print("Computer brand:", brand)  # 输出: Computer brand: HP

ram = computer.get("RAM", None)
bios = computer.get("bios", "No bios in dict")
print("RAM:", ram)  # 输出: RAM: 8GB
print("BIOS:", bios)  # 输出: No bios in dict

keys_list = computer.keys()
print("Keys:", keys_list)  # 输出: Keys: dict_keys(['brand', 'RAM', 'CPU', 'storage'])
# brand
# RAM
# CPU
# storage
for i in keys_list:
    print(i)

values_list = computer.values()
print("Values:", values_list)  # 输出: Values: dict_values(['HP', '8GB', 'i7', '1TB HDD'])
# HP
# 8GB
# i7
# 1TB HDD
for i in values_list:
    print(i)

items_list = computer.items()
print(
    "Items:", items_list
)  # 输出: Items: dict_items([('brand', 'HP'), ('RAM', '8GB'), ('CPU', 'i7'), ('storage', '1TB HDD')])
# The brand of this computer is HP
# The RAM of this computer is 8GB
# The CPU of this computer is i7
# The storage of this computer is 1TB HDD
for key, value in items_list:
    print(f"The {key} of this computer is {value}")

# Add Methods:
computer["GPU"] = "NVIDIA GTX 1650"
print("Updated computer dictionary:", computer)
# 输出: Updated computer dictionary: {'brand': 'HP', 'RAM': '8GB', 'CPU': 'i7', 'storage': '1TB HDD', 'GPU': 'NVIDIA GTX 1650'}

computer.update({"Bluetooth": "Yes", "USB Ports": 4, "CPU": "i9"})
print("Updated computer dictionary:", computer)
# 输出: Updated computer dictionary: {'brand': 'HP', 'RAM': '8GB', 'CPU': 'i9', 'storage': '1TB HDD', 'GPU': 'NVIDIA GTX 1650', 'Bluetooth': 'Yes', 'USB Ports': 4}

default_value = computer.setdefault("Graphics", "Intel UHD Graphics")
print("Default Value:", default_value)
# 输出: Default Value: Intel UHD Graphics

default_value2 = computer.setdefault("GPU", "AMD Radeon")
print("Default Value:", default_value2)
# 输出: Default Value: NVIDIA GTX 1650

default_value3 = computer.setdefault("CPU", "i3")
print("Default Value:", default_value3)
# 输出: Default Value: i9

print(computer) # {'brand': 'HP', 'RAM': '8GB', 'CPU': 'i9', 'storage': '1TB HDD', 'GPU': 'NVIDIA GTX 1650', 'Bluetooth': 'Yes', 'USB Ports': 4, 'Graphics': 'Intel UHD Graphics'}

# Delete Methods:
computer.pop("storage")
print("Updated computer dictionary:", computer)
# 输出: Updated computer dictionary: {'brand': 'HP', 'RAM': '8GB', 'CPU': 'i7', 'GPU': 'NVIDIA GTX 1650', 'Bluetooth': 'Yes', 'USB Ports': 4, 'Graphics': 'Intel UHD Graphics'}

last_item = computer.popitem()
print("Removed last item:", last_item)
print("Updated computer dictionary:", computer)
# 输出: Removed last item: ('Graphics', 'Intel UHD Graphics')
# 输出: Updated computer dictionary: {'brand': 'HP', 'RAM': '8GB', 'CPU': 'i7', 'GPU': 'NVIDIA GTX 1650', 'Bluetooth': 'Yes', 'USB Ports': 4}


computer = {
    "Host": {"CPU": 1300, "Memory": 400, "Hard Disk": 200},
    "Monitor": 1000,
    "Mouse": 60,
    "Keyboard": ["Mechanical Keyboard", "Membrane Keyboard"],
}

print(type(computer["Host"])) # <class 'dict'>
print(type(computer["Keyboard"])) # <class 'list'>

# Accessing the value of the "Monitor" key.
monitor_price = computer["Monitor"]
print("Monitor price:", monitor_price)  # Output: Monitor price: 1000

# Accessing the value of the "Memory" key within the "Host" key.
host_memory = computer["Host"]["Memory"]
print("Host memory:", host_memory)  # Output: Host memory: 400

# Modifying the value of the "Mouse" key.
computer["Mouse"] = 70
print("Updated mouse price:", computer["Mouse"])  # Output: Updated mouse price: 70

# Adding a new key-value pair to the "Host" key.
computer["Host"]["GPU"] = 250
print("Updated computer dictionary:", computer)
# Output: Updated computer dictionary: {'Host': {'CPU': 1300, 'Memory': 400, 'Hard Disk': 200, 'GPU': 250}, 'Monitor': 1000, 'Mouse': 70, 'Keyboard': ['Mechanical Keyboard', 'Membrane Keyboard']}

# Removing the "Hard Disk" key from the "Host" key.
del computer["Host"]["Hard Disk"]
print("Updated computer dictionary:", computer)
# Output: Updated computer dictionary: {'Host': {'CPU': 1300, 'Memory': 400, 'GPU': 250}, 'Monitor': 1000, 'Mouse': 70, 'Keyboard': ['Mechanical Keyboard', 'Membrane Keyboard']}

computer["Keyboard"].append("Other keyboard")
print("Updated keyboard dictionary:", computer["Keyboard"])
# Output: Updated keyboard dictionary: ['Mechanical Keyboard', 'Membrane Keyboard', 'Other keyboard']

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)