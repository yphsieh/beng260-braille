# beng260-braille
Braille is a tactile writing system of raised dots designed for people who are visually impaired. The system uses raised and unraised dots in six positions to represent a letter. In this project, we proposed a neuronal network along with a data generation method to simulate the Braille reading.

## Usage
Use the command ```python baseline.py <input sentence>``` to run the Braille simulation. <br/>
e.g. ```python baseline.py abcde```

```create_data.py <input sentence>```: generates the input data for Braille reading. The output is stored in the file named `data_seq.csv`.<br/>

```neurons.py```: defines the neurons utilized in the Braille reading model.<br/>

```Hodgkin_Huxley.py <input letter>```: simulates the resulting potential using the Hodgkin-Huxley model. Notice that the input letter should be in ```data_seq.csv```.<br/>

```alphabet.txt```: contains the alphabet letters and their corresponding Braille character. Other characters, such as symbols, can be added into the file to expand the dictionary.
