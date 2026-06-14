from opensearchpy import OpenSearch
from app.core.config import settings

opensearch_client = OpenSearch(
    hosts=[
        {
            "host": settings.OPENSEARCH_HOST,
            "port": settings.OPENSEARCH_PORT,
            "scheme": "https" if settings.OPENSEARCH_USE_SSL else "http",
        }
    ],
    use_ssl=settings.OPENSEARCH_USE_SSL,
    verify_certs=settings.OPENSEARCH_VERIFY_CERTS,
    timeout=5,
)
