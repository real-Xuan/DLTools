import Augmentor

path_to_data = "dir"

#Create a pipeline
p = Augmentor.Pipeline(path_to_data)

#Add operations to pipeline

#Skew an image in a random direction, either left to right, top to bottom, or one of 8 corner directions.
p.skew(probability = 1.0, magnitude = 1.0)

#Rotate an image by an arbitrary amount.
p.rotate_random(probability = 1.0, max_left_rotation = 25, max_right_rotation = 25)

#Flip (mirror) the image along either its horizontal or vertical axis.
p.flip_random(probability = 1.0)

#histogram_equalisation
p.histogram_equalisation(probability = 1.0)

#Random change brightness of an image.
p.random_brightness(probability = 1.0, min_factor = 0.0, max_factor = 1.0)

#Random change saturation of an image.
p.random_color(probability = 1.0, min_factor = 0.0,max_factor = 1.0)

#Random change image contrast.
p.random_contrast(probability = 1.0, min_factor = 0.0, max_factor = 1.0)




#Samples
num_of _samples = int(1e5)
p.sample(num_of_samples)
