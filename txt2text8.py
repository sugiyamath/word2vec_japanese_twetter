if __name__ == "__main__":
    import sentencepiece as spm
    import re
    from tqdm import tqdm

    sp = spm.SentencePieceProcessor()
    sp.Load('sp/sp.model')
    
    regex_url = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    regex_user = re.compile('@(\w){1,15}')

    with open("sp/tweet.txt", "r") as f:
        for i, line in tqdm(enumerate(f)):
            try:
                line = line.strip()
                line = re.sub(regex_url, "", line)
                line = re.sub(regex_user, "", line)
                data = ' '.join([l.replace("▁", "").replace("#","") for l in sp.EncodeAsPieces(line)])
                with open("tweet_ja.text8", "a") as g:
                    g.write(data+"\n")
            except:
                print("error: fail line {}".format(i))
                
    print("Done!")