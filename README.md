# lists-python

Student List Merger
This script merges two lists of student dictionaries based on their "id" field. The goal is to create a new list containing all information about each student from both lists in one single dictionary.

Code Explanation
The main function in this script is merge_lists(list_1, list_2), which takes two lists of dictionaries as input and returns a merged list of dictionaries.

Approach
First, we create a new dictionary called combined_dict to store the combined dictionaries from both input lists. The keys in this dictionary will be the student "id" values, and the values will be the dictionaries themselves.

We iterate through list_1, and for each dictionary in list_1, we add it to combined_dict using the "id" value as the key.

We iterate through list_2, and for each dictionary in list_2, we check if the "id" value already exists in combined_dict. If it does, we update the existing dictionary in combined_dict with the new values from list_2. If the "id" value does not exist in combined_dict, we add the new dictionary from list_2 to combined_dict.

We create a new list called list_3 and populate it with the values (i.e., the dictionaries) from combined_dict.

Finally, the function returns list_3, the merged list of dictionaries.

# Usage

```python
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
```

# Output

```[    {'id': '1', 'name': 'Shrey', 'age': 25, 'marks': 100},    {'id': '3', 'age': 10, 'name': 'Hello', 'marks': 90, 'roll_no': 11, 'extra_info': {'hello': 'world'}},    {'id': '2', 'name': 'World', 'age': 24}]```
