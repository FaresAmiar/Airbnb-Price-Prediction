<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>Airbnb-Price-Prediction
</h1>
<h3>◦ Unlock Authentic Pricing</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style&logo=pre-commit&logoColor=black" alt="precommit" />
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/Terraform-7B42BC.svg?style&logo=Terraform&logoColor=white" alt="Terraform" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />

<img src="https://img.shields.io/badge/pandas-150458.svg?style&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style&logo=Pytest&logoColor=white" alt="Pytest" />
<img src="https://img.shields.io/badge/MLflow-0194E2.svg?style&logo=MLflow&logoColor=white" alt="MLflow" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/languages/top/FaresAmiar/Airbnb-Price-Prediction?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/FaresAmiar/Airbnb-Price-Prediction?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/FaresAmiar/Airbnb-Price-Prediction?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/FaresAmiar/Airbnb-Price-Prediction?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project is focused on deploying an MLOps architecture, using mainly MlFlow for ML and models management. Cloud architecture used is AWS (EC2, RDS, Lambda), with Terraform as IAC.

---

## ⚙️ Features

| Feature                | Description                                                                                                                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **⚙️ Architecture**     | The system follows a modular architecture, organizing the codebase into separate files for different functionalities such as infrastructure setup, data and workflow management, model wrapper, API, and monitoring. |
| **🔗 Dependencies**    | The project relies on external libraries such as MLflow, Prefect, Flask, pandas, scikit-learn, and evidently for various functionalities including workflow management, API development, and monitoring.                                                                                       |
| **🔌 Integrations**    | The system integrates well with external tools and services such as MLflow, Prefect, Docker, AWS (EC2, S3, RDS), and Terraform for infrastructure provisioning and management.                                |


---



## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                              |
| ---                                                                                                  | ---                                                                                                                                                                                                                  |
| [Dockerfile](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/Dockerfile)             | This code sets up a Python environment, installs the required dependencies listed in requirements.txt, copies project files and data into a working directory, and runs the runner.py script for managing workflows. |
| [Makefile](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/Makefile)                 | This Makefile provides commands for starting MLflow, Prefect Server, and Prefect Agent, as well as running a Python script. It also includes a help message and an additional target for other actions.              |
| [start_mlflow.bat](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/start_mlflow.bat) | This command starts an MLflow server with specified host, port, backend store, and default artifact root configurations.                                                                                             |
| [killakill.bat](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/killakill.bat)       | This script kills processes using ports 5000 and 4200 using the taskkill command in Windows cmd. It then notifies the user and waits for their confirmation before exiting. It is very convenient for cleaning Prefect and MlFlow services to run new instances                                            |

</details>



<details closed><summary>Infrastructure</summary>

| File                                                                                                                                | Summary                                                                                                                                                                                                                                                 |
| ---                                                                                                                                 | ---                                                                                                                                                                                                                                                     |

| [main.tf](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/infrastructure/main.tf)                                   | The code sets up AWS resources for MLOps. It provisions an S3 bucket for datasets, another S3 bucket for MLflow artifacts, an RDS instance for PostgreSQL, and an EC2 instance to execute code. Outputs provide the EC2 IP and RDS endpoint.            |


</details>

<details closed><summary>Workflow_mgmt</summary>

| File                                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                         |
| [ModelWrapper.py](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/workflow_mgmt/ModelWrapper.py)                 | This code defines a ModelWrapper class that extends the mlflow.pyfunc.PythonModel class. It wraps a given model and implements a predict method, which uses the wrapped model to make predictions on the input data.                                                                                                                                                                        |
| [runner.py](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/workflow_mgmt/runner.py)                             | This code defines a pipeline for training and evaluating a machine learning model on the Airbnb dataset. It loads the dataset, preprocesses it, splits it into training and testing sets, transforms it, trains the model, evaluates its performance, and logs the results using MLflow. It also includes functionality for monitoring metrics and potentially triggering model retraining. |
| [model_ops.py](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/workflow_mgmt/model_ops.py)                       | The code includes two functions: 1. "train_model" to train a machine learning model using specified hyperparameters and log the parameters with MLflow.2. "evaluate_model" to evaluate the trained model's performance using a specified metric function and log the result with MLflow.                                                                                                    |
| [data_ops.py](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/workflow_mgmt/data_ops.py)                         | The code consists of functions to load a dataset, preprocess it by filling missing values and filtering out certain values, split the dataset into training and test sets, transform the dataset by encoding categorical variables, and extract features and target variables. It utilizes pandas, scikit-learn, and DictVectorizer.                                                        |
| [evidently_monitoring.py](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/workflow_mgmt/evidently_monitoring.py) | This code includes functions for loading data and models, as well as calculating and generating reports on data drift using the package evidently. It also has a commented-out main function for running the metrics calculation. The code aims to provide analysis and insights on how the model's predictions might change over time.                                                     |

</details>

<details closed><summary>Api</summary>

| File                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                  |
| [api.py](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/api/api.py) | This code sets up a Flask API that uses a pre-trained machine learning model to predict outcomes based on input data. It loads the model and data vectorizer, accepts POST requests with JSON data, transforms the data using the vectorizer, runs it through the model, and returns the predictions as JSON. The API can be accessed at'0.0.0.0:5000/predict' when the code is run. |

</details>

<details closed><summary>Model_insight</summary>

| File                                                                                                                   | Summary                                                                                                                                                                            |
| ---                                                                                                                    | ---                                                                                                                                                                                |
| [EvidentlyReport.py](https://github.com/FaresAmiar/Airbnb-Price-Prediction/blob/main/model_insight/EvidentlyReport.py) | Generates a report using the Evidently library, comparing drift between train and test data for numerical and categorical features. The report is saved as an HTML file. |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites


1. Create an account in AWS

2. Install [AWS CLI](https://docs.aws.amazon.com/fr_fr/cli/v1/userguide/install-windows.html)

3. Import your profile via aws configure (after creating a key)

```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
```

4. Define your profile in OS

```
$ export AWS_PROFILE=user1
```

or in windows :

```
setx AWS_PROFILE=user1
```

5. Install jq

- Windows :
```
choco install jq
```

- macOs :
```
brew install jq
```

6. Install make if it is not on your machine


### 📦 Installation

1. Clone the Airbnb-Price-Prediction repository:
```sh
git clone https://github.com/FaresAmiar/Airbnb-Price-Prediction
```

2. Change to the project directory:
```sh
cd Airbnb-Price-Prediction
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

4. Create ressources on AWS :

```
terraform init
terraform plan
terraform apply --auto-approve
```

For removing resources:
```
terraform destroy --auto-approve
```

### 🎮 Using Airbnb-Price-Prediction

1. Using docker-compose and makefile:
```sh
docker-compose up -d
make run-all
```

---


## 👏 Acknowledgments

Big shout out to [Datatalks Club](https://datatalks.club/) for all their work and help through their courses

Especially [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) which allowed me to build this project




---
