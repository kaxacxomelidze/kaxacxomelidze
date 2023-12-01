from flask import Flask, render_template, request

app = Flask(__name__)

class SmartphoneRecommendation:
    def __init__(self):
        self.questions = [
            {
                'text': 'Choose a product category:',
                'options': ['Smartphone', 'Tablet', 'Laptop', 'Desktop'],
                'next': 'usage'
            },
            {
                'text': '',  # This will be dynamically filled later
                'options': ['Gaming', 'Photo / Video', 'Social Media', 'Audio', 'Global'],
                'next': 'storage'
            },
            {
                'text': 'Great choice! What storage capacity are you looking for?',
                'options': ['64GB', '128GB', '256GB', '512GB'],
                'next': 'budget'
            },
            {
                'text': 'What is your budget range for the smartphone?',
                'options': ['$200-$400', '$400-$600', '$600-$800', '$800-$1000'],
                'next': 'brand'
            },
            {
                'text': 'Do you have any preferred brand for the smartphone?',
                'options': ['Samsung', 'Apple', 'Xiaomi', 'OnePlus', 'Google'],
                'next': 'color'
            },
            {
                'text': 'Any preferred color for the smartphone?',
                'options': ['Black', 'White', 'Blue', 'Red'],
                'next': 'result'
            }
        ]
        self.user_responses = {}

    def get_current_question(self):
        if len(self.user_responses) < len(self.questions):
            current_question = self.questions[len(self.user_responses)]
            if '{category}' in current_question['text']:
                # Replace '{category}' with the actual selected category
                current_question['text'] = current_question['text'].format(category=self.user_responses.get('category', ''))
            return current_question
        else:
            return None

    def get_recommendation(self):
        # Implement your recommendation logic based on user responses
        # This is a placeholder, replace it with your actual logic
        return "Your recommendation goes here"

wilbot = SmartphoneRecommendation()

@app.route('/')
def index():
    current_question = wilbot.get_current_question()
    if current_question:
        return render_template('question.html', question=current_question)
    else:
        return render_template('result.html', recommendation=wilbot.get_recommendation())

@app.route('/answer', methods=['POST'])
def answer():
    current_question = wilbot.get_current_question()
    if current_question:
        user_answer = request.form['answer']
        wilbot.user_responses[current_question['next']] = user_answer
        return render_template('question.html', question=wilbot.get_current_question())
    else:
        return render_template('result.html', recommendation=wilbot.get_recommendation())

if __name__ == '__main__':
    app.run(debug=True)
