from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated

model = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
)


class Review(TypedDict):
    summary : Annotated[str, 'summary of the review product']
    sentiment : str

structured_model = model.with_structured_output(Review)

review_prompt = "Write a review of a high-performance gaming laptop, highlighting its features, performance, and value for money."


structured_model.invoke()
# llm = ChatOpenAI(
#     model="gpt-4o",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     # api_key="...",
#     # base_url="...",
#     # organization="...",
#     # other params...
# )
