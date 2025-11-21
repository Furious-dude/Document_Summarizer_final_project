from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# function chinh cua chuc nang to tat dang 2
def sumy_summarizer(text_raw:str,number_of_line:int) -> str:
    parser = PlaintextParser.from_string(text_raw,Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document,number_of_line)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

if __name__ == "__main__":
    main()