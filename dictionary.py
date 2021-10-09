
dictionary_example={
    "name":"Ekta",
    "phone":"1234",
    "email":"ekta@gmail.com"
}
print(dictionary_example)
print(dictionary_example["name"])
print(dictionary_example["email"])

sequences={
    "YC1":"ATGATAAGA",
    "YC2":"ATGATAGAA",
    "YC3":"AATGATAG",
    "YC4":"ATATATGATAG",
    "YC5":"ATGATAAAG",
}

print(sequences["YC1"].count("A"))
print(sequences["YC2"].count("A"))


sequences={
    "YC1":"ATGATAAGA",
    "YC2":"ATGATAGAA",
    "YC3":"AATGATAG",
    "YC4":"ATATATGATAG",
    "YC5":"ATGATAAAG",
}

accc_ids=sequences.keys()
print(accc_ids)

sequences_list=sequences.values()
print(sequences_list)

sequences={
    "YC1":{
        "length":45,
        "gc_percentage":86
    },
    "YC2":{
        "length":45,
        "gc_percentage":86
    },
    "YC3":{
        "length":45,
        "gc_percentage":86
    },
    "YC4":{
        "length":45,
        "gc_percentage":86
    },
    "YC5":{
        "length":45,
        "gc_percentage":86
    },
}
print(sequences)

sequences={
    "YC1":{
        "length":{
            "half_length":45,
            "complete_length":90
        },
        "gc_percentage":86
    },
    "YC2":{
        "length":45,
        "gc_percentage":86
    },
    "YC3":{
        "length":45,
        "gc_percentage":86
    },
    "YC4":{
        "length":45,
        "gc_percentage":86
    },
    "YC5":{
        "length":45,
        "gc_percentage":86
    },
}
print(sequences["YC1"])
print(sequences["YC1"]["gc_percentage"])



dictionary_example={
    "name":"Ekta",
    "phone":"1234",
    "email":"ekta@gmail.com"
}

#addition of new data
dictionary_example["address"]="Noida, India"
print(dictionary_example)

#keys

print(dictionary_example.keys())

sequences={
    "YC1":"ATGATAAGA",
    "YC2":"ATGATAGAA",
    "YC3":"AATGATAG",
    "YC4":"ATATATGATAG",
    "YC5":"ATGATAAAG",
}

accc_ids=sequences.keys()
print(accc_ids)

sequences_list=sequences.values()
print(sequences_list)