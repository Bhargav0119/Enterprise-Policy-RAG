from document_processor import DocumentProcessor

processor = DocumentProcessor("data/sample_policies/leave_policy.txt")

content = processor.load_document()

chunks = processor.chunk_document(content)

print("Total Chunks:", len(chunks))

for chunk in chunks:
    print("__________________________________")
    print(chunk)
    
print("Type of chunks:", type(chunks))
print("Type of first chunk:", type(chunks[0]))