import requests # Import the requests library to handle HTTP requests
import json # Import the json library

def emotion_detector(text_to_analyze): #Defining a function named emotion_detector to take a string input (text_to_analyze)
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict" #URL of the emotion detector
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} #Set the headers for the required API request
    myobj = {"raw_document": {"text": text_to_analyze}} #Create a dictionary of the text to be analyzed

    response = requests.post(url, json=myobj, headers=header) #Sending a POST request to the API with the text and headers

    if response.status_code == 400: #Check if blank text was entered
        return { #Return dictionary with None values for invalid input
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text) #Parse the JSON response from API into a Python dictionary

    emotions = formatted_response['emotionPredictions'][0]['emotion'] #Extract the emotion dictionary from the API result

    anger_score = emotions['anger'] #Extracting anger score from the response
    disgust_score = emotions['disgust'] #Extracting disgust score from the response
    fear_score = emotions['fear'] #Extracting fear score from the response
    joy_score = emotions['joy'] #Extracting joy score from the response
    sadness_score = emotions['sadness'] #Extracting sadness score from the response

    dominant_emotion = max(emotions, key=emotions.get) #Determine the dominant emotion with the highest score

    return { #Return a dictionary containing emotion scores and dominant emotion
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }