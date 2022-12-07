# beng260-braille
Braille is the most common method of reading and writing that is learned and used by people with visual impairments and blindness. This tactile system utilizes matrices of raised dots, or “bumps”, on a target surface to represent different characters, punctuation, and symbols of a given language. In addition to the practical applications of this tactile coding system, researchers have also started studying how people learn and understand Braille to gain a better understanding of how the neural system of a visually impaired person is capable of creating new neural connections, referred to as neuroplasticity, to reroute mechanosensory information and compensate for a lack of visual perception in comparison to individuals without any visual impairments. The team proposed the development of a neural network computer algorithm that is capable of mimicking the process of learning and reading Braille by teaching Hodgkin-Huxley spiking neurons to respond to the tactile stimuli perceived from touching the raised dots that make up Braille. This model will aid in gaining a better understanding of how Braille is comprehended by people with visual impairments.

## Usage
Use the command ```python baseline.py <input sentence>``` to run the Braille simulation. <br/>
e.g. ```python baseline.py abcde```

```create_data.py <input sentence>```: generates the input data for Braille reading. The output is stored in the file named `data_seq.csv`.<br/>

```neurons.py```: defines the neurons utilized in the Braille reading model.<br/>

```Hodgkin_Huxley.py <input letter>```: simulates the resulting potential using the Hodgkin-Huxley model. Notice that the input letter should be in ```data_seq.csv```.<br/>

```alphabet.txt```: contains the alphabet letters and their corresponding Braille character. Other characters, such as symbols, can be added into the file to expand the dictionary.
