import logging
import re
from transformers import pipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("summerizerfunction")

try:
    logger.info("Loading model...")
    summerizer = pipeline("summerization",model="sshleifer/distilbart-cnn-12-6")
    logger.info("Summerizer loaded successfully!")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    raise RuntimeError("summerizer model loader failed.") from e

