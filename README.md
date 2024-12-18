# AI Readiness Assessment Tool with GPT Integration

This is an interactive web-based tool designed to evaluate your organization's readiness for AI adoption. With the added GPT integration, users can receive personalized enhancement suggestions based on their assessment results.

---

## Features

1. **Interactive Assessment**:
   - Covers key areas like Organizational Readiness and Regulatory Compliance.
   - Users can check applicable options to calculate their readiness scores.
   
2. **Visualization**:
   - Displays readiness scores using dynamic bar charts.

3. **GPT-Enhanced Suggestions**:
   - Submits assessment results to OpenAI's GPT model for tailored improvement suggestions.

4. **Simple API Integration**:
   - Flask backend handles communication with the GPT API.

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ai-readiness-assessment.git
Run the Backend API:

Navigate to the project folder.
Install dependencies:
bash
Copy code
pip install flask openai
Start the Flask server:
bash
Copy code
python api_app.py
Open the Frontend:

Open updated_index.html in your browser.
Complete the Assessment:

Check the boxes for questions relevant to your organization.
Click "Submit" to view readiness scores.
Get Enhancement Suggestions:

Click "Get Enhancement Suggestions" to send your results to GPT.
View personalized suggestions displayed on the webpage.
File Structure
api_app.py: Flask backend for handling GPT requests.
updated_index.html: Main HTML file for the assessment tool.
updated_script.js: JavaScript file for frontend interactivity and API calls.
style.css: (Optional) Styles for the tool (if needed).
Technologies Used
Frontend:

HTML, CSS, JavaScript
Chart.js for visualization
Backend:

Flask for API integration
OpenAI API for GPT suggestions
Future Enhancements
Add more categories to the assessment (e.g., Data Governance, Ethical AI).
Enable user authentication for saving and revisiting results.
Allow exporting results and suggestions as PDFs.
License
This project is licensed under the MIT License. Feel free to use and modify it.

Demo
Host the backend and frontend locally or deploy the backend on a platform like Heroku or AWS. Open the frontend in a browser to start the assessment process.

