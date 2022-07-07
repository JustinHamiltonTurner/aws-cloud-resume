.PHONY: build

build:
	sam build

deploy-infra:
	sam build && sam deploy --profile jt-cloud-resume-challenge-v2 

deploy-site:
	aws s3 sync ./resume_site s3://jt0524-fantastic-website --profile jt-cloud-resume-challenge-v2 

reset-db:
	aws dynamodb put-item --profile jt-cloud-resume-challenge-v2 --table-name cloud-resume-challenge --item '{"id": {"S": "1"},  "visitorCount": {"N": "0"} }'