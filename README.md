# dataiku_application
Dataiku Hiring: Technical Assessment Inbox

## Publish image to ECR

### Build the image

Build
```
cd api
docker build -f Dockerfile -t api_image:latest .
```

Test local
```
docker run --rm -p5000:5000 api_image:latest
```

Do the get thing
```
casep@X1Carbon:~$ curl -s http://127.0.0.1:5000/api/time | jq
{
  "time": 1752485928.8066182
}
casep@X1Carbon:~$ curl -s http://127.0.0.1:5000/api/dummy | jq
{
  "error": "Not Found"
}
```

### Push to ECR

Login

```
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 777230094305.dkr.ecr.eu-central-1.amazonaws.com
```

Tag it
```
docker tag api_image:latest 777230094305.dkr.ecr.eu-central-1.amazonaws.com/api_image:latest
```

Push it
```
docker tag api_image:latest 777230094305.dkr.ecr.eu-central-1.amazonaws.com/api_image:latest
```

Test from ECR
```
docker run --rm -p5000:5000 777230094305.dkr.ecr.eu-central-1.amazonaws.com/api_image:latest


casep@X1Carbon:~$ curl -s http://127.0.0.1:5000/api/time | jq
{
  "time": 1752486288.4351952
}
casep@X1Carbon:~$ curl -s http://127.0.0.1:5000/api/dummy | jq
{
  "error": "Not Found"
}

```


## Terraform bits
