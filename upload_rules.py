from openai import OpenAI

client = OpenAI(api_key="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")


VECTOR_STORE_ID = "vs_697dca4c483c8191b3469c2539a40761"  

file = client.files.create(
    file=open("rules.dataset.json", "rb"),
    purpose="assistants"
)

client.vector_stores.files.create(
    vector_store_id=VECTOR_STORE_ID,
    file_id=file.id
)

print("Upload complete")
