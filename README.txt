Example-Based Machine Translation

This code demonstrates example-based machine translation from English and Azerbaijani to Turkish using the Zemberek library and NLTK.

Requirements:
- Python 3.x
- zemberek-python library (install with 'pip install zemberek-python')
- NLTK library (install with 'pip install nltk' and download the 'punkt' package with 'nltk.download("punkt")')

Usage:
1. Modify the file paths in the code:
   - Open the Python script in a text editor.
   - Locate the file path variables: 'english_file_path', 'azerbaijani_file_path', and 'turkish_file_path'.
   - Update the file paths to the respective locations of your text files.
   - english_sentences.txt: Contains English sentences separated by newline characters.
   - azerbaijani_sentences.txt: Contains Azerbaijani sentences separated by newline characters.
   - turkish_sentences.txt: Contains Turkish sentences separated by newline characters.

2. Run the script in a Python environment that meets the requirements.

3. The program will present a menu with the following options:
   1. English to Turkish
   2. Azerbaijani to Turkish
   3. Exit

4. Choose an option by entering the corresponding number.

5. If you choose option 1, enter an English sentence when prompted. The program will translate it to Turkish using example-based machine translation and display the translated sentence along with the BLEU score.

6. If you choose option 2, enter an Azerbaijani sentence when prompted. The program will translate it to Turkish using example-based machine translation and display the translated sentence along with the BLEU score.

7. Repeat steps 4-6 as desired. To exit the program, choose option 3.

Note:
- The script assumes that the text files are properly formatted, with one sentence per line and no empty lines.
- Make sure the required libraries are installed and imported correctly.
- The Turkish sentences will be preprocessed using Turkish morphological analysis and normalization provided by the Zemberek library.
- The BLEU score is calculated using the NLTK library.

 
