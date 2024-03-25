# Llama2-on-CPU-Machine
# How to run from github
### step 1;
create a repository from github, create a folder on your desktop, highlight and select terminal. clone the repository on the terminal, cd into the folder created after cloning the repository.

'''bash
git clone https://github.com/
'''

### step 2;
Create a Virtual Environment

'''bash
conda create - n environment_name python=3.8 -y
'''
i.e : conda create -n cpullama python=3.8 -y   # the cpu is the environment name I gave. You can choose a different environment name

'''bash
conda activate environment_name
'''
i.e : conda activate cpullama


'''bash
pip install -r requirements.txt
'''

'''bash
python app.py
'''

### Download the quantize model from the link provided in model folder & keep the model in the model directory
''' ini
## Download the Llama 2 Model
llama-2-7b-chat-ggmlv3.q4_0.bin

## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

