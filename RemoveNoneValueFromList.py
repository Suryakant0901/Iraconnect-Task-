# Remove None values from a list

items = input("Enter items separated by commas: ").split(",")

result = []

for item in items:
    item = item.strip()

    if item.lower() != "none":
        result.append(item)

print(result)