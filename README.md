# FridgeWhiz

## Overview
**FridgeWhiz** is a smart kitchen companion designed to help college students plan meals effortlessly. Just snap a picture of your fridge, and FridgeWhiz will identify the ingredients and suggest delicious, budget-friendly recipes. FridgeWhiz also provides healthy shopping lists to complement your ingredients, helping you eat well without the stress of meal planning.

## Features
- **Identify Ingredients**: Upload a picture of your fridge, and FridgeWhiz will recognize the ingredients.
- **Recipe Suggestions**: Get normal and healthy recipes based on your available ingredients.
- **Shopping List**: Receive a custom shopping list to help enhance your meals.
- **Healthy Meal Planning**: Balanced recipe suggestions that fit your nutritional goals.

## Requirements
- **Python 3.x**
- **Flask**
- **Pillow** (for image processing)
- **OpenCV** (for image handling)
- **Ultralytics** (for YOLOv8 model)

## Setup Instructions

1. **Clone the Repository**:
   - Clone this repository to your local machine:
     ```sh
     git clone https://github.com/your_username/FridgeWhiz.git
     ```
   - Navigate into the project directory:
     ```sh
     cd FridgeWhiz
     ```

2. **Create a Virtual Environment**:
   - Create a new virtual environment to keep dependencies organized:
     ```sh
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**:
       ```sh
       .\venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```sh
       source venv/bin/activate
       ```

3. **Install Dependencies**:
   - Install the required packages using `requirements.txt`:
     ```sh
     pip install -r requirements.txt
     ```

4. **Download YOLOv8 Model**:
   - Make sure you have the YOLOv8 model saved at the correct location. Download or train a model (`best.pt`) and place it in your project folder.

5. **Run the Application**:
   - Run the Flask app:
     ```sh
     python app.py
     ```
   - Open your browser and navigate to:
     ```
     http://127.0.0.1:5000/
     ```

## Usage
1. **Homepage**: Get started by clicking the **"Start"** button.
2. **Upload Image**: Use the **"Upload"** button to upload a picture of your fridge.
3. **Get Recipes**: View the generated recipes, shopping lists, and healthy meal suggestions.

## File Structure
