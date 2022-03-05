# message-positivity
A small NLP project to determine the positivity of messages

In order for this to run you must set your reddit api client key and secret envrionment variables. This can be done by creating a kustomize file called `kustomization.yaml` inside the `deployment` folder:
```
secretGenerator:
- name: reddit-client-secrets
  literals:
  - username=YOURCLIENTKEYHERE
  - password=YOURCLIENTSECRETWORDHERE

```

# Dependencies
To install dependencies run:
`cd api && pip3 install -r requirements.txt`
