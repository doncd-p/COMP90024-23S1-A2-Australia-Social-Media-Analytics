## Prerequisites
- Python 3.11.3
- Docker (optional)

## Running the Application
1. Run the application using Python:
```
pip install -r requirements.txt
python main.py
```
2. Alternatively, you can use Docker to build and run the application:
```
sudo docker image build -t backend .
sudo docker run -d --name backend --network di -p 0.0.0.0:8080:8080 backend:latest
```