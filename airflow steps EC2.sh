#Steps for installing and running Airflow 2.8.4 on Ubuntu EC2 using Python 3.10
#including virtual envronment and aws connectors, perators
sudo apt-get update
sudo apt install python3-pip
sudo apt install python3.10-venv
python3 -m venv aws-endtoend_venv
source aws-endtoend_venv/bin/activate

PATH=$PATH:~/.local/bin

sudo apt install s3fs
pip install "apache-airflow==2.8.4" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.4/constraints-no-providers-3.10.txt"
pip install apache-airflow-providers-amazon

airflow db init
airflow users create --username admin --password admin --firstname John --lastname Doe --role Admin --email admin@domain.com
airflow webserver -D
airflow scheduler -D

#View airflow PIDs so we can kill them if needed
lsof -t tcp:8080
