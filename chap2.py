# transfer learning using MobileNet-V3 large

from tensorflow.keras import Model
from tensorflow.keras.applications import MobileNetV3Large
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam

trainPath = "/home/student/Desktop/datahelmet/train"
ValidPath = "/home/student/Desktop/datahelmet/validate"


trainGenerator = ImageDataGenerator(
    rotation_range=15 , width_shift_range=0.1,
    height_shift_range=0.1, brightness_range=(0, 0.2)).flow_from_directory(trainPath, target_size=(224,224), batch_size=16)

ValidGenerator = ImageDataGenerator(
    rotation_range=15 , width_shift_range=0.1,
    height_shift_range=0.1, brightness_range=(0, 0.2)).flow_from_directory(ValidPath, target_size=(224,224), batch_size=16)


# Build the model
#
baseModel = MobileNetV3Large(weights="imagenet", include_top=False)
#
x = baseModel.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(128, activation='relu')(x)
x = Dense(128, activation='relu')(x)
x = Dense(64, activation='relu')(x)
x = Dense(64, activation='relu')(x)
#
predictionLayer = Dense(2, activation='softmax')(x)
#
model = Model(inputs=baseModel.input , outputs=predictionLayer)

print(model.summary())

# freeze the layers of the MobileNetV3 (already trained)

for layer in model.layers[:-5]:
    layer.trainable = False

# Compile

optimizer = Adam(learning_rate = 0.0001)
model.compile(loss= "categorical_crossentropy", optimizer=optimizer , metrics=['accuracy'])
#
# train
model.fit(trainGenerator, validation_data=ValidGenerator, epochs=50)
#
# modelSavedPath = "/Users/yoonjc0615/Downloads/fishmobilenet/data/dataset_for_model/fishV3.h5"
# model.save(modelSavedPath)


model_save_path = "/home/student/Desktop/HelmetV3.keras"

model.save(model_save_path)
print("Model saved successfully as .keras format.")
