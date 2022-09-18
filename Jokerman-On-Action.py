
PATH_To_Model_h5_File = input("Enter the path to the model .h5 file: ")

saved_model = load_model(PATH_To_Model_h5_File)

def normalized_inverse(float_num):
  return (1/float_num)


def Run_Jokerman():
 # saved_model = load_model(PATH_To_Model_h5_File)
  no_of_sentences = int(input("Enter the number of sentences you want as input: "))

  sentence = []
  print("\n")
  for i in range(0,no_of_sentences):
    inpt = input(str(i+1)+ "-th sentence: ")
    sentence.append(str(inpt))

  print("\n\n")

  # sentence = ["granny starting to fear spiders in the garden might be real", "game of thrones season finale showing this sunday night"]

  sequences = tokenizer.texts_to_sequences(sentence)
  padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
  result = saved_model.predict(padded)
  print("\n")
  result

  float_result=[]

  for j in range(0,len(result)):
    float_result.append(str(float(normalized_inverse(result[i]))))

  JsoNBoy = {"Syntagma":sentence, "Semantic Integrity":float_result
                      }
  df = pd.DataFrame.from_dict(JsoNBoy, orient='index')
  df = df.transpose()
  return HTML(df.to_html()) 
  print("\n")