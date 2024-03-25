from langchain import PromptTemplate
from langchain import LLMChain # chains
from langchain.llms import CTransformers # for the quantization
from src.helper import *

B_INST, E_INST = "[INST]", "[/INST]"  # B--Biginning, E--Ending, INT -- Instruction, SYS -- System
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

# English to French translation
instruction = "Convert the following text from English to Hindi: \n\n {text}"
# instruction = "Give the proper summary of the : \n\n {text}"


SYSTEM_PROMPT = B_SYS + CUSTOM_SYSTEM_PROMPT + E_SYS
template1 = B_INST + SYSTEM_PROMPT + instruction + E_INST


prompt1 = PromptTemplate(template=template1, input_variables=["text"])

# Import the LLM
llm = CTransformers(model='model/llama-2-7b-chat.ggmlv3.q4_0.bin',
                    model_type='llama',
                    config={'max_new_tokens': 128,
                            'temperature': 0.01} # template parameter is the creativity of the model
                   )

# LLM CHAIN
LLM_Chain=LLMChain(prompt=prompt1, llm=llm)

print(LLM_Chain.run("How are you?"))







# For TEXT SUMMARIZATION

# B_INST, E_INST = "[INST]", "[/INST]"  # B--Biginning, E--Ending, INT -- Instruction, SYS -- System
# B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

# # English to French translation
# # instruction = "Give the proper summary of the : \n\n {text}"


# SYSTEM_PROMPT = B_SYS + CUSTOM_SYSTEM_PROMPT + E_SYS
# template1 = B_INST + SYSTEM_PROMPT + instruction + E_INST


# prompt1 = PromptTemplate(template=template1, input_variables=["text"])

# # Import the LLM
# llm = CTransformers(model='model/llama-2-7b-chat.ggmlv3.q4_0.bin',
#                     model_type='llama',
#                     config={'max_new_tokens': 128,
#                             'temperature': 0.01} # template parameter is the creativity of the model
#                    )

# # LLM CHAIN
# LLM_Chain=LLMChain(prompt=prompt1, llm=llm)

# #print(LLM_Chain.run("Harry Porter"))