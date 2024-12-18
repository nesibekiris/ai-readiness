
async function submitToGPT() {
    const sections = document.querySelectorAll('.section');
    const scores = [];

    sections.forEach(section => {
        const questions = section.querySelectorAll('.question');
        let sectionScore = 0;
        questions.forEach(question => {
            if (question.checked) sectionScore++;
        });
        scores.push(sectionScore);
    });

    const assessmentData = {
        "Organizational Readiness": scores[0],
        "Regulatory Compliance": scores[1]
    };

    document.getElementById('assessment-data').value = JSON.stringify(assessmentData);

    const response = await fetch('http://127.0.0.1:5000/enhance', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(assessmentData)
    });

    const result = await response.json();
    document.getElementById('gpt-response').innerText = result.message;
}
