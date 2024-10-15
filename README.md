
# Data Warehouse for Ethiopian Medical Business Data

This repository contains the code and resources for building a **data warehouse** to store, clean, and process data scraped from **Ethiopian medical businesses**' Telegram channels. The project also includes object detection using the **YOLOv5 (You Only Look Once)** model for analyzing images from the channels.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Data Scraping](#data-scraping)
- [Data Cleaning & Transformation](#data-cleaning--transformation)
- [Object Detection Using YOLO](#object-detection-using-yolo)
- [Database Integration](#database-integration)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Introduction
This project aims to create a **centralized data warehouse** to store and analyze data on Ethiopian medical businesses, including text-based business information and image-based insights using object detection. Data is scraped from public Telegram channels and transformed into a format suitable for further analysis and reporting. The object detection component identifies key elements in images using the YOLOv5 model, and the results are integrated into the data warehouse for enhanced analysis.

## Project Structure

\`\`\`bash
├── data
│   ├── photos                   # Raw images from Telegram scraping
│   └── telegram_data.csv         # Raw scraped data from Telegram channels
├── dbt                          # DBT models for data transformation
├── notebooks                    # Jupyter notebooks for data exploration and transformation
├── yolov5                       # YOLOv5 model for object detection
├── scripts                      # Python scripts for data processing and database integration
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation (this file)
└── LICENSE                      # License information
\`\`\`

## Installation

### Clone the Repository
\`\`\`bash
git clone https://github.com/yourusername/Data-Warehouse-for-Ethiopian-Medical-Business-Data.git
cd Data-Warehouse-for-Ethiopian-Medical-Business-Data
\`\`\`

### Set Up Virtual Environment
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Linux/MacOS
venv\Scriptsctivate  # On Windows
\`\`\`

### Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### YOLOv5 Setup
For object detection, the YOLOv5 model is used.
\`\`\`bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
\`\`\`

## Data Scraping

The project scrapes data from specific Ethiopian medical Telegram channels. The scraping process involves collecting:
- Business names
- Channel descriptions
- Media content (images)
  
The data is initially stored in a CSV file (\`telegram_data.csv\`) located in the \`data\` folder.

You can run the scraping script using:
\`\`\`bash
python scripts/scrape_telegram.py
\`\`\`

## Data Cleaning & Transformation

The raw scraped data contains duplicates, missing values, and inconsistent formats. We use **Pandas** for data cleaning and **DBT (Data Build Tool)** for transformations.

To clean and transform the data:
1. Run the cleaning script:
   \`\`\`bash
   python scripts/data_cleaning.py
   \`\`\`
2. Set up DBT:
   \`\`\`bash
   cd dbt
   dbt init medical_project
   \`\`\`
3. Run DBT models for data transformations:
   \`\`\`bash
   dbt run
   \`\`\`

## Object Detection Using YOLO

We use the YOLOv5 pre-trained model to perform object detection on the collected images. The results include bounding boxes, labels, and confidence scores.

To run object detection:
\`\`\`bash
cd yolov5
python detect.py --source "../data/photos" --weights yolov5s.pt --conf 0.4 --save-txt --save-conf
\`\`\`

The detection results will be saved in the \`runs/detect/exp/labels\` folder.

## Database Integration

All cleaned and transformed data, including the YOLO detection results, is stored in a **PostgreSQL** database. To store data in the database:
1. Define the database schema:
   \`\`\`sql
   CREATE TABLE object_detection_results (
       detection_id SERIAL PRIMARY KEY,
       image_name VARCHAR(255),
       label VARCHAR(100),
       x_center FLOAT,
       y_center FLOAT,
       width FLOAT,
       height FLOAT,
       confidence FLOAT
   );
   \`\`\`
2. Use the script to insert detection results into the database:
   \`\`\`bash
   python scripts/store_yolo_results.py
   \`\`\`

## Usage

### Running the End-to-End Pipeline
To run the entire data pipeline (scraping, cleaning, transformation, object detection, and database integration), follow these steps:

1. Scrape data from Telegram:
   \`\`\`bash
   python scripts/scrape_telegram.py
   \`\`\`
2. Clean and transform the data:
   \`\`\`bash
   python scripts/data_cleaning.py
   dbt run
   \`\`\`
3. Run YOLOv5 object detection:
   \`\`\`bash
   python yolov5/detect.py --source "../data/photos" --weights yolov5s.pt --conf 0.4
   \`\`\`
4. Store the detection results in the PostgreSQL database:
   \`\`\`bash
   python scripts/store_yolo_results.py
   \`\`\`

## Results
- **Scraped Data**: Collected data from public Ethiopian medical Telegram channels.
- **Object Detection**: YOLO detected objects such as people, ties, and other relevant elements in images.
- **Data Warehouse**: The transformed and enriched data is stored in PostgreSQL for querying and analysis.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
