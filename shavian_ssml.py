#!/usr/bin/env python3
# shavian_ssml.py for Python 3.6 (2016) or newer
# Converts Shavian text to SSML with IPA for use with Text-To-Speech engines
import sys
import argparse


# Shavian IPA equivalency tables
ipa_modern: dict[str, str] = {
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
ipa_traditional: dict[str, str] = {
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


def main() -> None:
    args: argparse.Namespace = arguments()
    translator = Translator(args)

    # Read file if provided
    if args.input_file:
        desc = 'Input'
        text = translator.read_text(args.input_file)
    # Demo if no file
    else:
        desc = 'Universal Declaration of Human Rights'
        text = '𐑭𐑤 𐑣𐑿𐑥𐑩𐑯 𐑚𐑰𐑦𐑙𐑟 𐑸 𐑚𐑹𐑯 𐑓𐑮𐑰 𐑯 𐑰𐑒𐑢𐑩𐑤 𐑦𐑯 𐑛𐑦𐑜𐑯𐑩𐑑𐑰 𐑯 𐑮𐑲𐑑𐑕. '
        text += '𐑞𐑱 𐑸 𐑧𐑯𐑛𐑬𐑛 𐑢𐑦𐑞 𐑮𐑰𐑟𐑩𐑯 𐑯 𐑒𐑪𐑯𐑖𐑩𐑯𐑕 𐑯 𐑖𐑫𐑛 𐑨𐑒𐑑 𐑑𐑹𐑛𐑟 𐑢𐑳𐑯 '
        text += '𐑩𐑯𐑳𐑞𐑼 𐑦𐑯 𐑩 𐑕𐑐𐑦𐑮𐑦𐑑 𐑝 𐑚𐑮𐑳𐑞𐑼𐑣𐑫𐑛.'

    # Create SSML
    out = translator.make_ssml(text)
    print(f'\n{desc}:\n{text}')
    print(f'\nOutput:\n{out}')
    written = translator.write_output(out)
    print(written)
    print('Test in SSML mode here:')
    print('https://speech.microsoft.com/audiocontentcreation')


def arguments() -> None:
    parser = argparse.ArgumentParser(
        description='Convert Shavian text to SSML with IPA for TTS engines')
    # parser.add_argument('--ipa', choices=['modern', 'traditional'],
        # default='traditional', help='Select IPA style')
    parser.add_argument('-m', '--modern', action='store_true',
        help='Use modern IPA style (default is traditional)')
    parser.add_argument('-r', '--region', choices=['us', 'gb'],
        default='gb', help='Select TTS region (us or gb)')
    parser.add_argument('input_file', nargs='?',
        help='Input file containing Shavian text')
    return parser.parse_args()


class Translator:
    def __init__(self, args: argparse.Namespace) -> None:
        self.in_file: str = ''
        self.out_file: str = ''
        self.shavipa: dict[str, str] = {}

        # Select IPA type
        if args.modern:
            global ipa_modern
            self.shavipa = ipa_modern
        else:
            global ipa_traditional
            self.shavipa = ipa_traditional

        # Select region and voice
        if args.region == 'us':
            lang = 'en-US'
            voice = 'en-US-JennyNeutral'
        else:  # Default to 'gb'
            lang = 'en-GB'
            voice = 'en-GB-SoniaNeural'
        self.ssml_open = '<speak xmlns="http://www.w3.org/2001/10/synthesis" '
        self.ssml_open += 'xmlns:mstts="http://www.w3.org/2001/mstts" '
        self.ssml_open += 'xmlns:emo="http://www.w3.org/2009/10/emotionml" '
        self.ssml_open += f'version="1.0" xml:lang="{lang}">\n'
        self.ssml_open += f'  <voice name="{voice}">\n'
        self.ssml_close: str = '\n  </voice>\n</speak>\n'
        self.phoneme: str = '<phoneme alphabet="ipa" ph="THEIPA">'
        self.phoneme += 'THESHA</phoneme>'

    # Read Shavian text from file supplied as command parameter
    def read_text(self, in_file: str) -> str:
        self.in_file = in_file
        self.out_file = "out_" + in_file
        try:
            with open(self.in_file, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"File '{self.in_file}' not found.")
            sys.exit(1)

    # Wrap word in phoneme tag
    def wrap(self, word: str) -> str:
        sha = ''.join(word)
        ipa = ''.join([self.shavipa[c] for c in sha])

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
        out = self.phoneme.replace('THEIPA', ipa).replace('THESHA', sha)
        return out

    # Takes Shavian text, returns SSML
    def make_ssml(self, text: str) -> str:
        out = self.ssml_open
        word = ''

        # Read char-by-char
        # Add to word buffer if Shavian
        # Wrap buffer then pass through when not Shavian
        for char in text:
            if char in self.shavipa:
                word += char
            else:
                if word:
                    out += self.wrap(word)
                    word = ''
                out += char

        # Ensure final buffer is processed
        if word:
            out += self.wrap(word)
        out += self.ssml_close

        return ''.join(out).strip()

    # Write SSML to file (if initially read from file)
    def write_output(self, out: str) -> str:
        if not self.out_file:
            return ''
        with open(self.out_file, 'w', encoding='utf-8') as file:
            file.write(out)
        return f'\nSSML saved to {self.out_file}'


if __name__ == '__main__':
    main()

