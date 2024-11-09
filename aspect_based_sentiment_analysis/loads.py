import os
import logging
from typing import Callable
from typing import List

import transformers

from . import utils
from .data_types import LabeledExample
from .models import BertABSCConfig
from .models import BertABSClassifier
from .pipelines import Pipeline
from .professors import Professor
from .aux_models import ReferenceRecognizer
from .aux_models import PatternRecognizer

logger = logging.getLogger('absa.load')
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DOWNLOADS_DIR = os.path.join(ROOT_DIR, 'downloads')


def load(
        name: str = 'absa/classifier-rest-0.2',
        text_splitter: Callable[[str], List[str]] = None,
        reference_recognizer: ReferenceRecognizer = None,
        pattern_recognizer: PatternRecognizer = None,
        **model_kwargs
) -> Pipeline:
    """ Load ready to use pipelines. Files are stored on
    the HaggingFace AWS S3. """
    try:
        config = BertABSCConfig.from_pretrained(name, **model_kwargs)
        model = BertABSClassifier.from_pretrained(name, config=config)
        tokenizer = transformers.BertTokenizer.from_pretrained(name)
        professor = Professor(reference_recognizer, pattern_recognizer)
        nlp = Pipeline(model, tokenizer, professor, text_splitter)
        return nlp

    except EnvironmentError as error:
        text = 'Model or Tokenizer not found. Please check a documentation.'
        logger.error(text)
        raise error
