### Setup
pip install -r requirements.txt


### Test Fuzzing string
* Start python web server
``` 
python -m SimpleHTTPServer 

```

```
python Fuzzer.py --dst http://localhost(OR 127.0.0.1) --fuzz http --data "testData" --port 8000

or

./Fuzzer --dst http://localhost(127.0.0.1 --fuzz http --data "testData" --port 8000 

```

