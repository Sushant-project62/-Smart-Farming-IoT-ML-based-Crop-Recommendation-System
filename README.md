# 🌱 Smart Farming – IoT & ML-based Crop Recommendation System

A data-driven smart farming system that integrates **IoT sensors** with **machine learning** to recommend the most suitable crop for cultivation. The system enables farmers to make informed crop selection decisions based on **real-time soil and weather data**, reducing guesswork and improving yield.

## 📌 Project Overview

Traditional farming often relies on intuition and experience, leading to inefficiencies. This project bridges the gap by combining **IoT devices, cloud storage, and machine learning** to deliver real-time, accurate recommendations for sustainable agriculture.

## ⚙️ Tools & Technologies

* **IoT Sensors:** DHT11 (Temperature & Humidity), Soil Moisture Sensor
* **Cloud:** Google Sheets (via Google Forms) for data storage and visualization
* **Machine Learning:** Random Forest Classifier (Crop Recommendation Dataset)
* **Dashboard:** Blynk IoT Cloud for real-time monitoring
* **Programming:** Python (Pandas, NumPy, Scikit-learn)
* **Hardware:** Arduino / NodeMCU ESP8266

## 🧠 Workflow

1. **IoT Data Collection**

   * Temperature, humidity, soil moisture collected from sensors
   * Approximate NPK & pH values generated from ranges (due to sensor unavailability)

2. **Cloud Integration**

   * Sensor data stored in **Google Sheets** via Google Forms
   * Data visualized for monitoring trends

3. **Machine Learning Model**

   * Trained a **Random Forest Classifier** on Crop Recommendation Dataset
   * Input: soil nutrients + environmental parameters
   * Output: Recommended crop

4. **Real-time Dashboard**

   * Predictions sent to **Blynk Cloud**
   * Farmers can access results on mobile for decision-making

## 💻 How to Run the Project

1. Clone repository:

   ```bash
   git clone https://github.com/<your-username>/smart-farming.git
   cd smart-farming
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run ML model:

   ```bash
   python crop_recommendation.py
   ```

4. View live data on **Google Sheets** or **Blynk App**

## 🌐 Features

* IoT-based real-time environmental monitoring
* Cloud storage for easy visualization
* ML-based accurate crop recommendation
* Mobile-friendly dashboard for farmers

## 📊 Sample Output

* Input: Temperature = 27°C, Humidity = 65%, Soil Moisture = 45%
* Predicted Crop: **Rice**

## 🚀 Future Enhancements

* Integration of actual **NPK & pH sensors**
* Use of **weather forecasting APIs** for climate-aware recommendations
* **Mobile advisory system** powered by AI/ML
* Expansion to multiple languages for farmer accessibility

## 📜 Conclusion

This project shows how **IoT + AI can transform agriculture** by providing a low-cost, scalable, and smart solution. With further refinements, it can make farming **data-driven, efficient, and sustainable**.

---

👨‍💻 **Author:** Sushant Kishan Rathod
📧 Contact: [sushantrathod6288@gmail.com]
🔗 GitHub: [https://github.com/Sushant-project62]
