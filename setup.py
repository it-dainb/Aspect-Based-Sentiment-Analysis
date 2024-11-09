import pathlib
import aspect_based_sentiment_analysis as absa
from setuptools import setup
from setuptools import find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The README text
README = (HERE / "README.md").read_text()
description = 'Aspect Based Sentiment Analysis: ' \
              'Transformer & Interpretability (TensorFlow)'

setup(
    name='aspect-based-sentiment-analysis',
    version=absa.__version__,  # Semantic: MAJOR, MINOR, and PATCH
    url='https://github.com/ScalaConsultants/Aspect-Based-Sentiment-Analysis',
    description=description,
    long_description=README,
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    author=' Rafal Rolczynski',
    author_email='rafal.rolczynski@gmail.com',
    include_package_data=False,
    packages=find_packages(),
    install_requires=[
        'scikit-learn==0.24.2',
        'dataclasses==0.8',
        'tensorflow==2.5.0',
        'testfixtures==6.17.1',
        'transformers==4.8.2',
        'optuna==2.8.0',
        'spacy==3.1.1',
        'ipython==7.16.3'
    ],
    python_requires='==3.6*
)
