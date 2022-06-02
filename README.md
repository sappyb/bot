##1. Create a python virtual environment with anaconda
```shell
conda create -n yourenvname python=3.7 anaconda
```

##2. Activate the environment
```shell
conda activate yourenvname
```
##3. Run setup
```shell
pip install -r requirements.txt -e .
```
or
```shell
pip install -r requirements.txt -e "path/to/chatbot"
```
