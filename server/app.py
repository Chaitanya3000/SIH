from flask import Flask, jsonify,request
from career_recommendation import recommend_career
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your Flask app


@app.route('/api/run-python', methods=['GET'])
def run_python_code():
    # Your Python code goes here
    result = "Hello from Python!"
    return jsonify({'result': result})

@app.route('/api/recommend-career', methods=['POST'])
def recommend_career_api():
    try:
        data = request.get_json()
        user_interests = data['interests']
        recommendation = recommend_career(user_interests)

        return jsonify(recommendation)
    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route('/api/speech', methods=['GET', 'POST'])
def speech_recognition_api():
    if request.method == 'POST':
        try:
            # Replace with your speech recognition and text-to-speech logic here
            # For example, you can call the functions from speech_recognition.py
            data = request.get_json()
            print(data)
            import speech_recognition as sr
            import win32com.client

            def say(text):
                speaker = win32com.client.Dispatch("SAPI.SpVoice")
                speaker.Speak(text)

            def takeCommand():
                r = sr.Recognizer()
                print("hi......")
                with sr.Microphone() as source:
                    r.pause_threshold = 1
                    audio = r.listen(source)
                    query = r.recognize_google(audio, language="en-in")
                    print("talked")
                    print(f"User said: {query}")
                    return query

            print("Listening.....")
            t = "Hello"
            say(t)
            say("Recommended Career:")
            say(data["Recommendedcareer"])
            say("Recommended Undergraduate Course")
            say(data["UndergraduateCourse"])
            say("Recommended Postgraduate Course")
            say(data["PostgraduateCourse"])
            text = takeCommand()
            say(text)

            return jsonify({'message': 'Speech recognition and text-to-speech completed successfully'})
        except Exception as e:
            return jsonify({'error': str(e)})
    elif request.method == 'GET':
        # Handle GET request here (if needed)
        return jsonify({'message': 'GET request received for /api/speech'})


if __name__ == '__main__':
    app.run(debug=True)
