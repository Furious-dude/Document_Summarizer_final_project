import logging
import re
from transformers import pipeline
from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
#llm = AutoModelForCausalLM.from_pretrained("TheBloke/TinyLlama-1.1B-1T-OpenOrca-GGUF", model_file="tinyllama-1.1b-1t-openorca.Q4_K_M.gguf", model_type="llama", gpu_layers=50)
llm = AutoModelForCausalLM.from_pretrained("*/tinyllama-1.1b-1t-openorca.Q4_K_M.gguf")
print(llm("AI is going to"))
# testing for what is actually good with the model/ em tim hieu model hoat dong nhu nao

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("summerizerfunction")

try:
    logger.info("Loading model...")
    summerizer = pipeline("summerization",model="sshleifer/distilbart-cnn-12-6")
    logger.info("Summerizer loaded successfully!")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    raise RuntimeError("summerizer model loader failed.") from e

