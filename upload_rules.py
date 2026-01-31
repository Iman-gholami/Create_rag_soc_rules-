from openai import OpenAI

client = OpenAI(api_key="")


VECTOR_STORE_ID = "vs_697dca4c483c8191b3469c2539a40761"  

file = client.files.create(
    file=open("filename", "rb"),
    purpose="assistants"
)

client.vector_stores.files.create(
    vector_store_id=VECTOR_STORE_ID,
    file_id=file.id
)

print("Upload complete")
