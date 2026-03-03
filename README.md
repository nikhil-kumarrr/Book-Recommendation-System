# Book Recommendation System
An ML-powered book recommender app built using collaborative filtering and cosine similarity with an interactive Streamlit dashboard.
Select a book and instantly get the top similar recommendations with covers and author details.

##  Features
-  ML-based similarity recommendations
-  Popular books dashboard
-  Instant top-5 recommendations
-  Clean interactive UI
-  Uses Book-Crossing dataset
-  Real-time recommendation engine

##  How It Works
The system uses:
### 1️⃣ Dataset
Book-Crossing Dataset 
containing:
- ISBN
- Book Title
- Author
- User Ratings
- Book Cover URL

### 2️⃣ Data Processing (Notebook)
- Removing implicit ratings
- Filtering active users
- Selecting popular books
- Creating user-book pivot table

### 3️⃣ ML Model
- User-Item Matrix
- Similarity Matrix → Cosine Similarity
- Stored as → similarity_scores.pkl

## 🛠 Tech Stack
- Python
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Pickle

## ⚙️ Installation & Setup
### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
```

### 3️⃣ Activate environment
#### Windows
```bash
venv\Scripts\activate
```
#### Mac/Linux
```bash
source venv/bin/activate
```

### 4️⃣ Install requirements
```bash
pip install -r requirements.txt
```

### 5️⃣ Run Streamlit app
```bash
streamlit run app.py
```

## 📁 Project Structure
```bash
│── app.py
│── books.pkl
│── popular.pkl
│── pt.pkl
│── similarity_scores.pkl
│── book-recommender-system.ipynb
│── requirements.txt
└── README.md
```

## 📊 Dataset
Dataset used: Book-Crossing Dataset
Available on Kaggle : https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset
