from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
from keras.models import load_model

model = load_model('keras_model.h5')
img_path = r"D:\Freelancing\Fiverr\DJANGO\razan_alkhamisi\rawa_website\rawa_website\rawaProject\data\Plants_2\test\Basil healthy (P8)\0008_0001.JPG"  # Replace with the path to your input image
img = image.load_img(img_path, target_size=(224, 224))  # Adjust the target_size according to your model's input_shape
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Make predictions
predictions = model.predict(img_array)

predicted_class = np.argmax(predictions)

# If you have a list of class labels, you can get the corresponding label
class_labels = ["disease", "healthy"]  # Replace with your actual class labels
predicted_class_label = class_labels[predicted_class]

# Now, 'predicted_class' contains the index of the predicted class, and 'predicted_class_label' contains the corresponding label
print("Predicted class index:", predicted_class)
print("Predicted class label:", predicted_class_label)
# Now, 'predictions' contains the model's output for the given input image
