# message-positivity
A small NLP project to determine the positivity of reddit threads

In order for this to run you must set your reddit api client key and secret envrionment variables. This can be done by creating a kubernetes secret file called `secret.yaml` inside the `deployment` folder:
```
apiVersion: v1
kind: Secret
metadata:
  name: reddit-client-secrets
type: kubernetes.io/basic-auth
stringData:
  username: [CLIENTID]
  password: [CLIENTKEY]

```

You will also need to deploy and ingress controller. This can be done by running the following command:
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.1/deploy/static/provider/cloud/deploy.yaml
```

Finally to run the project in development mode use:
```
skaffold dev
```

# Dependencies
To install dependencies run:
`cd api && pip3 install -r requirements.txt`
