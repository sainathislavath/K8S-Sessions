# EKS Deployment

Create Cluster:
```bash
eksctl create cluster --name buildflow-deployment-v1 --region us-west-2 --nodegroup-name standard-workers --node-type t3.medium --nodes 2 --nodes-min 1 --nodes-max 3
```

Configuring the kubectl with eks cluster:
```bash
aws eks --region us-west-2 update-kubeconfig --name buildflow-deployment-v1
```
Apply the k8s files:
```bash
kubectl apply -f Deployment.yml
```

To Monitor:
```bash
kubectl get services --watch
```

Delete EKS Cluster:
```bash
eksctl delete cluster --name buildflow-deployment-v1 --region us-west-2
```

Find all contexts (Cluster):
```bash
kubectl config get-contexts
```

Switching to the cluster:
```bash
kubectl config use-context docker-desktop
```