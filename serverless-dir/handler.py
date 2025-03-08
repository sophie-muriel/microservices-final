import json


def function_1(event, context):
    body ={
        "First Name": "Sebastián",
        "Surname": "Cruz",
        "Age": 34,
        "Favourite Colour": "Blue",
        "Favourite Game": "Age of empires"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def function_2(event, context):
    body = {
        "One" : 1,
        "Two" : 2,
        "Three" : 3,
        "Four" : 4,
        "Five" : 5,
        "Six" : 6,
        "Seven" : 7,
        "Eight" : 8,
        "Nine" : 9,
        "Ten" : 10,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response