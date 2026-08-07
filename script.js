document.getElementById('predictForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const data = {
        CGPA: parseFloat(document.getElementById('CGPA').value),
        Internships: parseInt(document.getElementById('Internships').value),
        Projects: parseInt(document.getElementById('Projects').value),
        WorkshopsCertifications: parseInt(document.getElementById('WorkshopsCertifications').value),
        AptitudeTestScore: parseInt(document.getElementById('AptitudeTestScore').value),
        SoftSkillsRating: parseFloat(document.getElementById('SoftSkillsRating').value),
        ExtracurricularActivities: document.getElementById('ExtracurricularActivities').value,
        PlacementTraining: document.getElementById('PlacementTraining').value,
        SSC_Marks: parseInt(document.getElementById('SSC_Marks').value),
        HSC_Marks: parseInt(document.getElementById('HSC_Marks').value)
    };

    const response = await fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    const stampEl = document.getElementById('result');

    stampEl.classList.remove('show', 'placed', 'not-placed');
    void stampEl.offsetWidth;

    if (result.placement_status === 'Placed') {
        stampEl.textContent = 'Placed';
        stampEl.classList.add('placed');
    } else {
        stampEl.textContent = 'Not Placed';
        stampEl.classList.add('not-placed');
    }

    stampEl.classList.add('show');
});