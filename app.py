from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect all 31 inputs
        radius = float(request.form['radius'])
        texture = float(request.form['texture'])
        perimeter = float(request.form['perimeter'])
        # Add remaining features here
        # Example: smoothness = float(request.form['smoothness'])
        
        # Create a feature vector in the correct order
        features = [radius, texture, perimeter]  # Add all 31 features here
        
        # Predict
        prediction = model.predict([features])
        return jsonify({'prediction': f'The result is: {int(prediction[0])}'})
    except Exception as e:
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True)
