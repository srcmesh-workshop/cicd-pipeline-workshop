# cicd-pipeline-workshop

## Helm

### 基本 Helm 操作

```bash
# 建立 Chart 骨架
helm create demo-api

# 安裝 helm chart release 到指定 Namespace 底下
helm install [release-name] -n [namespace] demo-api/

# 列出指定 Namespace 底下安裝哪些 helm chart release
helm list -n [namespace]

# 升級 release
helm upgrade [release-name] -n [namespace] demo-api/

# 修改完後產生 YAML 檢測 Chart 是否有問題 (靜態檢查)
helm template [release-name] -n [namespace] demo-api/
```

## 實作 1

**請直接修改 example-helm-chart 的內容，不要額外 copy**

1. 請將 `example-helm-chart/templates/api.yaml` 的 `image: python:latest` 替換成剛剛推送的鏡像
2. 請為 `example-helm-chart/templates/api.yaml` 加上對應的 `Image Pull Secret`
3. 請按照 `基本 Helm 操作` 步驟將修改過的 Helm Chart 部署到叢集你的 Namespace 內

## 實作 2

1. 請參考資料夾 `example-helm-chart/templates/nginx.yaml` 的變數替換方式，將其他欄位也進行替換

替換前請思考:
  - 替換的原則是什麼
  - `values.yaml` 的格式如何擺放

全部修改完後 git push 到你的 repo