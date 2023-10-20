# cicd-pipeline-workshop

## Helm

### Create Sample Helm Chart

```bash
# Command
helm create demo-api

# Remove all files under demo-api/templates
rm -rf demo-api/templates/*
rm demo-api/values.yaml

# Create empty values.yaml
touch demo-api/values.yaml

# Copy sample YAML files
cp sample-yaml/* demo-api/templates
```

### Values replacement

請參考資料夾 `example-helm-chart` 的變數替換方式，將 `demo-api/templates` 底下的 YAML 也做變數替換

### Helm 安裝

```
helm install <release-name> --namespace <user-id>
``` 