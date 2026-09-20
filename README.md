# 🎓 Internship Success Predictor

A machine learning web app that predicts whether a student is likely to get **Placed** or **Not Placed** based on their academic record, experience, and skills — powered by a Logistic Regression model, a FastAPI backend, and a clean "candidate dossier"-styled frontend.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688?logo=fastapi)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9-F7931E?logo=scikit-learn)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📖 Overview

This project takes a student's academic and extracurricular profile and predicts their campus placement outcome. It has three parts:

- **Model** — a Logistic Regression classifier trained on ~10,000 student records (`01_explore_data.ipynb`)
- **Backend** — a FastAPI server (`main.py`) that loads the trained model and exposes a `/predict` endpoint
- **Frontend** — a static HTML/CSS/JS page (`index.html`, `script.js`, `style.css`) styled like a candidate assessment dossier, which calls the backend and shows a "Placed" / "Not Placed" stamp

## ✨ Features

- Predicts placement outcome from 10 input features (CGPA, internships, projects, aptitude score, soft skills, etc.)
- Simple REST API built with FastAPI, CORS-enabled for easy frontend integration
- Lightweight, dependency-free vanilla JS frontend with a distinctive dossier/stamp UI
- Model trained and serialized with `joblib` — no retraining needed to run the app
- Jupyter notebook included showing the full data exploration → training → evaluation pipeline

## 🧠 Model Details

| | |
|---|---|
| Algorithm | Logistic Regression (`scikit-learn`) |
| Dataset size | 10,000 student records |
| Train/test split | 80% / 20% (stratified) |
| Accuracy | **~81%** |

**Input features used by the model:**

`CGPA`, `Internships`, `Projects`, `WorkshopsCertifications`, `AptitudeTestScore`, `SoftSkillsRating`, `ExtracurricularActivities`, `PlacementTraining`, `SSC_Marks`, `HSC_Marks`

## 📁 Project Structure

```
internship-success-predictor/
├── main.py                          # FastAPI backend + /predict endpoint
├── placement_model.pkl              # Trained Logistic Regression model
├── requirements.txt                 # Python dependencies
├── 01_explore_data.ipynb            # Data exploration & model training notebook
├── data/
│   └── intership-succes-predictor.csv   # Training dataset
├── index.html                       # Frontend UI
├── script.js                        # Frontend logic (calls the API)
└── style.css                        # Frontend styling
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/internship-success-predictor.git
cd internship-success-predictor
```

### 2. Set up a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the backend

```bash
uvicorn main:app --reload
```

The API will be live at `http://127.0.0.1:8000`. Interactive API docs are available at `http://127.0.0.1:8000/docs`.

### 5. Launch the frontend

Simply open `index.html` in your browser (e.g. with the VS Code "Live Server" extension, or `python -m http.server`). Fill in the candidate's details and click **Assess Candidate** to get a prediction.

> **Note:** The frontend currently calls `http://127.0.0.1:8000/predict` directly, so make sure the backend is running locally before using the UI.

## 🔌 API Reference

### `POST /predict`

Predicts placement status for a given student profile.

**Request body:**

```json
{
  "CGPA": 8.9,
  "Internships": 2,
  "Projects": 3,
  "WorkshopsCertifications": 2,
  "AptitudeTestScore": 85,
  "SoftSkillsRating": 4.2,
  "ExtracurricularActivities": "Yes",
  "PlacementTraining": "Yes",
  "SSC_Marks": 78,
  "HSC_Marks": 82
}
```

**Response:**

```json
{
  "placement_status": "Placed"
}
```

## 🛠️ Tech Stack

- **Backend:** FastAPI, Pydantic, Uvicorn
- **ML:** scikit-learn, pandas, numpy, joblib
- **Frontend:** HTML, CSS, JavaScript (no frameworks)
- **Notebook:** Jupyter

## 🗺️ Roadmap / Ideas for Improvement

- [ ] Make the API URL in `script.js` configurable (env-based) instead of hardcoded
- [ ] Add input validation and better error handling on the frontend
- [ ] Try other models (Random Forest, XGBoost) and compare accuracy
- [ ] Add a probability/confidence score alongside the prediction
- [ ] Deploy backend + frontend (e.g. Render/Vercel) for a live demo

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License.
