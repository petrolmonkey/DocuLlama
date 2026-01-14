## Summary
A chatbot that answers questions about a set of PDF documents using the OpenAI LLM and LlamaIndex framework. It searches a set of instruction manuals and gives responses relevant to the tools and appliances I have.

## Workflow
1. **Document Ingestion**: PDFs are loaded and split into text chunks using LlamaIndex
2. **Vector Embeddings**: Each chunk is converted to a vector embedding for semantic search
3. **Vector Database**: Embeddings stored in an index for fast similarity search
4. **Query Flow**: User question → vector search → retrieve relevant chunks → LLM generates answer using document context

## Tech Stack
- **LlamaIndex**: Document processing, vector search, retrieval
- **Streamlit**: Chatbot UI
- **OpenAI GPT**: Response generation  
- **Python 3.13.9**

## Quick Start
1. Clone Repo `git clone https://github.com/petrolmonkey/DocuLlama.git`
2. Goto `cd docullama/v3-docullama/scripts`
3. Run `streamlit run v3-docullama.py`
   
<img width="430" height="520" alt="Screenshot 2025-12-16 at 10 31 24 AM" src="https://github.com/user-attachments/assets/841c5cdc-00b1-4472-90de-cea574930a85" />
