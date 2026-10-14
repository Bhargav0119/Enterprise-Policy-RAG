class DocumentProcessor:
    
    def __init__(self, document_path):
        self.document_path = document_path
        
    def load_document(self):
        with open (self.document_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content

    def chunk_document(self, content):
        chunks = content.split("\n\n")
        return chunks
