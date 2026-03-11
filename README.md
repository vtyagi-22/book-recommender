# 📚 Book Recommendation System

##  Overview

As a book reader, I often faced difficulty deciding what to read next. Many platforms provide generic recommendations instead of suggesting books based on actual similarity.

To solve this problem, I built a **Book Recommendation System** that recommends books similar to a selected book on basis of genre and description using **machine learning techniques**.

The system converts books into **numerical vectors** and uses **K-Nearest Neighbors (KNN)** with **Cosine Similarity** to find the most similar books.

---

##  Features

* Select a book from a dropdown list
* Get **top 5 similar book recommendations**
* Displays **book cover images**
* Fast recommendations using **vector similarity**
* Interactive **Streamlit web interface**

---

##  Machine Learning Approach

### 1️ Data Processing

The dataset contains information about books such as title, author, and ratings. The data is cleaned and prepared using **Pandas**.

### 2️ Vectorization

Books are converted into **vector representations** so that machine learning algorithms can compare them mathematically.

### 3️ Cosine Similarity

Cosine similarity measures the similarity between two book vectors. Books with smaller angles between their vectors are considered more similar.

### 4️ K-Nearest Neighbors (KNN)

The **KNN algorithm** is used to find the most similar books to the selected book based on their vector representations.

---

##  Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**

---

##  Project Structure

```
Book_rec/
│
├── app.py
├── main.py
├── book.pkl
|── bk.pkl
├── vectors.pkl
├── model.pkl

```

---

##  Dataset

The kaggle dataset used for this project contains book information used to generate recommendations.

Dataset s: **GoodReads 100k books**
Dataset Link: https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k

---

##  Running the Project

Clone the repository

```
git clone https://github.com/vtyagi-22/book-recommender.git
```

Navigate to the project folder

```
cd book-recommendation-system
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
streamlit run app.py
```

---

##  Future Improvements

* Add **user-based collaborative filtering**
* Improve recommendation accuracy
* Deploy the application online
* Add search functionality by genre

---

##  Author

Vaishnavi Tyagi
