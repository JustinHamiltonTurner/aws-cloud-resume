-- 6/22/2022

https://www.youtube.com/watch?v=HOxsacd8Frw&list=PLEk97Q5Nj5oesA1WNk7DzaUpZUnCsQFVQ&index=4

- Manage AWS accounts and login
    - Installed aws-vault using scoop
    - "aws-vault list" shows current profiles
    - aws-vault login jt-cloud-resume-challenge-v2
- Setup SAM CLI
    - sam init
    - sam build
- Deploy SAM
    - sam deploy --guided --profile jt-aws-cloud-resume-challenge-v2 
    - Couldn't use aws-vault due to iam creation issue
- S3 Bucket

---
MyWebsite:
    Type: AWS::S3::Bucket
    Properties:
        BucketName: my-fantastic-website
---

-- NEXT: https://www.youtube.com/watch?v=kjJHttSUNRY&list=PLEk97Q5Nj5oesA1WNk7DzaUpZUnCsQFVQ&index=5

- Update S3 in template.yaml to include html and css

---
MyWebsite:
    Type: AWS::S3::Bucket
    Properties:
        AccessControl: PublicRead
        WebsiteConfiguration:
            IndexDocument: index.html
        BucketName: jt0524-fantastic-website
---

- Used Scoop to install make and then created make document. https://scoop.sh/#/apps?q=make&s=0&d=1&o=true

---

Transfers jhtresume.com between accounts:

aws route53domains transfer-domain-to-another-aws-account --domain-name jhtresume.com --account-id 198830422380 --region us-east-1 --profile iamadmin-jt-cloud-resume-challenge

{
    "OperationId": "6c5fc35d-b028-44de-a738-4be0498ce905",
    "Password": "oU6TK,GuVfxU&3"
}

aws route53domains accept-domain-transfer-from-another-aws-account --domain-name jhtresume.com --password "oU6TK,GuVfxU&3" --profile jt-cloud-resume-challenge-v2

{
    "OperationId": "00ff49ee-f1fd-43c4-97a4-ea17fc655748"
}

---
https://www.youtube.com/watch?v=50vzowTPdv0&list=PLEk97Q5Nj5oesA1WNk7DzaUpZUnCsQFVQ&index=16

CICD gihub actions with aws:
https://www.freecodecamp.org/news/how-to-setup-a-ci-cd-pipeline-with-github-actions-and-aws/