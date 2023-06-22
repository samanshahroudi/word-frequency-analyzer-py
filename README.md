## Word Frequency Analyzer (Python)
The Word Frequency Analyzer is a Python script that analyzes a text-based file (.txt, .srt, etc.) and generates an HTML file containing a list of words along with their frequency of occurrence in the text. It can be particularly useful for generating dictionaries or vocabulary lists from various text-based sources, including subtitles.

### Features
* Counts the frequency of each word in the input text file.
* Excludes numbers and words below a specified minimum length threshold.
* Supports linking words to popular online dictionaries for reference.
* Provides an option to include a Google Translate link for word translation.

### Prerequisites
* Python 3.x
* Libraries mentioned in the requirements.txt file

### Usage
1. Clone the repository:
```shell
git clone https://github.com/samanshahroudi/word-frequency-analyzer-py.git
```
2. Navigate to the project directory:
```shell
cd word-frequency-analyzer-py
```
3. Create virtual env for project
```shell
python3 -m venv .venv
```
4. Activate virtual env (Ubuntu)
```shell
source .venv/bin/activate 
```
5. Install the required dependencies:
```shell
pip install -r requirements.txt
```
6. Run the script:
```shell
python script.py <text_file> <output_file> [--min_length_threshold <min_length>] [--google_translate_to <language_code>]
```
Replace <text_file> with the path to your input text file and <output_file> with the desired path for the output HTML file. You can also specify an optional minimum length threshold for words and a destination language code for Google Translate.

7. Open the generated HTML file in a web browser to view the word frequency analysis results.

   ![](https://github.com/samanshahroudi/word-frequency-analyzer-py/blob/main/images/generated_html.png?raw=true)

### Example
To analyze the frequency of words in a text file named "input.txt" and generate an HTML file named "output.html":
```shell
python script.py input.txt output.html
```