import requests # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyze): #Defining a function named emotion_detector to take a string input (text_to_analyze)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' #URL of the emotion detector service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} #Set the headers for the required API request
    myobj = {"raw_document": { "text": text_to_analyze }} #Create a dictionary of the text to be analyzed
    response = requests.post(url, json = myobj, headers=header) # Sending a POST request to the API with the text and headers
    return response.text #Returns the response text from the API