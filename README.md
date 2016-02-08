
### About
2015 Wireshark fuzzer project

### Setup
pip install -r requirements.txt


### Test Fuzzing string
* Start python web server
``` 
python -m SimpleHTTPServer 

```


```
python Fuzzer.py --dst http://localhost --fuzz http --data "testData"

or

./Fuzzer --dst http://localhost --fuzz http --data "testData" 

```

