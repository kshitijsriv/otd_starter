# otd_starter
how to get started with Open Transit Data platform

### 1. Install pip
```
sudo apt-get install python3-pip
```
### 2. Install virtualenv
```
sudo pip3 install virtualenv 
```
### 3. Create virtual environment and activate
```
virtualenv venv 
source venv/bin/activate
```
### 5. Install google transit library
```
pip install --upgrade gtfs-realtime-bindings
```
### 6. Install requirements
```
pip install -r requirements.txt
```
### 7. Add you OTD API key in starter.py file
```
API_KEY = "YOUR_API_KEY"
```
### 8. Run starter.py
```
python starter.py
```
