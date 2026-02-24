from openai import OpenAI

client = OpenAI(api_key="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")

## create database  
vector_store = client.vector_stores.create(
    name="soc-ids-rules"
)

print("Vector Store ID:", vector_store.id)



