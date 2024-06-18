from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Your other routes and functions...

@app.route('/predict', methods=['POST'])
def predict():
    # Get the entered symptoms from the form
    symptoms = request.form['symptoms']

    # Check if the entered symptoms are misspelled
    # Replace this with your actual code to check for misspelling
    if is_misspelled(symptoms):
        # If misspelled, redirect to a page or display a message asking for correct spelling
        return redirect(url_for('spell_check'))

    # If not misspelled, proceed with prediction
    # Your prediction code goes here...

    return render_template('results.html', predicted_disease=predicted_disease)

@app.route('/spell_check')
def spell_check():
    return render_template('spell_check.html')

if __name__ == '__main__':
    app.run(debug=True)
