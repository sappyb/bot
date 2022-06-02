1. Create a python virtual enviroment with anaconda
conda create -n yourenvname python=3.7 anaconda
2. Activate the enviroment
conda activate yourenvname
3. Run setup
pip install -r requirements.txt -e .
or
pip install -r requirements.txt -e "path/to/chatbot"
