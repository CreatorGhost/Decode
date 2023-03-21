import requests

def download_bip39_wordlist():
    url = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"
    response = requests.get(url)
    if response.status_code == 200:
        wordlist = response.text.split('\n')[:-1]
        return wordlist
    else:
        raise Exception("Failed to download BIP39 word list")

def bip39_words_to_indices(words, wordlist):
    indices = []
    for word in words:
        if word in wordlist:
            index = wordlist.index(word)
            indices.append(index)
        else:
            raise ValueError(f"Invalid BIP39 word: {word}")
    return indices

def bip39_indices_to_words(indices, wordlist):
    words = []
    for index in indices:
        if 0 <= index < len(wordlist):
            word = wordlist[index]
            words.append(word)
        else:
            raise ValueError(f"Invalid BIP39 word index: {index}")
    return words

if __name__ == "__main__":
    bip39_wordlist = download_bip39_wordlist()
    input_words = ["pistol", "maple", "dutch", "expire", "rent", "cluster", "science", "transfer", "toast", "canyon", "illness", "cage"]
    
    # Convert words to indices
    result_indices = bip39_words_to_indices(input_words, bip39_wordlist)
    print("BIP39 word indices:", result_indices)
    
    # Convert indices back to words
    result_words = bip39_indices_to_words(result_indices, bip39_wordlist)
    print("BIP39 words from indices:", result_words)
