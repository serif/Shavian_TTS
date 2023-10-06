#!/usr/bin/env python3
# shavian_ssml.py for Python 3.6 (2016) or newer
# Converts Shavian text to SSML with IPA for use with Text-To-Speech engines
import sys


# Global variables here at the top to keep them easy to see and change.
# The xml/ssml below is for Microsoft TTS since that is freely accessible
# by web browser and requires no other software be installed.
ssml_open = '<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">\n  <voice name="en-US-JennyNeural">\n'
phoneme = '<phoneme alphabet="ipa" ph="THEIPA">THESHA</phoneme>'
ssml_close = '\n  </voice>\n</speak>\n'
ipa_modern = {
    '𐑐': 'p', '𐑚': 'b', '𐑑': 't', '𐑛': 'd', '𐑒': 'k', '𐑜': 'g',
    '𐑓': 'f', '𐑝': 'v', '𐑔': 'θ', '𐑞': 'ð', '𐑕': 's', '𐑟': 'z',
    '𐑖': 'ʃ', '𐑠': 'ʒ', '𐑗': 'ʧ', '𐑡': 'ʤ', '𐑘': 'j', '𐑢': 'w',
    '𐑙': 'ŋ', '𐑣': 'h', '𐑤': 'l', '𐑮': 'r', '𐑥': 'm', '𐑯': 'n',
    '𐑦': 'ɪ́', '𐑰': 'ɪ́j', '𐑧': 'ɛ́', '𐑱': 'ɛ́j', '𐑨': 'á', '𐑲': 'ɑ́j',
    '𐑩': 'ə', '𐑳': 'ə́', '𐑪': 'ɔ́', '𐑴': 'ə́w', '𐑫': 'ʉ́', '𐑵': 'ʉ́w',
    '𐑬': 'áw', '𐑶': 'ój', '𐑭': 'ɑ́ː', '𐑷': 'óː',
    '𐑸': 'ɑ́ːr', '𐑹': 'óːr', '𐑺': 'ɛ́ːr',
    '𐑻': 'ə́ːr', '𐑼': 'ər', '𐑽': 'ɪ́ːr',
    '𐑾': 'ɪjə', '𐑿': 'jʉ́w'
}
ipa_traditional = {
    '𐑐': 'p', '𐑚': 'b', '𐑑': 't', '𐑛': 'd', '𐑒': 'k', '𐑜': 'g',
    '𐑓': 'f', '𐑝': 'v', '𐑔': 'θ', '𐑞': 'ð', '𐑕': 's', '𐑟': 'z',
    '𐑖': 'ʃ', '𐑠': 'ʒ', '𐑗': 'ʧ', '𐑡': 'ʤ', '𐑘': 'j', '𐑢': 'w',
    '𐑙': 'ŋ', '𐑣': 'h', '𐑤': 'l', '𐑮': 'r', '𐑥': 'm', '𐑯': 'n',
    '𐑦': 'ɪ', '𐑰': 'iː', '𐑧': 'ɛ', '𐑱': 'eɪ', '𐑨': 'æ', '𐑲': 'aɪ',
    '𐑩': 'ə', '𐑳': 'ʌ', '𐑪': 'ɒ', '𐑴': 'əʊ', '𐑫': 'ʊ', '𐑵': 'uː',
    '𐑬': 'aʊ', '𐑶': 'ɔɪ', '𐑭': 'ɑː', '𐑷': 'ɔː',
    '𐑸': 'ɑːr', '𐑹': 'ɔːr', '𐑺': 'ɛəːr',
    '𐑻': 'ɜːr', '𐑼': 'ər', '𐑽': 'ɪər',
    '𐑾': 'ɪə', '𐑿': 'juː'
}
# Select your preferred IPA set here
shavipa = ipa_traditional


def main():
    translator = Translator()

    if len(sys.argv) != 2:
        desc = 'Demo'
        print('Usage: python shavian_ssml.py <in_file>')
        print('Example: python shavian_ssml.py input.txt')
        text = '𐑭𐑤 𐑣𐑿𐑥𐑩𐑯 𐑚𐑰𐑦𐑙𐑟 𐑸 𐑚𐑹𐑯 𐑓𐑮𐑰 𐑯 𐑰𐑒𐑢𐑩𐑤 𐑦𐑯 𐑛𐑦𐑜𐑯𐑩𐑑𐑰 𐑯 𐑮𐑲𐑑𐑕. 𐑞𐑱 𐑸 𐑧𐑯𐑛𐑬𐑛 𐑢𐑦𐑞 𐑮𐑰𐑟𐑩𐑯 𐑯 𐑒𐑭𐑯𐑖𐑩𐑯𐑕 𐑯 𐑖𐑫𐑛 𐑨𐑒𐑑 𐑑𐑹𐑛𐑟 𐑢𐑩𐑯 𐑩𐑯𐑳𐑞𐑼 𐑦𐑯 𐑩 𐑕𐑐𐑦𐑮𐑦𐑑 𐑝 𐑚𐑮𐑳𐑞𐑼𐑣𐑫𐑛.'
    else:
        desc = 'Input'
        in_file = sys.argv[1]
        text = translator.read_text(in_file)

    out = translator.make_ssml(text)
    print(f'\n{desc}:\n{text}')
    print(f'\nOutput:\n{out}')
    written = translator.write_output(out)
    print(written)
    print('Test here:\nhttps://speech.microsoft.com/audiocontentcreation')


class Translator:
    def __init__(self):
        self.in_file = ''
        self.out_file = ''

    # Read Shavian text from file supplied as command parameter
    def read_text(self, in_file):
        self.in_file = in_file
        self.out_file = "out_" + in_file
        try:
            with open(self.in_file, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"File '{self.in_file}' not found.")
            sys.exit(1)

    # Wrap word in phoneme tag
    def wrap(self, word):
        global shavipa
        global phoneme

        sha = ''.join(word)
        ipa = ''.join([shavipa[c] for c in sha])

        # Expand abbreviations
        # Must be done here at the word-level
        abbreviations = {
            'ð': 'ðə',
            'v': 'ʌv',
            # æsh ends up sounding over-emphasized
            # 'n': 'ænd',
            'n': 'ənd',
            't': 'tu',
            'f': 'fɔr'
        }
        for k, v in abbreviations.items():
            if ipa == k:
                ipa = v
                break

        # Insert into phoneme tag
        out = phoneme.replace('THEIPA', ipa).replace('THESHA', sha)
        return out

    # Takes Shavian text, returns SSML
    def make_ssml(self, text):
        global ssml_open
        global ssml_close

        out = [ssml_open]
        word = []

        # Read char-by-char
        # Add to word buffer if Shavian
        # Wrap buffer then pass through when not Shavian
        for char in text:
            if char in shavipa:
                word.append(char)
            else:
                if word:
                    out.append(self.wrap(word))
                    word.clear()
                out.append(char)

        # Ensure final buffer is processed
        if word:
            out.append(self.wrap(word))
        out.append(ssml_close)

        return ''.join(out).strip()

    # Write SSML to file (if initially read from file)
    def write_output(self, out):
        if not self.out_file:
            return ''
        with open(self.out_file, 'w', encoding='utf-8') as file:
            file.write(out)
        return f'\nSSML saved to {self.out_file}'


if __name__ == "__main__":
    main()
