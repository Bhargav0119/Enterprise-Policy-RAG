from app.document_processor import DocumentProcessor

def test_chunk_documnet():

    processor = DocumentProcessor("sample.txt")

    content = "Annual Leave\n\nSick Leave\n\nMaternity Leave"

    chunks = processor.chunk_document(content)

    assert len(chunks) == 3

def test_load_documnet():

    processor = DocumentProcessor("data/sample_policies/leave_policy.txt")

    content = processor.load_document()

    assert "20 days of annual leave" in content
