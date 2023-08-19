from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from  Utils.DataProcessing import process_links
import numpy as np
def round_th(a,th):
  if a<th:
    return 0
  return 1

#  Define the evaluation function
def evaluate_model(model, test_dataset, th):
    y_true = []
    y_true = np.concatenate([y.numpy() for _, y in test_dataset], axis=0).flatten()
    y_pred = model.predict(test_dataset)
    y_pred = y_pred.flatten()
    y_pred = [round_th(i,th) for i in y_pred]
    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:")
    print(cm)

    # Accuracy
    acc = accuracy_score(y_true, y_pred)
    print("Accuracy:", acc)

    # Precision
    prec = precision_score(y_true, y_pred, average='weighted')
    print("Precision:", prec)

    # Recall
    rec = recall_score(y_true, y_pred, average='weighted')
    print("Recall:", rec)

    # F1 Score
    f1 = f1_score(y_true, y_pred, average='weighted')
    print("F1 Score:", f1)
    
    return [cm,acc,prec,rec,f1]

def make_prediction(model, batch_size, Vectorize_Layer, links, th):
  ans = list()
  for _ in links:
    ds =  process_links([_], batch_size, Vectorize_Layer)
    y_pred = model.predict(ds)
    y_pred = y_pred.flatten()
    y_pred = [round_th(i,th) for i in y_pred]
    for _ in y_pred:
      if _ == 1:
        ans.append("Safe")
      else:
        ans.append("Malicious")
  return ans