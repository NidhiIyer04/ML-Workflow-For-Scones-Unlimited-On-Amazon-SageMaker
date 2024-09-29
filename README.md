# Project: Build an ML Workflow for Scones Unlimited on Amazon SageMaker

## Project Introduction

Image classifiers are crucial in the field of computer vision, helping to identify the content of an image. They are widely used across various industries, including advanced technologies like autonomous vehicles, augmented reality, eCommerce platforms, and diagnostic medicine.

In this project, I have learnt the skills required to be a Machine Learning Engineer (MLE) by developing an image classification model to optimize a fictional scone-delivery-focused logistics company, **Scones Unlimited**. The task was to develop an image classification model to optimize the company’s logistics operations. The model will help the team by identifying delivery vehicles (e.g., bicycles and motorcycles) from images. This will allow Scones Unlimited to assign nearby deliveries to bicycle couriers and route farther deliveries to motorcyclists, improving the company’s efficiency.

The goal as an MLE is to ship a **scalable** and **safe** image classification model. Once the model is deployed, it should scale to meet demands and have safeguards to monitor and control for drift or degraded performance.

I have used **AWS SageMaker** to build, train, and deploy an image classification model capable of distinguishing between bicycles and motorcycles. Additionally, I've used **AWS Lambda** functions and **AWS Step Functions** to create supporting services and orchestrate the workflow. I have achieved a validation accuracy of 0.833333 and a train accuracy of 0.976815.

---

## Project Steps Overview

### Step 1: Data Staging
- Set up and prepared the dataset for model training.

### Step 2: Model Training and Deployment
- Trained the image classification model using SageMaker.
- Deployed the trained model and created an API endpoint for inference.

### Step 3: Lambdas and Step Function Workflow
- Authored three Lambda functions to:
  1. Process the image.
  2. Perform image classification.
  3. Filter low-confidence inferences.
- Used Step Functions to orchestrate the Lambda functions into a workflow.

### Step 4: Testing and Evaluation
- Tested the deployed model and evaluated its performance.

---

## Criteria for Success

### Trained and Deployed a Machine Learning Model

#### Setup SageMaker Studio Workspace
- Successfully set up a SageMaker Studio workspace and a kernel to run the project.

#### Loaded and Prepared Data
- Completed the **ETL (Extract, Transform, Load)** section of the starter code and prepare the dataset for training.

#### Train an ML Model
- Successfully trained an image classification model in SageMaker.
- Reached the "Getting Ready to Deploy" section, showing that the model has been trained.

#### Deployed the Model and Created an API Endpoint
- Successfully deployed the trained model in SageMaker.
- Printed the unique model endpoint name in the notebook for future use.
- Successfully made predictions using a sample image through the model’s API endpoint.

### Built a Full Machine Learning Workflow

#### Authored Three Lambda Functions
- **1st Lambda Function**: Returns an object to Step Function as `image_data` in an event.
- **2nd Lambda Function**: Performs image classification.
- **3rd Lambda Function**: Filters low-confidence inferences.
- Saved the code for each Lambda function in a Python script.

#### Composed Lambdas in a Step Function
- Composed the three Lambda functions into a workflow using AWS Step Functions.
- Exported the Step Function definition as JSON.
- Included a screenshot showing the working Step Function.

### Monitored the Model for Errors

#### Extracted Monitoring Data
- Loaded model monitoring data from Amazon S3 into your notebook.

#### Visualized Monitoring Data
- Created a custom visualization for the Model Monitor data outputs.


