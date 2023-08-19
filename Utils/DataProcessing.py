import pandas as pd
import tensorflow as tf
import re
from  Utils.FeatureCreation import create_features
AUTOTUNE = tf.data.AUTOTUNE

# Define a function to preprocess the link
def preprocess_link(link):
    # Convert all letters to lowercase
    link = link.lower()
    link = link.replace("http://","")
    link = link.replace("https://","")
    link = link.replace("www.","")
    link = link.replace(" ","")
    link = link.strip()
    # Remove punctuation and special characters
    link = re.sub('[^A-Za-z0-9]+', '', link)
    return link

def process_train_data(df,batch_size):
    df = create_features(df)
    df['url'] = df['url'].apply(preprocess_link)
    df = df.drop_duplicates(subset=['url'])
    df = df.dropna().reset_index(drop=True)
    ds = tf.data.Dataset.from_tensor_slices(((df['url'].values, df.iloc[:,2:].values), df['type'].values))
    ds = ds.batch(batch_size)
    return ds

def vectorize_text(text,numerics, label, Vectorize_Layer):
    text = tf.expand_dims(text, -1)
    return (Vectorize_Layer(text), numerics), label

def process_data(df,batch_size, Vectorize_Layer):
    ds = process_train_data(df,batch_size)
    ds = ds.unbatch()
    ds = ds.shuffle(10000)
    ds = ds.batch(batch_size)
    ds = ds.map(lambda x, z: vectorize_text(x[0],x[1],z,Vectorize_Layer))
    ds = ds.cache().prefetch(buffer_size=AUTOTUNE)
    return ds

def process_links(links,batch_size, Vectorize_Layer):
    df = pd.DataFrame()
    df['url'] = links
    # here type is not provided as these links type is to be predicted, so we are keeping -1 just only for maintaining dimensionality
    df['type'] = -1
    return process_data(df,batch_size, Vectorize_Layer)