
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
# Libraries for TensorFlow
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing import image
from tensorflow.keras import models, layers
# Library for Transfer Learning
from tensorflow.keras.applications import VGG16
from keras.applications.efficientnet import preprocess_input

print("Importing libraries completed.")



train_folder =  "Blood/"


# variables for image size
img_width = 200
img_height = 200

# variable for model
batch_size = 32
epochs =10


train_class_names = os.listdir(train_folder)
print("Train class names: %s" % (train_class_names))


# Declaring variables
x = []  # to store array value of the images
y = []  # to store the labels of the images

for folder in os.listdir(train_folder):
    image_list = os.listdir(train_folder + "/" + folder)
    for img_name in image_list:
        # Loading images
        img = image.load_img(train_folder + "/" + folder + "/" + img_name, target_size=(img_width, img_height))
        img = image.img_to_array(img)
        img = preprocess_input(img)

        x.append(img)
        y.append(train_class_names.index(folder))  # appending class index to the array

print("Training Dataset")

x = np.array(x)
print(x.shape)

y = to_categorical(y)
# print(y)
print(y.shape)

from tensorflow.keras.applications import EfficientNetB3
base_model = EfficientNetB3(weights='imagenet', include_top=False, input_shape=(img_width, img_height, 3))
base_model.trainable = False
last_layer = base_model.output
flatten = layers.GlobalAveragePooling2D()(last_layer)  # Better than Flatten for CNNs
output_layer = layers.Dense(5, activation='softmax')(flatten)
model = models.Model(inputs=base_model.input, outputs=output_layer)
model.summary()

from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=0)
print("Splitting data for train and test completed.")

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print("Model compilation completed.")

history2 = model.fit(xtrain, ytrain, epochs=epochs, batch_size=batch_size, verbose=True, validation_data=(xtrain, ytrain))

print("Fitting the model completed.")

model.save("bmodel.h5")

acc = history2.history['accuracy']
val_acc = history2.history['val_accuracy']
epochs = range(len(acc))

plt.plot(epochs, acc, label='Training Accuracy')
plt.plot(epochs, val_acc, label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()

# Plot Model Loss
loss_train = history2.history['loss']
loss_val = history2.history['val_loss']
plt.plot(epochs, loss_train, label='Training Loss')
plt.plot(epochs, loss_val, label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()

y_pred = model.predict(xtrain)
y_pred = np.argmax(y_pred, axis=1)
print(y_pred)
y_test=np.argmax(ytrain, axis=1)
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
print(cm)

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix  ')
plt.show()