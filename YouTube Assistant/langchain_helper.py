from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI

from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

# video_url = "lG7Uxts9SXs"

def create_vector_db_from_youtube_url(video_url: str) -> FAISS:
    loader = YoutubeLoader(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)

    return db


def response_from_query(db, query, k=4):

    docs = db.similarity_search(query, k)

    docs_page_content =  " ".join([d.page_content for d in docs])

    llm = OpenAI(model = "text-davinci-003" )

    prompt = PromptTemplate(
        input_variables = ["questions", "docs"],
        template = """You are a helpful assistant that that can answer questions about youtube videos 
        based on the video's transcript.
        
        Answer the following question: {questions}
        By searching the following video transcript: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be verbose and detailed.
        """, )

    chain = LLMChain(llm=llm, prompt= prompt)
    response = chain.run(questions = query, docs=docs_page_content)

    response = response.replace("\n","")
    return response, docs
# print(create_vector_db_from_youtube_url(video_url))
