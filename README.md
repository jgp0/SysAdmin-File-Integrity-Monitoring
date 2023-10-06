# SysAdmin File Integrity Monitoring

The File Integrity Monitoring System is a tool developed in Python that allows system administrators to detect unauthorized changes to critical files in an IT infrastructure. This system ensures that critical files are not modified without authorization and provides alerts in case of unwanted changes.

## Requirements

- Python 3.x

## How to use
1. Execute of main script:
   
```python
python engine/main.py
```

2. How works?

    Keep the program running and it will monitor the directory you specify in the "directorio_monitoreado" variable. An alert will be displayed in the terminal in case you have modified any files within the monitored directory. In addition, the alert will be saved together with the file hash in a CSV file as a log.