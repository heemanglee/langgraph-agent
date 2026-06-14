from datetime import datetime

from opensearchpy import OpenSearch


class DocumentRepository:
    def __init__(self, opensearch_client: OpenSearch):
        self.os_client = opensearch_client

    def get_documents(self, question: str) -> list[dict]:
        body = {
            "query": {
                "match": {
                    "question": question,
                }
            },
            "_source": [
                "question",
                "llm_answer",
            ],
        }

        response = self.os_client.search(
            index="langgraph-agent",
            body=body,
        )

        return [hit["_source"] for hit in response["hits"]["hits"]]

    def create_document(self, question: str, llm_answer: str, created_at: datetime):
        body = {
            "question": question,
            "llm_answer": llm_answer,
            "created_at": created_at,
        }

        response = self.os_client.index(
            index="langgraph-agent",
            body=body,
            refresh=True,
        )

        return response["_id"]
