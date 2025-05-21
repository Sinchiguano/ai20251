


import tensorflow as tf
import keras 


from tensorflow import keras
model = keras.Sequential([
    keras.layers.Dense(16, activation="relu", input_shape=(8,)),
    keras.layers.Dense(1, activation="sigmoid")
])
model.compile(optimizer="adam", loss="binary_crossentropy")
print("Model built and compiled ✅")





print("TENSORFLOW VERSION: ",tf.__version__)
print("KERAS VERSION: ",keras.__version__)

