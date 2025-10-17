from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the pipeline using a basic GPT-2 model (or try other open-source models)
generator = pipeline('text-generation', model='gpt2')

@app.route('/plan', methods=['POST'])
def generate_plan():
    data = request.json
    goal = data.get('goal')

    if not goal:
        return jsonify({'error': 'Please provide a goal'}), 400

    prompt = f"Break down this goal into actionable tasks with deadlines and dependencies:\n{goal}\nTasks:"
    # Generate the plan using the local model
    response = generator(prompt, max_length=256, num_return_sequences=1)
    plan = response[0]['generated_text'].replace(prompt, '').strip()

    return jsonify({'plan': plan})

if __name__ == '__main__':
    app.run(debug=True)
