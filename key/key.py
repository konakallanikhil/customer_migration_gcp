import os
# credentials 
def service_Key_Credentials():
    try:
        path = r""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Credential file not found: {path}")
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path
    except Exception as e:
        print(f"Error setting credentials: {e}")
