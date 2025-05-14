## How to run

### *Online: 
https://mmgkxuq3hr.us-east-1.awsapprunner.com/ 

*The url can be out for service due to billing

### Locally
0. Make sure you have python 3.11
1. Create a virtual environment
2. Activate the virtual environment
3. Install the dependencies
```
pip install -r requirements.txt
```
4. Create the .env file with the definition of the template
6. Run
```
python run.py
```
7. Visit and interact with the api in:
```
http://127.0.0.1:5000/api/docs

```
### Docker
Build the docker image
```
docker build -t blue-label-back .
```
Run the container in detached mode, mapping port 5000
```
docker run -d -p 5000:5000 --name blue-label-back blue-label-back