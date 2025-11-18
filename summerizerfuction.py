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

# def load_llm():
#     pass


def load_llm(string_a):
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
    try:

            txt = self.textbox.get("0.0",customtkinter.END)
            self.main_button_1.configure(state="disabled")
            # global summary_cache # lay cache o ngoai, vi python hoat dong khac so voi cac ngon ngu lap trinh khac
            # if summary_cache:
            #     txt = summary_cache # lay text tu ben da lay sang cache, global  
            # else:
            llm = AutoModelForCausalLM.from_pretrained(r"D:\05_uni_things\DoAn_Document_summary\tinyllama_model\tinyllama-1.1b-1t-openorca.Q2_K.gguf", model_type="llama",local_files_only=True)
            txt_summarized = llm("summarize this as short as you can: "+ txt)# dang lam, buon ngu qua
            self.textbox.insert("0.0",txt_summarized) # hien thi ket qua xuong duoi txtbox nho
            # threading.Thread(target=text_summerize).start() # thread nhu nay se khong hoat dong duoc
    except Exception as e:
            tkinter.messagebox.showerror("Error",f"{e}")
    finally:
            self.main_button_1.configure(state="enabled")
            #cai nay se khong lam duoc, de thu xem cach khac nhu nao, vi cai nayf se khien 
            # txt ket lai o vi tri processing, nhung co the minh se cho thread vao day luon
    
        # print(llm("Summarize this text : " + txt)) # khong can nua, day la de test
    return llm
    llm = AutoModelForCausalLM.from_pretrained(r"D:\05_uni_things\DoAn_Document_summary\tinyllama_model\tinyllama-1.1b-1t-openorca.Q2_K.gguf", model_type="llama",local_files_only=True)
    if string_a!=NULL:
        print(llm("Summarize this text : " + text(string_a)))
        return llm

    elif string_a=="":
        print("write something")
        return llm

    else:
        return

# def load_llm(string_a):
#     llm = AutoModelForCausalLM.from_pretrained(r"D:\05_uni_things\DoAn_Document_summary\tinyllama_model\tinyllama-1.1b-1t-openorca.Q2_K.gguf", model_type="llama",local_files_only=True)
#     print(llm(text(string_a)))
#     return llm

# Call load_llm() to create an instance of the model
# llm_model = load_llm()

# Test if the model was loaded successfully
# if llm_model is not None:
#     print("Model loaded successfully.")
# else:
#     print("Failed to load the model.")

#test to see neu em load duoc model len khong

if __name__ == '__main__':
    # sua loi module chay luon ngay khi import o main
    load_llm()