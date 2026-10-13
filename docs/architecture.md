# Enterprise Policy RAG — Architecture

## 1. Architecture Overview

The application uses Retrieval-Augmented Generation (RAG)
to answer questions from approved employee policy documents.

## 2. Document Ingestion

1. Load policy documents.
2. Extract text.
3. Split text into chunks.
4. Generate embeddings.
5. Store embeddings and source metadata in ChromaDB.

## 3. Question Answering

1. Receive a question through FastAPI.
2. Generate an embedding for the question.
3. Retrieve relevant chunks from ChromaDB.
4. Pass the question and retrieved context to an LLM.
5. Return a grounded answer with source references.

## 4. Planned Integrations

- MCP: Expose approved tools and external data access.
- Google ADK: Coordinate agent workflows.
- Docker: Package the application.
- Kubernetes: Practice orchestration and deployment.
- GCP: Host and monitor the application.

## 5. Engineering Considerations

- Protect credentials and sensitive data.
- Enforce document and tool access permissions.
- Handle missing evidence and retrieval failures.
- Log requests and failures without exposing sensitive data.
- Monitor response latency and model usage.