# cicd-pipeline-workshop

## Helm

### 基本 Helm 操作

```bash
# 建立 Chart 骨架
helm create demo-api

# 安裝 helm chart release 到指定 Namespace 底下
helm install [release] -n [namespace] demo-api/

# 列出指定 Namespace 底下安裝哪些 helm chart release
helm list -n [namespace]

# 升級 release
helm upgrade [release] -n [namespace] demo-api
```

### Values replacement

請參考資料夾 `example-helm-chart` 的變數替換方式，將 `demo-api/templates` 底下的 YAML 也做變數替換

### Helm 安裝

```
helm install <release-name> --namespace <user-id>
``` 