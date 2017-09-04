# Voting Demo
This is a voting demo to collect data from the web interface. This demo demonstrate the following features: 
1. A web interface to collect the button click data and send to the backend system.
2. The web server that builds on top of the flask micro-framework to receive the POST request and update the database record. 
3. The backend process to retrieve the aggregated data back to the frontend visualization.
3. A Pie Chart to display the total button click and a histogam to display the last 10 minus count distribution

## Environment Setup
I assume it is a brand new linux instance, e.g. EC2 instance with t2.micro. Let's start by updating the environment and prepare the execution platform. This demo is written in Python and we will make use of python virtual environment to run it. Therefore, we have to get Python installed before moving forward. 

First clone the demo into your linux folder, e.g. /home/ubuntu/

    git clone https://github.com/jcchoiling/voting-flask.git
    
Run the setup.sh for environment setup:

    bash setup.sh 
    
#### *If you have already executed the setup.sh, you don't have to run the following code, you can directly jump to _Getting Start_.*

### Environment Setup - Details
This section explain the action in the setup.sh

_Below code install the following components:_
* Python3 package manager (pip3) - that is to help install python package with minimal effort at maintaining the package location.
* Python virtual environment - that is to separate your project dependencies with other project.
* Python3 - the demo works well with Python 3.5 or above. In Ubuntu, it is by default has Python3.5 installed

        sudo apt-get update -y
        sudo apt install python3-pip -y
        sudo apt install python3 -y
        sudo apt-get install python-virtualenv -y

Next is to install the Python virtual environment package

    sudo pip3 install virtualenv

## Getting Started

Move the project folder. e.g. voting-flask  
    
    cd voting-flask

create an virtual environment to run the demo.

    virtualenv venv

##### *Just to remind this demo works well with python version 3.5 or above, in case you have lower version and you want to create different version of python virtual environment. You will have to use the specific python to run the script as below.*

        # virtualenv -p /usr/local/Cellar/python3/3.6.2/bin/python3.6 venv
  

enable the virtual environment

    source venv/bin/activate

Last but not least, download the project dependency library by executing:

    pip3 install -r requirements.txt

start the app

    python3 run.py

If you see the same message shown below which means that you have successfully started the voting-demo. Please open a browser and input http://127.0.0.1:5000/ to check the results.

(venv) ubuntu@ip-172-31-24-71:~/voting-flask$ python3 run.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 103-055-927    


 Next, you can access the webserver by http://<ec2-public-ip>:5000

<img src=https://i.imgur.com/pfik5S7.png>
<img src=https://i.imgur.com/qnEfmM1.png>


