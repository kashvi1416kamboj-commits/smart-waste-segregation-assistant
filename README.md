# smart-waste-segregation-assistant
♻️ Smart Waste Segregation Assistant

An AI-based prototype that analyzes an uploaded image of waste and helps identify the object and determine its appropriate waste category and disposal guidance.

📌 About the Project

The Smart Waste Segregation Assistant is designed to make waste segregation easier for users. The application allows users to upload an image of a waste item and uses a vision-language model to analyze the image.

Based on the identified object, the application provides a suitable waste category and basic disposal guidance.

✨ Features

* Upload an image of a waste item
* AI-based image analysis
* Identification of objects present in the image
* Waste category classification
* Disposal and recycling guidance
* Simple and interactive web interface

🛠️ Technologies Used

* Python
* Streamlit – Web application interface
* Pillow (PIL) – Image processing
* Ollama – Local AI model integration
* Moondream – Vision-language model

🔄 How It Works

User uploads an image
        ↓
Image is processed using Pillow
        ↓
Moondream analyzes the image
        ↓
Object/waste item is identified
        ↓
Waste category is determined
        ↓
Disposal guidance is displayed

⚠️ Current Limitations

This is an initial prototype. The vision model may sometimes identify the object correctly but may not always determine the exact waste category on its own. The project therefore combines AI-based identification with predefined waste-classification rules.

The accuracy may vary depending on the image, object type, lighting, and background.

🚀 Future Improvements

* Improve waste classification accuracy
* Support more types of waste
* Integrate more advanced vision models
* Add real-time camera input
* Provide more detailed recycling information
* Improve handling of ambiguous waste items

▶️ How to Run

1. Clone the repository

git clone <your-github-repository-link>
cd smart-waste-segregation-assistant

2. Create and activate a virtual environment

python -m venv venv

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

3. Install the required packages

pip install -r requirements.txt

4. Make sure Ollama is installed and the required model is available.

5. Run the application

streamlit run app.py

The application will open in your browser.

👩‍💻 Project Status

Prototype / Student Project

This project was developed as a learning project to explore AI-powered image analysis and practical waste segregation.