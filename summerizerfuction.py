# import logging
# import re
# from transformers import pipeline
# from ctransformers import AutoModelForCausalLM

# # Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
# #llm = AutoModelForCausalLM.from_pretrained("TheBloke/TinyLlama-1.1B-1T-OpenOrca-GGUF", model_file="tinyllama-1.1b-1t-openorca.Q4_K_M.gguf", model_type="llama", gpu_layers=50)
# llm = AutoModelForCausalLM.from_pretrained("*/tinyllama-1.1b-1t-openorca.Q4_K_M.gguf")
# print(llm("AI is going to"))
# # testing for what is actually good with the model/ em tim hieu model hoat dong nhu nao

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger("summerizerfunction")

# try:
#     logger.info("Loading model...")
#     summerizer = pipeline("summerization",model="sshleifer/distilbart-cnn-12-6")
#     logger.info("Summerizer loaded successfully!")
# except Exception as e:
#     logger.error(f"Failed to load model: {e}")
#     raise RuntimeError("summerizer model loader failed.") from e

# from transformers import CTransformers
# import ctransformers
# from ctransformers import ctransformers
from ctransformers import AutoModelForCausalLM

def load_llm():
    # # New model details
    # MODEL_BIN_PATH = r'tinyllama_model\tinyllama-1.1b-1t-openorca.Q2_K.gguf'
    # MODEL_TYPE = 'llama'
    # MAX_NEW_TOKENS = 3000
    # TEMPERATURE = 0.01
    # context_length = 3000
    # llm = CTransformers(model=MODEL_BIN_PATH,
    #                     model_type=MODEL_TYPE,
    #                     config={'max_new_tokens': MAX_NEW_TOKENS,
    #                             'temperature': TEMPERATURE,
    #                             'context_length': context_length}
    #                     )
    llm = AutoModelForCausalLM.from_pretrained("tinyllama_model/tinyllama-1.1b-1t-openorca.Q2_K.gguf", model_type="llama",local_files_only=True)
    print(llm("AI is going to"))
    return llm



# Call load_llm() to create an instance of the model
llm_model = load_llm()

# Test if the model was loaded successfully
if llm_model is not None:
    print("Model loaded successfully.")
else:
    print("Failed to load the model.")


#test to see neu em load duoc model len khong