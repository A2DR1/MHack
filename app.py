from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
from openai import OpenAI
from openai import OpenAI
import markdown

# import custom function for image analysis
from image_analysis import analyze_image_with_gpt4
from recipe_recommendation import generate_normal_recipe_recommendation, generate_healthy_recipe_recommendation, generate_shopping_list
from Yolo import detect_image

client = OpenAI(api_key="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")
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set your OpenAI API key

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Home route
@app.route('/')
def home():
    return render_template('main.html')

# Start route
@app.route('/start')
def start():
    return render_template('start.html')

# Upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'picture' not in request.files:
        return "No file part"
    file = request.files['picture']
    if file.filename == '':
        return "No selected file"
    if file:
        # Save the original uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Open the image with Pillow for processing
        with Image.open(file_path) as img:
            # Resize the image to a specific size (e.g., 800x600)
            img = img.resize((800, 600))

            # Save the processed image (overwrite original)
            img.save(file_path)

        # Use the OpenAI API to generate a response about the image processing
        # Path to your image file
        image_path = file_path
        chat_response = analyze_image_with_gpt4(image_path)
        # sample_response = """Here are the ingredients visible inside the fridge: 
        #                     - Chicken (cooked) 
        #                     - Potatoes (cooked with chicken) 
        #                     - Tomatoes 
        #                     - Yellow bell peppers 
        #                     - Leafy greens (possibly lettuce) 
        #                     - Blueberries (in a container) 
        #                     - Mixed salad (in a container) 
        #                     - Eggs 
        #                     - Some type of liquid (possibly a bottle of wine and water) 
        #                     Please note that some items are in containers and their specific contents are not clearly visible."""
        # chat_response = sample_response

        # Use YOLO to detect ingredients in the image
        yolo_ingredient = detect_image(image_path)
        chat_response += "\n" + "\n" + "Ingredients detected by YOLO: " + yolo_ingredient

        normal_recipe_recommendation = generate_normal_recipe_recommendation(chat_response)
        shopping_list = generate_shopping_list(chat_response)
        healthy_recipe_recommendation = generate_healthy_recipe_recommendation(chat_response, shopping_list)

        response = chat_response + "\n" + "\n" + normal_recipe_recommendation + "\n" + "\n" + shopping_list + "\n" + "\n" + healthy_recipe_recommendation 

        # save the response to a file
        with open(os.path.join(app.config['UPLOAD_FOLDER'], 'response.txt'), 'w') as f:
            f.write(response)
        # Redirect to show the processed image with a response from ChatGPT
        return redirect(url_for('show_image', filename=file.filename, chat_response=response, normal = normal_recipe_recommendation
                                , shopping = shopping_list, healthy = healthy_recipe_recommendation))

@app.route('/uploads/<filename>')
def show_image(filename):
    chat_response = request.args.get('chat_response', '')
    normal = markdown_output(request.args.get('normal', ''))
    shopping = markdown_output(request.args.get('shopping', ''))
    healthy = markdown_output(request.args.get('healthy', ''))
    return render_template('display.html', filename=filename, chat_response=chat_response, normal = normal, 
                           shopping = shopping, healthy = healthy) 

def markdown_output(text_input):
    # Example Markdown content
    markdown_content = text_input

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)
    return html_content



if __name__ == "__main__":
    app.run(debug=True)