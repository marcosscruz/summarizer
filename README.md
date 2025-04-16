# Automatic Text Summarizer

A Python-based automatic text summarization tool that preserves the original text structure (including stop words) and allows adjustable compression levels. Summaries retain sentence order for coherence.

## Features
- **Preservation of Original Text**: No removal of stop words or sentence alterations.
- **Adjustable Compression**: Specify summary length as a percentage (1-100) of the original text.
- **Batch Processing**: Process multiple `.txt` files in a directory.
- **Order Retention**: Selected sentences appear in their original sequence.

## Installation

### Dependencies
- Python 3.6+
- Required libraries:  
  ```bash
  pip install -r requirements.txt
  ```

## Usage

### Command-Line Arguments
| Argument               | Description                                  |
|------------------------|----------------------------------------------|
| `--input-dir`          | Directory containing input `.txt` files      |
| `--output-dir`         | Directory to save summarized files           |
| `--compression-level`  | Summary length as % of original (1-100)      |

### Example
```bash
python summarizer.py --input-dir ./documents --output-dir ./summaries --compression-level 30
```