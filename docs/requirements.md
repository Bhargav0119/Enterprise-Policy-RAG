# Enterprise Policy RAG Assistant

## 1. Project Objective

Build an enterprise-grade AI application that answers employee
policy questions using Retrieval-Augmented Generation (RAG).

## 2. Functional Requirements

FR-01: Load employee policy documents.

FR-02: Extract and split document text into chunks.

FR-03: Generate embeddings and store them in a vector database.

FR-04: Retrieve relevant chunks based on a user question.

FR-05: Generate an LLM response using retrieved context.

FR-06: Return source references with the answer.

FR-07: Handle questions that cannot be answered from available documents.

FR-08: Expose the application through FastAPI.

FR-09: Integrate external tools through MCP.

FR-10: Support AI agent workflows using Google ADK.

## 3. Non-Functional Requirements

NFR-01: Secure configuration using environment variables.

NFR-02: Maintainable and modular Python code.

NFR-03: Automated unit and integration testing.

NFR-04: Containerization using Docker.

NFR-05: Kubernetes deployment support.

NFR-06: Deployment to Google Cloud Platform.

NFR-07: Application logging and monitoring.

NFR-08: Secure access to documents and external tools.

## 4. Initial Technology Stack

- Python 3.12
- FastAPI
- ChromaDB
- Ollama / Vertex AI
- MCP Python SDK
- Google ADK
- Docker
- Kubernetes
- GitHub Actions
- Google Cloud Platform

## 5. MVP Scope

The first version will:

1. Load a sample employee policy document.
2. Split the document into chunks.
3. Store and retrieve relevant chunks.
4. Generate a grounded answer using an LLM.
5. Return the answer with source references.