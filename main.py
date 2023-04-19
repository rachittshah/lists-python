def merge_lists(list_1, list_2) -> list:
    # Create a new dictionary to store the combined dictionaries
    combined_dict = {}
    
    # Add dictionaries from list_1 to combined_dict
    for item in list_1:
        item_id = item.get("id")
        if item_id:
            combined_dict[item_id] = item

    # Update the combined_dict with dictionaries from list_2
    for item in list_2:
        item_id = item.get("id")
        if item_id:
            if item_id in combined_dict:
                combined_dict[item_id].update(item)
            else:
                combined_dict[item_id] = item

    # Create a new list with the combined dictionaries
    list_3 = list(combined_dict.values())
    
    return list_3

list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

list_3 = merge_lists(list_1, list_2)
print(list_3)
