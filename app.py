from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import CTransformers
from src.helper import *
from flask import Flask, render_template, jsonify, request # Import the flask


app = Flask(__name__) # initialize Flask 


#Load the PDF File
loader=DirectoryLoader('RAG-Concept-data/',
                       glob="*.pdf",
                       loader_cls=PyPDFLoader)

documents=loader.load()


#Split Text into Chunks
text_splitter=RecursiveCharacterTextSplitter(
                                             chunk_size=500,
                                             chunk_overlap=50)
text_chunks=text_splitter.split_documents(documents)


#Load the Embedding Model
embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', 
                                 model_kwargs={'device':'cpu'})


#Convert the Text Chunks into Embeddings and Create a FAISS Vector Store
vector_store=FAISS.from_documents(text_chunks, embeddings)


llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':128,
                          'temperature':0.01})


qa_prompt=PromptTemplate(template=template, input_variables=['context', 'question'])



chain = RetrievalQA.from_chain_type(llm=llm,
                                   chain_type='stuff',
                                   retriever=vector_store.as_retriever(search_kwargs={'k': 2}),
                                   return_source_documents=False,
                                   chain_type_kwargs={'prompt': qa_prompt})





@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


# # LET LUNCH THE APPLICATION NOW
@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        user_input = request.form['question'] # Take questions as input
        print(user_input)

        result=chain({'query':user_input})# Give the input to the chain, and it will give a result
        print(f"Answer:{result['result']}")

    return jsonify({"response": str(result['result']) }) # it returns the output

# INITIALIZE OUR APPLICATION

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8080,debug=True)