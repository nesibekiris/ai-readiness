
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API Key
openai.api_key = "your_openai_api_key"  # Replace with your actual OpenAI API key

@app.route('/enhance', methods=['POST'])
def enhance_assessment():
    data = request.json
    assessment_summary = f"""
    Assessment Results:
    - Organizational Readiness: {data.get('Organizational Readiness', 0)}/4
    - Regulatory Compliance: {data.get('Regulatory Compliance', 0)}/4

    Based on these results, suggest areas for improvement in AI readiness.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in AI readiness assessment for organizations."},
                {"role": "user", "content": assessment_summary}
            ]
        )

        return jsonify({"message": response['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
