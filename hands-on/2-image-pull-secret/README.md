# Pull From Private Image Registry

Kubernetes 集群可以使用 image pull secret 從私有的鏡像倉庫或代碼倉庫拉取鏡像來創建 Pod。

## 準備工作

要生成 image pull secret，您可以使用以下命令：

```bash
kubectl create secret docker-registry <secret-name> \
    --docker-server=<your-registry-server> \
    --docker-username=<your-name> \
    --docker-password=<your-pword>
```

你可以在課程平台上找到上述資訊

## 使用 image pull secret

要使用 image pull secret，您需要將其添加到 Pod 的 spec 中。您可以使用以下 YAML 片段來指定 image pull secret：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: <image-name>
  imagePullSecrets:
  - name: <secret-name>
```

## 驗證

要驗證 Pod 是否能夠使用 image pull secret 拉取鏡像，您可以使用以下命令：

```
kubectl get pod <pod-name>
```

如果 Pod 的狀態為 Running，則表示 Pod 已成功拉取鏡像。

```bash
# 生成 secret
kubectl create secret docker-registry my-secret \
    --docker-server=<your-registry-server> \
    --docker-username=<your-name> \
    --docker-password=<your-pword>

# 查看 secret
kubectl get secret my-secret -o yaml

# 創建 Pod
kubectl apply -f my-pod.yaml

# 驗證 Pod
kubectl get pod my-pod
```

在上述範例中，我們將使用名為 my-secret 的 image pull secret 來拉取名為 nginx:latest 的鏡像。