from pydantic import BaseModel

from .base_trial import BaseTrial


class QuestionAnsweringTrial(BaseModel, BaseTrial):
    
