Dataset to place at ./data : https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data

Project about predicting airbnb price through caracteristics of airbnb.

Used prefect, mlflow, ci/cd, etc..

import your aws profile and change it in worflow/mgmt/runner.py, line 27
also change the password in backend_uri : mlflowmlflow, as defined in docker-compose.yaml

in api, change run_id by the one created when you launch the script 

In config.json, remove local and cloud prefix dict choose which you want and keep these values in "mlflow" 

to run app : docker-compose, and compile dockerfile or use makefile with run-all (if you are in windows, for unix change the commands)
