# Shavian TTS
Convert Shavian text to SSML for use with Text-To-Speech (TTS) engines

```
usage: shavian_ssml.py [-h] [-m] [input_file]

positional arguments:
  input_file    Input file containing Shavian text

options:
  -h, --help    show this help message and exit
  -m, --modern  Use modern IPA style (default is traditional)
```

Created at the suggestion of u/ProvincialPromenade

## Installation

Requires with Python 3.6 (2016) or newer

### Linux/Unix/Mac

```
wget https://raw.githubusercontent.com/serif/Shavian_TTS/main/shavian_ssml.py
chmod +x shavian_ssml.py
./shavian_ssml.py
```

### Windows

- Download [shavian_ssml.py](https://raw.githubusercontent.com/serif/Shavian_TTS/main/shavian_ssml.py)
- In a terminal, run with `python shavian_ssml.py`

## Sample

If running with no input file, it converts the following demo text.

> 𐑭𐑤 𐑣𐑿𐑥𐑩𐑯 𐑚𐑰𐑦𐑙𐑟 𐑸 𐑚𐑹𐑯 𐑓𐑮𐑰 𐑯 𐑰𐑒𐑢𐑩𐑤 𐑦𐑯 𐑛𐑦𐑜𐑯𐑩𐑑𐑰 𐑯 𐑮𐑲𐑑𐑕. 𐑞𐑱 𐑸 𐑧𐑯𐑛𐑬𐑛 𐑢𐑦𐑞 𐑮𐑰𐑟𐑩𐑯 𐑯 𐑒𐑭𐑯𐑖𐑩𐑯𐑕 𐑯 𐑖𐑫𐑛 𐑨𐑒𐑑 𐑑𐑹𐑛𐑟 𐑢𐑩𐑯 𐑩𐑯𐑳𐑞𐑼 𐑦𐑯 𐑩 𐑕𐑐𐑦𐑮𐑦𐑑 𐑝 𐑚𐑮𐑳𐑞𐑼𐑣𐑫𐑛.

This is Article 1 of the Universal Declaration of Human Rights, "All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood."

That Shavian text is converted to the following SSML using either Modern IPA or Traditional IPA (default, seems to work better with Microsoft Speech Studio). (see [shavian.school/table.html](https://shavian.school/table.html))

```xml
<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">
  <voice name="en-US-JennyNeural">
<phoneme alphabet="ipa" ph="ɑːl">𐑭𐑤</phoneme> <phoneme alphabet="ipa" ph="hjuːmən">𐑣𐑿𐑥𐑩𐑯</phoneme> <phoneme alphabet="ipa" ph="biːɪŋz">𐑚𐑰𐑦𐑙𐑟</phoneme> <phoneme alphabet="ipa" ph="ɑːr">𐑸</phoneme> <phoneme alphabet="ipa" ph="bɔːrn">𐑚𐑹𐑯</phoneme> <phoneme alphabet="ipa" ph="friː">𐑓𐑮𐑰</phoneme> <phoneme alphabet="ipa" ph="ənd">𐑯</phoneme> <phoneme alphabet="ipa" ph="iːkwəl">𐑰𐑒𐑢𐑩𐑤</phoneme> <phoneme alphabet="ipa" ph="ɪn">𐑦𐑯</phoneme> <phoneme alphabet="ipa" ph="dɪgnətiː">𐑛𐑦𐑜𐑯𐑩𐑑𐑰</phoneme> <phoneme alphabet="ipa" ph="ənd">𐑯</phoneme> <phoneme alphabet="ipa" ph="raɪts">𐑮𐑲𐑑𐑕</phoneme>. <phoneme alphabet="ipa" ph="ðeɪ">𐑞𐑱</phoneme> <phoneme alphabet="ipa" ph="ɑːr">𐑸</phoneme> <phoneme alphabet="ipa" ph="ɛndaʊd">𐑧𐑯𐑛𐑬𐑛</phoneme> <phoneme alphabet="ipa" ph="wɪð">𐑢𐑦𐑞</phoneme> <phoneme alphabet="ipa" ph="riːzən">𐑮𐑰𐑟𐑩𐑯</phoneme> <phoneme alphabet="ipa" ph="ənd">𐑯</phoneme> <phoneme alphabet="ipa" ph="kɑːnʃəns">𐑒𐑭𐑯𐑖𐑩𐑯𐑕</phoneme> <phoneme alphabet="ipa" ph="ənd">𐑯</phoneme> <phoneme alphabet="ipa" ph="ʃʊd">𐑖𐑫𐑛</phoneme> <phoneme alphabet="ipa" ph="ækt">𐑨𐑒𐑑</phoneme> <phoneme alphabet="ipa" ph="tɔːrdz">𐑑𐑹𐑛𐑟</phoneme> <phoneme alphabet="ipa" ph="wən">𐑢𐑩𐑯</phoneme> <phoneme alphabet="ipa" ph="ənʌðər">𐑩𐑯𐑳𐑞𐑼</phoneme> <phoneme alphabet="ipa" ph="ɪn">𐑦𐑯</phoneme> <phoneme alphabet="ipa" ph="ə">𐑩</phoneme> <phoneme alphabet="ipa" ph="spɪrɪt">𐑕𐑐𐑦𐑮𐑦𐑑</phoneme> <phoneme alphabet="ipa" ph="ʌv">𐑝</phoneme> <phoneme alphabet="ipa" ph="brʌðərhʊd">𐑚𐑮𐑳𐑞𐑼𐑣𐑫𐑛</phoneme>.
  </voice>
</speak>
```

## Listen

- Go to [speech.microsoft.com/audiocontentcreation](https://speech.microsoft.com/audiocontentcreation)
- Enable SSML input with the switch
- Replace all content in the text box with the SSML output from this pre-processor
- Click the ▶ Play button above the editor
