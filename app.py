import gradio as gr
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import random
import re
import json
import tensorflow as tf
import mysql.connector
from nltk.util import ngrams
import itertools
from Utils import Evaluation
from Utils import DataProcessing, FeatureCreation, Model

N_for_NGram = 3
Sequence_length = 50
Batch_Size = 128
max_tokens = 10000
host = os.environ["HOST"]
user = os.environ["USER"]
password = os.environ["PASSWORD"]
database = os.environ["DATABASE"]

from gradio.components import File, Textbox

class DataFlagger(gr.FlaggingCallback):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def setup(self, a, b):
        pass

    def flag(self,
        flag_data,
        flag_option: str | None = None,
        flag_index: int | None = None,
        username: str | None = None,):
        input_data = flag_data[0]
        output_data = flag_data[1]
        message = "Safe"
        if output_data == "Safe":
          message = "Malicious"
        connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password , database=self.database)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO `URL_CLASSIFIER` (`serial_number`,`url`,`type`) VALUES (NULL,'{input_data}','{message}');")
        connection.commit()
        cursor.close()
        connection.close()


# Define a function that takes a list of links as input and returns the prediction result as output
def url_checker(link):
    # Split the input by comma and strip any whitespace
    links = [link]
    connection = mysql.connector.connect(host=host, user=user, password=password , database=database)
    cursor = connection.cursor()
    cursor.execute(f"SELECT type FROM `URL_CLASSIFIER` WHERE url = '{link}';")
    ls = list(cursor.fetchall())
    if(len(ls)!=0):
      cursor.close()
      connection.close()
      return str(ls[0][0])
    else:
      model = tf.keras.models.load_model("./Trained_Model/Model.keras")
      with open("./Trained_Model/Vectorization_Layer/vocab.json", "r") as f:
          vocab = json.load(f)

      VL = tf.keras.layers.TextVectorization(standardize='lower_and_strip_punctuation',
                                                    split="character",
                                                    ngrams=(N_for_NGram,),
                                                    output_mode='int',
                                                    output_sequence_length=Sequence_length,
                                                    vocabulary=vocab)
      # Call the Evaluation.make_prediction function with the model, batch size, vectorization layer, links and threshold
      result = Evaluation.make_prediction(model, Batch_Size, VL, links, 0.5)
      # Return the result as a string
      return str(result[0])

# Define a Gradio interface with a text input and a text output
iface = gr.Interface(fn=url_checker,
             allow_flagging="manual",
            flagging_callback=DataFlagger(host, user, password, database), inputs=Textbox(label="Enter the link."), outputs="text")
# Launch the interface
iface.launch(debug=True)