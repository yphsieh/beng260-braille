# beng260-braille

## Usage
Use the command ```python baseline.py <input sentence>``` to run the Braille simulation. <br/>
e.g. ```python baseline.py abcde```

```create_data.py <input sentence>```: generates the input data for Braille reading. The output is stored in the file named `data_seq.csv`.<br/>
```neurons.py```: defines the neurons utilized in the Braille reading model.<br/>
```Hodgkin-Huxley.py <input letter>```: simulates the resulting potential using the Hodgkin-Huxley model. Notice that the input letter should be in ```data_seq.csv```.<br/>
