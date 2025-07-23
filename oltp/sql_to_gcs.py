from google.cloud import storage

def sql_To_Gcs(bucketname,foldername,filename,csv_file):
  client = storage.Client()
  try:
     bucket = client.get_bucket(bucketname)
     print('The bucket is already exist')
  except Exception as e:
     bucket = client.create_bucket(bucketname)
     print('The bucket has been created')
  blob = bucket.blob(f'{foldername}/{filename}')
  blob.upload_from_filename(csv_file)
  print('Sucessfully migrated data to GCS')