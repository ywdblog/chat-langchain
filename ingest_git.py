import pickle

from langchain.document_loaders import ReadTheDocsLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from git import Repo
import sys 
 
 
## Git Loader
# repo = Repo.clone_from(
#     "https://github.com/openai/openai-cookbook", to_path="./example_data/openai-cookbook"
# )
# branch = repo.head.reference
from langchain.document_loaders import GitLoader
#loader = GitLoader(repo_path="./openai-cookbook/", branch="main")
loader = GitLoader(repo_path="./openai-cookbook/", file_filter=lambda file_path: file_path.endswith((".md" )))
#loader = GitLoader(repo_path="./openai-cookbook/", file_filter=lambda file_path: file_path.endswith((".md","ipynb")))
raw_documents = loader.load()

# https://python.langchain.com/en/latest/modules/indexes/text_splitters/examples/character_text_splitter.html
text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

documents = text_splitter.split_documents(raw_documents )
print(len(documents))


embeddings = OpenAIEmbeddings(openai_api_key="",openai_api_version='2020-11-07')
# query_result = embeddings.embed_query(text) 
vectorstore = FAISS.from_documents(documents, embeddings)
 
with open("vectorstore.pkl", "wb") as f:
    pickle.dump(vectorstore, f)
