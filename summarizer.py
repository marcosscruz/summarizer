import argparse
import os
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import nltk

nltk.download('punkt')

def summarize_text(text, compression_level):
    """
    resume o texto usando o algoritmo TextRank e mantém a ordem original das frases
    """
    parser = PlaintextParser.from_string(text, Tokenizer("portuguese"))
    summarizer = TextRankSummarizer()
    document = parser.document
    total_sentences = len(document.sentences)
    
    if total_sentences == 0:
        return ""
    
    # calcula o número de frases a incluir
    num_sentences = max(1, int(total_sentences * (compression_level / 100)))
    if num_sentences >= total_sentences:
        return text  # se nenhum resumo for necessário retorna o texto original
    
    # extrai as frases originais e as classifica
    summary_sentences = summarizer(document, num_sentences)
    sentence_indices = [document.sentences.index(sent) for sent in summary_sentences]
    sorted_indices = sorted(sentence_indices)
    sorted_summary = [document.sentences[i] for i in sorted_indices]
    
    return ' '.join(str(sentence) for sentence in sorted_summary)

def process_files(input_dir, output_dir, compression_level):
    """
    processa todos os arquivos .txt no diretório de entrada e salva os resumos
    """
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_dir, filename)
            base_name = os.path.splitext(filename)[0]
            output_filename = f"{base_name}_summary_{compression_level}.txt"
            output_path = os.path.join(output_dir, output_filename)
            
            with open(input_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            summary = summarize_text(text, compression_level)
            
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(summary)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sumarizador automático')
    parser.add_argument('--input-dir', type=str, required=True, help='Diretório contendo arquivos .txt de entrada')
    parser.add_argument('--output-dir', type=str, required=True, help='Diretório para salvar arquivos resumidos')
    parser.add_argument('--compression-level', type=int, required=True, help='Nível de compressão (1-100)')
    
    args = parser.parse_args()
    
    if not 1 <= args.compression_level <= 100:
        raise ValueError("O nível de compressão deve estar entre 1 e 100")
    
    process_files(args.input_dir, args.output_dir, args.compression_level)