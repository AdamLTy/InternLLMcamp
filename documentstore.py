from haystack.document_stores.in_memory import InMemoryDocumentStore
from doc_embedder import doc_embedder
from load_data import docs
document_store = InMemoryDocumentStore()

docs_with_embeddings = doc_embedder.run(docs)
document_store.write_documents(docs_with_embeddings["documents"])
