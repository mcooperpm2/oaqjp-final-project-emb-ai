from flask import Flask, render_template, request # Import Flask tools for web app
from EmotionDetection.emotion_detection import emotion_detector # Import emotion detector function

app = Flask(__name__) # Create Flask app

@app.route("/") # Route for home page
def home():
    return render_template("index.html") # Load index.html page

@app.route("/emotionDetector") # Route for emotion detector
def emotion_detector_route():

    # Get text entered by user from the webpage
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass user text to emotion detector function
    response = emotion_detector(text_to_analyze)

    # Check if dominant emotion is None for blank input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return formatted response to customer
    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

# Run Flask app on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)