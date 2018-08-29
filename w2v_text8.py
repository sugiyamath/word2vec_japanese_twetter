import logging
from gensim.models import word2vec

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus('data/tweet_ja.text8')
    model = word2vec.Word2Vec(sentences, size=200, workers=8)
    model.save("word2vec_tweet.model")