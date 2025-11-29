import ctransformers

# error : chunked text still larger than the 512 limit of tokens

# def split_into_paragraphs(text : str) -> list[str]: # paragraph chunker module
#     paragraph = text.split("\n")

#     # convert large text to paragraph
    
#     chunks = [[]]
#     chunk_total_words = 0

#     for words in paragraph: # check if words in a paragraph is inside the limit
#         chunk_total_words += len(words.split(" "))
#         if chunk_total_words >= 384: # total words per the limit of the model prompt
#             chunks.append([])
#             chunk_total_words = len(words.split(" "))
#         chunks[len(chunks)-1].append(words)
#     return chunks # output as chunks[], i think
#     # this whole logic is wrong, how to fix

def split_into_paragraphs(text : str, paragraph_length : int = 384) -> list[str]: # paragraph chunker module
    paragraph = text.splitlines()
    list_of_output_paragraphs=[]
    current_paragraph=[]
    for line in paragraph:
        word_count=sum(len(i.split(" ")) for i in current_paragraph)+len(line.split(" "))
        if word_count>384: #current limit of the model that i set
            # Make a new line first

            # slice off the leading space
            list_of_output_paragraphs.append(current_paragraph)
            current_paragraph=[]
        current_paragraph.append(line)
    list_of_output_paragraphs.append(current_paragraph)
    return list_of_output_paragraphs


# one_large_text = r'''Multi-document extractive summarization faces a problem of redundancy. Ideally, we want to extract sentences that are both "central" (i.e., contain the main ideas) and "diverse" (i.e., they differ from one another). For example, in a set of news articles about some event, each article is likely to have many similar sentences. To address this issue, LexRank applies a heuristic post-processing step that adds sentences in rank order, but discards sentences that are too similar to ones already in the summary. This method is called Cross-Sentence Information Subsumption (CSIS). These methods work based on the idea that sentences "recommend" other similar sentences to the reader. Thus, if one sentence is very similar to many others, it will likely be a sentence of great importance. Its importance also stems from the importance of the sentences "recommending" it. Thus, to get ranked highly and placed in a summary, a sentence must be similar to many sentences that are in turn also similar to many other sentences. This makes intuitive sense and allows the algorithms to be applied to an arbitrary new text. The methods are domain-independent and easily portable. One could imagine the features indicating important sentences in the news domain might vary considerably from the biomedical domain. However, the unsupervised "recommendation"-based approach applies to any domain.
# A related method is Maximal Marginal Relevance (MMR),[21] which uses a general-purpose graph-based ranking algorithm like Page/Lex/TextRank that handles both "centrality" and "diversity" in a unified mathematical framework based on absorbing Markov chain random walks (a random walk where certain states end the walk). The algorithm is called GRASSHOPPER.[22] In addition to explicitly promoting diversity during the ranking process, GRASSHOPPER incorporates a prior ranking (based on sentence position in the case of summarization).
# The state of the art results for multi-document summarization are obtained using mixtures of submodular functions. These methods have achieved the state of the art results for Document Summarization Corpora, DUC 04 - 07.[23] Similar results were achieved with the use of determinantal point processes (which are a special case of submodular functions) for DUC-04.[24]
# A new method for multi-lingual multi-document summarization that avoids redundancy generates ideograms to represent the meaning of each sentence in each document, then evaluates similarity by comparing ideogram shape and position. It does not use word frequency, training or preprocessing. It uses two user-supplied parameters: equivalence (when are two sentences to be considered equivalent?) and relevance (how long is the desired summary?)'''
# chunks = []
# chunks = split_into_paragraphs(one_large_text)

def summarization_main(chunks,num_of_sentences:int)->int:
    system_message = "You are a pratical, fast and polite assistant."
    config = ctransformers.AutoConfig.from_pretrained(r"D:\05_uni_things\DoAn_Document_summary\tinyllama_model\tinyllama-1.1b-1t-openorca.Q2_K.gguf",local_files_only=True)
    config.config.max_new_tokens = 2000 # fault: need to put these configs before, you could do it, but now you know it is possible
    config.config.context_length = 4000 # without these configs, will get into out of token loop error
    llm = ctransformers.AutoModelForCausalLM.from_pretrained(r"D:\05_uni_things\DoAn_Document_summary\tinyllama_model\tinyllama-1.1b-1t-openorca.Q2_K.gguf", model_type="llama",
            
            local_files_only=True,
            config = config
            )
    summarized_text = ""
    model_is_fed = False
    for chunk in chunks:
        if model_is_fed != True:
            print("working part ")
            print(chunk)
            system_message = f"You are a summarizer. You write a summary of the input using following steps:  . "

            prompt = f"Walk through the key points of this research paper step-by-step, explaining each point’s significance. Then summarize the entire document into {num_of_sentences} sentences with this but ignore if the chunk is less than 10 words: {chunk}"


            model_is_fed = True


            txt_summarized = llm(f"<|im_start|>system {system_message} <|im_end|><|im_start|>user {prompt} <|im_end|> <|im_start|>assistant")
            # system_message = f"<|im_start|>system You are an efficient bot. <|im_end|>"
            # user_message = f"<|im_start|>user summarize this paragraph into {num_of_sentences}: {chunk} <|im_end|>"
            # # the fault is in this user_message
            # model_is_fed = True
            # assistant_message = f"{system_message} {user_message} <|im_start|>assistant "

            # txt_summarized = llm(f"{system_message} {user_message} <|im_start|>assistant {assistant_message} ") # loi logic, bo 1 cai imstart di
            # # txt_summarized = llm("summarize this as short as you can: "+ txt)

            summarized_text = summarized_text +"\n" + txt_summarized # adding new line after each lines of text summarized
            model_is_fed = False
        elif model_is_fed == True:
            print("model is working")
        else:
            print("something is wrong")

    return summarized_text    

# this will be the newest fix

# txt_summarized = summarization_main(chunks)
# print(txt_summarized)


if __name__ == '__main__':
#     # sua loi module chay luon ngay khi import o main
    load_llm()




'''
chatml format for the prompt
<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
'''

