from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from models import GameState
import os
import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

app = Flask(__name__)
app.secret_key = os.environ.get('GOOGLE_API_KEY')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/<int:box_id>')
def game(box_id):
    session['game_state'] = GameState(character="Your Character", box_id=box_id).__dict__
    return render_template('game.html', box_id=box_id)

@app.route('/start_game', methods=['POST'])
def start_game():
    game_state = session.get('game_state')
    if game_state:
        return redirect(url_for('gameplay', box_id=game_state['box_id']))
    return redirect(url_for('index'))

@app.route('/gameplay/<int:box_id>')
def gameplay(box_id):
    game_state = session.get('game_state')
    print(game_state)
    if game_state:
        gs = GameState(**game_state)
        return render_template('gameplay.html', box_id=box_id, story_progress=gs.story_progress)
    return redirect(url_for('index'))


@app.route('/make_choice', methods=['POST'])
def make_choice():
    choice = request.json['choice']
    game_state = session.get('game_state')

    if game_state:
        gs = GameState(**game_state)
        gs.add_choice(choice)

        new_story = generate_story(gs)
        gs.update_story(new_story)

        session['game_state'] = gs.__dict__

        return {
            "story_progress": gs.story_progress,
            "choices": gs.choices,
            "box_id": gs.box_id
        }

@app.route('/get_game_state')
def get_game_state():
    game_state = session.get('game_state')
    if game_state:
        gs = GameState(**game_state)
        return {
            "character_image": "/static/images/character_1.png",  # Example, replace with actual data
            "story_progress": gs.story_progress,
            "choices": gs.choices,
            "box_id": gs.box_id  # Ensure box_id is included
        }
    return redirect(url_for('index'))


def generate_story(gs):
    # Generate story continuation using GPT API
    prompt = f"Character: {gs.character}, Choices: {gs.choices}, Current Story: {gs.story_progress}"

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
        history=[
        ]
    )

    response = chat_session.send_message(prompt)

    story_text = response.text

    # Example: Use a default background image if not set
    background_image = "static/images/game_background.png"

    return story_text



if __name__ == '__main__':
    app.run(debug=True)
