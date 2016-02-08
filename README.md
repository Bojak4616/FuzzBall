
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
./fuzzer --dst http://localhost --fuzz http --data "testData" 

```

