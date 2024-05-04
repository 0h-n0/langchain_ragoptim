from typing import Any

from pydantic import BaseModel

from .base_rag import BaseRAG
from .rag_modules.generation.base_generation import BaseGenerationModule
from .rag_modules.indexing.base_indexing import BaseIndexingModule
from .rag_modules.orchestration.base_orchestration import (
    BaseOrchestrationModule
)
from .rag_modules.post_retrieval.base_post_retrieval import (
    BasePostRetrievalModule
)
from .rag_modules.pre_retrieval.base_pre_retrieval import (
    BasePreRetrievalModule
)
from .rag_modules.retrieval.base_retrieval import BaseRetrievalModule


class ModularRAG(BaseModel, BaseRAG):
    llm: Any
    embedding_model: Any
    generation_module: BaseGenerationModule
    indexing_module: BaseIndexingModule
    retrieval_module: BaseRetrievalModule
    post_retrieval_module: BasePostRetrievalModule
    pre_retrieval_module: BasePreRetrievalModule
    orchestration_module: BaseOrchestrationModule

    
