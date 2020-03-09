from webapp import data
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def TF_IDF(item_name, num):
    ds = data.ds()
    tf = TfidfVectorizer(analyzer='word', ngram_range=(
        1, 3), min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(ds['popular_tags'].values.astype('U'))

    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    results = {}

    for idx, row in ds.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], ds['name'][i])
                         for i in similar_indices]

        results[row['name']] = similar_items[1:]
    recs = results[item_name][:num]
    print('Game : '+item_name)
    print('------------------------------------------------------')
    for rec in recs:
        print('Recommend : ' + rec[1] + ' (Score : ' + str(rec[0]) +')')
    return recs